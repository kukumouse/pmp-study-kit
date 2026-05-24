(function () {
  const usersKey = "pmpStudyUsersV1";
  const activeKey = "pmpStudyActiveUserV1";
  const defaultUser = "默认用户";

  function cleanName(name) {
    return String(name || "").trim().slice(0, 24);
  }

  function readUsers() {
    try {
      const users = JSON.parse(localStorage.getItem(usersKey));
      return Array.isArray(users) && users.length ? users : [defaultUser];
    } catch (error) {
      return [defaultUser];
    }
  }

  function writeUsers(users) {
    localStorage.setItem(usersKey, JSON.stringify(users));
  }

  function activeUser() {
    const users = readUsers();
    const active = cleanName(localStorage.getItem(activeKey));
    if (active && users.includes(active)) return active;
    localStorage.setItem(activeKey, users[0]);
    return users[0];
  }

  function setActiveUser(name) {
    const users = readUsers();
    if (users.includes(name)) localStorage.setItem(activeKey, name);
  }

  function addUser(name) {
    const cleaned = cleanName(name);
    if (!cleaned) return activeUser();
    const users = readUsers();
    if (!users.includes(cleaned)) {
      users.push(cleaned);
      writeUsers(users);
    }
    setActiveUser(cleaned);
    return cleaned;
  }

  function scopeKey(scope) {
    return `pmpStudy:${activeUser()}:${scope}`;
  }

  function read(scope, fallback) {
    try {
      const value = JSON.parse(localStorage.getItem(scopeKey(scope)));
      return value || fallback;
    } catch (error) {
      return fallback;
    }
  }

  function write(scope, value) {
    localStorage.setItem(scopeKey(scope), JSON.stringify(value));
  }

  function reset(scope) {
    localStorage.removeItem(scopeKey(scope));
  }

  function mount(target, onChange) {
    if (!target) {
      return { activeUser, read, write, reset };
    }

    function render() {
      const users = readUsers();
      const current = activeUser();
      target.innerHTML = `
        <div class="user-title">用户档案</div>
        <div class="user-row">
          <select aria-label="选择用户">${users.map((user) => `<option value="${user}" ${user === current ? "selected" : ""}>${user}</option>`).join("")}</select>
          <input type="text" maxlength="24" placeholder="新用户名">
          <button type="button">新增/切换</button>
        </div>
        <div class="user-hint">当前记录归属：<b>${current}</b></div>
      `;

      const select = target.querySelector("select");
      const input = target.querySelector("input");
      const button = target.querySelector("button");

      select.addEventListener("change", () => {
        setActiveUser(select.value);
        render();
        if (onChange) onChange();
      });

      button.addEventListener("click", () => {
        addUser(input.value);
        render();
        if (onChange) onChange();
      });
    }

    render();
    return { activeUser, read, write, reset };
  }

  window.PmpUsers = { activeUser, addUser, setActiveUser, read, write, reset, mount };
})();
