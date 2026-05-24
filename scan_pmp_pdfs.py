from pathlib import Path
from pypdf import PdfReader

FILES = [
    Path(r"D:\PMP考试相关资料\PMP新版通关宝典.pdf"),
    Path(r"D:\PMP考试相关资料\项目管理\PMP学习资料\PMBOK第七版中文版.pdf"),
    Path(r"D:\PMP考试相关资料\项目管理\PMP学习资料\PMI-敏捷实践指南.pdf"),
    Path(r"D:\PMP考试相关资料\项目管理\PMP学习资料\敏捷知识点补充—慧翔天地.pdf"),
    Path(r"D:\PMP考试相关资料\项目管理\PMP学习资料\2020-Scrum-Guide-Chinese-Simplified.pdf"),
]

KEYWORDS = [
    "资源管理", "资源管理计划", "团队章程", "建设团队", "管理团队", "控制资源",
    "获取资源", "估算活动资源", "冲突", "认可", "奖励", "RACI", "责任分配矩阵",
    "资源日历", "团队绩效", "虚拟团队",
    "敏捷", "Scrum", "产品负责人", "Scrum Master", "开发人员", "产品待办",
    "冲刺", "每日", "评审", "回顾", "燃尽", "看板", "WIP", "仆人式领导",
    "价值", "相关方", "治理", "合规", "变更", "风险",
]


def flatten_outline(outline):
    rows = []
    for item in outline or []:
        if isinstance(item, list):
            rows.extend(flatten_outline(item))
        else:
            title = getattr(item, "title", None)
            if title:
                rows.append(str(title))
    return rows


for path in FILES:
    print(f"\n=== {path.name} ===")
    try:
        reader = PdfReader(str(path))
    except Exception as exc:
        print(f"READ ERROR: {exc}")
        continue
    print(f"pages: {len(reader.pages)}")
    try:
        outline = flatten_outline(reader.outline)
        print("outline:")
        for title in outline[:60]:
            print(f"  - {title}")
        if len(outline) > 60:
            print(f"  ... {len(outline) - 60} more")
    except Exception as exc:
        print(f"outline error: {exc}")

    hits = {kw: [] for kw in KEYWORDS}
    max_pages = min(len(reader.pages), 450)
    for i in range(max_pages):
        try:
            text = reader.pages[i].extract_text() or ""
        except Exception:
            text = ""
        compact = text.replace("\n", " ")
        for kw in KEYWORDS:
            if kw.lower() in compact.lower():
                if len(hits[kw]) < 8:
                    hits[kw].append(i + 1)
    print("keyword pages:")
    for kw, pages in hits.items():
        if pages:
            print(f"  {kw}: {pages}")
