from pathlib import Path

OUT = Path(".")

STYLE = r"""
    :root{--ink:#172033;--muted:#607087;--line:#d7dfeb;--paper:#f6f8fc;--panel:#fff;--blue:#2563eb;--teal:#0f766e;--amber:#b45309;--rose:#be123c;--shadow:0 14px 34px rgba(22,34,55,.1)}
    *{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Microsoft YaHei","PingFang SC","Noto Sans CJK SC",Arial,sans-serif;line-height:1.5}main{max-width:1400px;margin:0 auto;padding:24px}.nav{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}.nav a{padding:8px 11px;border:1px solid var(--line);border-radius:8px;background:#fff;color:inherit;text-decoration:none}.panel{background:#fff;border:1px solid var(--line);border-radius:8px;box-shadow:var(--shadow)}.hero{display:grid;grid-template-columns:.9fr 1.3fr;gap:16px;align-items:stretch}.intro,.memory,.side,.section{padding:20px}h1{margin:0 0 10px;font-size:34px;line-height:1.16;letter-spacing:0}h2{margin:0 0 12px;font-size:20px;letter-spacing:0}h3{margin:0 0 8px;font-size:16px;letter-spacing:0}p{margin:0;color:var(--muted)}.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}.chip{padding:5px 10px;border-radius:999px;border:1px solid var(--line);background:#fff;color:#314058;font-size:13px}.quote{margin-top:14px;padding:12px;border-left:4px solid var(--blue);background:#f8fafc;color:#314058;border-radius:4px}.workspace{display:grid;grid-template-columns:minmax(760px,1fr) 360px;gap:16px;margin-top:16px;align-items:start}.flow{display:grid;grid-template-columns:repeat(var(--steps),minmax(150px,1fr));gap:16px;padding:16px;overflow-x:auto}.step{position:relative;min-height:170px;padding:14px;border:2px solid #dbeafe;border-radius:8px;background:#f8fbff;cursor:pointer;text-align:left}.step::after{content:"";position:absolute;right:-14px;top:52px;width:12px;height:12px;border-top:3px solid var(--blue);border-right:3px solid var(--blue);transform:rotate(45deg)}.step:last-child::after{display:none}.step:hover,.step.selected{outline:3px solid rgba(37,99,235,.18);background:#fff}.step small{display:block;color:var(--muted);margin-bottom:8px}.step b{display:block;margin-bottom:8px;font-size:16px}.step span{color:var(--muted);font-size:13px}.side{position:sticky;top:16px}.badge{display:inline-block;margin:0 6px 10px 0;padding:4px 8px;border-radius:999px;border:1px solid var(--line);background:#fff;color:#314058;font-size:12px}.block{margin-top:14px;padding-top:14px;border-top:1px solid var(--line)}.io{display:grid;gap:8px}.io div{padding:10px;border:1px solid #e5eaf2;border-radius:7px;background:#f8fafc;color:#314058;font-size:14px}.compare{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px}.card{padding:14px;border:1px solid var(--line);border-left:5px solid var(--blue);border-radius:8px;background:#fff}.card.teal{border-left-color:var(--teal)}.card.amber{border-left-color:var(--amber)}.card.rose{border-left-color:var(--rose)}.card ul{margin:8px 0 0;padding-left:18px;color:var(--muted)}.exam-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:12px}.exam{padding:12px;border-radius:8px;background:#f8fafc;border:1px solid #e5eaf2}.exam b{display:block;margin-bottom:5px}.formula{display:grid;grid-template-columns:repeat(var(--steps),1fr);gap:8px;margin-top:14px}.formula div{padding:10px;border-radius:8px;background:#eef5ff;color:#1746a2;text-align:center;font-weight:700;font-size:13px}@media(max-width:1100px){.hero,.workspace,.compare,.exam-grid,.formula{grid-template-columns:1fr}.side{position:static}.flow{grid-template-columns:1fr}.step::after{right:50%;top:auto;bottom:-14px;transform:translateX(50%) rotate(135deg)}}
"""

AREAS = [
    {
        "file": "pmp_integration_management_flow.html",
        "title": "整合管理关系流程图",
        "area": "整合管理",
        "summary": "整合管理是项目经理的总控台：授权项目、整合计划、执行工作、沉淀知识、监控全局、统一变更、正式收尾。",
        "quote": "口诀：章程给权，计划定法，执行产成果，监控看全局，变更统一批，收尾验收归档。",
        "steps": [
            ["制定项目章程", "启动", "授权", "正式批准项目或阶段，授权项目经理使用组织资源。", "商业文件、协议、事业环境因素、组织过程资产。", "项目章程、假设日志。", "看到正式任命、授权、发起人、高层边界，选章程。", "不要把章程和项目管理计划混淆：章程是授权，计划是怎么做。"],
            ["制定项目管理计划", "规划", "整合计划", "把各子计划和三大基准整合成统一项目管理计划。", "项目章程、其他过程输出、组织过程资产。", "项目管理计划。", "看到整合子计划、范围/进度/成本基准，选制定项目管理计划。", "不要在没有计划更新授权时私自改基准。"],
            ["指导与管理项目工作", "执行", "做项目", "按计划执行项目工作，产出可交付成果和工作绩效数据。", "项目管理计划、批准的变更请求。", "可交付成果、WPD、问题日志、变更请求。", "看到执行工作、产出成果、实施批准变更，选它。", "发现问题不等于直接改计划，可能要提出变更请求。"],
            ["管理项目知识", "执行", "沉淀经验", "使用现有知识并创造新知识，促进经验复用。", "可交付成果、项目文件、事业环境因素。", "经验教训登记册、项目管理计划更新。", "看到经验教训、知识分享、知识库、复盘，选它。", "不要只在收尾才考虑经验教训。"],
            ["监控项目工作", "监控", "看全局", "跟踪、审查和报告整体项目进展，实现项目目标。", "WPI、预测、项目管理计划。", "WPR、变更请求、计划和文件更新。", "看到汇总各领域状态、预测、全局报告，选监控项目工作。", "它是全局监控，不是某个领域的控制。"],
            ["实施整体变更控制", "监控", "批变更", "审查、批准、否决和管理所有变更，维护基准一致性。", "变更请求、项目管理计划、WPR。", "批准的变更请求、变更日志、计划和文件更新。", "看到基准变化、CCB、正式批准/否决，选它。", "不要口头批准或私自执行影响基准的变更。"],
            ["结束项目或阶段", "收尾", "归档", "正式完成项目或阶段，移交成果并更新组织过程资产。", "项目章程、项目管理计划、验收的可交付成果。", "最终产品/服务/成果移交、最终报告、OPA 更新。", "看到最终验收、移交、释放资源、归档，选收尾。", "没有验收的可交付成果时，不应直接收尾。"],
        ],
        "compare": [
            ["章程 vs 管理计划", "章程授权项目和项目经理；管理计划说明如何执行、监控和收尾。"],
            ["监控项目工作 vs 各控制过程", "监控项目工作看全局；控制范围/进度/成本等看局部领域。"],
            ["变更请求 vs 批准的变更请求", "变更请求先提交；批准后才进入执行过程实施。"],
        ],
        "exam": [
            "正式授权、任命项目经理：制定项目章程。",
            "整合所有子计划和基准：制定项目管理计划。",
            "实施批准的变更请求：指导与管理项目工作。",
            "经验教训、知识库、知识分享：管理项目知识。",
            "WPI 汇总为 WPR：监控项目工作。",
            "影响基准的变更：实施整体变更控制。",
        ],
    },
    {
        "file": "pmp_scope_management_flow.html",
        "title": "范围管理关系流程图",
        "area": "范围管理",
        "summary": "范围管理解决“做什么、不做什么、如何验收”。它从需求出发，形成范围说明书和 WBS，最后控制范围变化并确认验收。",
        "quote": "口诀：先定怎么管，再收需求；需求成范围，范围拆 WBS；内部先查质量，客户再确认范围。",
        "steps": [
            ["规划范围管理", "规划", "定规则", "规定如何定义、确认和控制范围及需求。", "项目章程、项目管理计划。", "范围管理计划、需求管理计划。", "看到范围怎么定义/确认/控制，选规划范围管理。", "不要和定义范围混淆：规划是定方法，不是写范围说明书。"],
            ["收集需求", "规划", "问需求", "确定、记录并管理相关方需要和需求。", "章程、相关方登记册、需求管理计划。", "需求文件、需求跟踪矩阵。", "看到访谈、焦点小组、问卷、原型、需求跟踪矩阵，选收集需求。", "不要直接跳到 WBS；先有需求。"],
            ["定义范围", "规划", "写范围", "制定项目和产品范围的详细描述。", "需求文件、章程、范围管理计划。", "项目范围说明书、项目文件更新。", "看到范围说明书、除外责任、验收标准，选定义范围。", "需求文件不是范围说明书。"],
            ["创建 WBS", "规划", "拆工作", "把项目可交付成果和项目工作分解为较小组件。", "范围说明书、需求文件、范围管理计划。", "范围基准、项目文件更新。", "看到 WBS、WBS 词典、工作包、范围基准，选创建 WBS。", "WBS 是可交付成果导向，不是活动清单。"],
            ["确认范围", "监控", "客户验收", "正式验收已完成的可交付成果。", "核实的可交付成果、范围基准。", "验收的可交付成果、变更请求。", "看到客户/发起人正式接受，选确认范围。", "内部检查是控制质量，不是确认范围。"],
            ["控制范围", "监控", "控变动", "监督项目和产品范围状态，管理范围基准变更。", "范围基准、WPD、需求文件。", "WPI、变更请求、计划和文件更新。", "看到范围蔓延、范围基准变化、未批准功能，选控制范围。", "客户提出新需求不等于直接做，先走变更。"],
        ],
        "compare": [
            ["收集需求 vs 定义范围", "收集需求拿到相关方需求；定义范围把需求转成项目范围说明书。"],
            ["创建 WBS vs 定义活动", "WBS 拆可交付成果/工作包；定义活动把工作包转成具体活动。"],
            ["控制质量 vs 确认范围", "控制质量是内部核实；确认范围是客户或发起人正式验收。"],
        ],
        "exam": [
            "需求文件、需求跟踪矩阵：收集需求。",
            "项目范围说明书：定义范围。",
            "WBS/WBS词典/范围基准：创建 WBS。",
            "核实的可交付成果进入确认范围。",
            "客户拒收成果：确认范围输出变更请求。",
            "范围蔓延：控制范围。",
        ],
    },
    {
        "file": "pmp_schedule_management_flow.html",
        "title": "进度管理关系流程图",
        "area": "进度管理",
        "summary": "进度管理把 WBS 工作包变成活动、顺序、持续时间和进度基准，再持续控制偏差。",
        "quote": "口诀：先定规则，再列活动；活动排顺序，再估时间；最后成进度，执行中控偏差。",
        "steps": [
            ["规划进度管理", "规划", "定规则", "规定如何规划、制定、管理和控制进度。", "项目章程、项目管理计划。", "进度管理计划。", "看到进度方法、工具、控制阈值，选规划进度管理。", "不是制定具体进度表。"],
            ["定义活动", "规划", "列活动", "识别为完成可交付成果需采取的具体活动。", "范围基准、进度管理计划。", "活动清单、活动属性、里程碑清单。", "看到活动清单、里程碑清单，选定义活动。", "WBS 工作包不是活动清单。"],
            ["排列活动顺序", "规划", "排依赖", "识别并记录活动之间的关系。", "活动清单、活动属性、里程碑清单。", "项目进度网络图、项目文件更新。", "看到 FS/SS/FF/SF、紧前关系、网络图，选排列活动顺序。", "不要和制定进度计划混淆。"],
            ["估算活动持续时间", "规划", "估时间", "估算完成单项活动所需工作时段。", "活动清单、资源需求、资源日历。", "持续时间估算、估算依据。", "看到三点估算、类比/参数估算、持续时间，选它。", "估持续时间不是估成本。"],
            ["制定进度计划", "规划", "成基准", "分析活动顺序、持续时间、资源和约束，生成进度模型。", "网络图、持续时间估算、资源日历、风险登记册。", "进度基准、项目进度计划、进度数据。", "看到关键路径、进度基准、进度压缩，选制定进度计划。", "进度基准形成后，变更要受控。"],
            ["控制进度", "监控", "控偏差", "监督进度状态，管理进度基准变更。", "进度基准、WPD、项目进度计划。", "WPI、进度预测、变更请求。", "看到 SPI、进度偏差、赶工/快速跟进执行中偏差，选控制进度。", "影响基准的调整要进入整体变更控制。"],
        ],
        "compare": [
            ["定义活动 vs 创建 WBS", "WBS 是范围分解；定义活动是把工作包变成进度活动。"],
            ["排列顺序 vs 制定进度计划", "排序只生成网络图；制定进度计划才生成进度基准。"],
            ["赶工 vs 快速跟进", "赶工加资源增成本；快速跟进并行活动增风险。"],
        ],
        "exam": [
            "活动清单：定义活动。",
            "网络图/依赖关系：排列活动顺序。",
            "持续时间估算：估算活动持续时间。",
            "关键路径/进度基准：制定进度计划。",
            "SPI、进度预测：控制进度。",
            "进度基准变化：整体变更控制。",
        ],
    },
    {
        "file": "pmp_cost_management_flow.html",
        "title": "成本管理关系流程图",
        "area": "成本管理",
        "summary": "成本管理回答项目要花多少钱、预算如何形成、执行中如何控制成本偏差。",
        "quote": "口诀：先定成本规则，再估每项成本；汇总成预算，执行看挣值。",
        "steps": [
            ["规划成本管理", "规划", "定规则", "规定如何估算、预算、管理、监督和控制成本。", "项目章程、项目管理计划。", "成本管理计划。", "看到成本单位、精确度、控制阈值、报告格式，选规划成本管理。", "不是算具体金额。"],
            ["估算成本", "规划", "估金额", "估算完成项目工作所需资金。", "成本管理计划、质量管理计划、资源需求。", "成本估算、估算依据、项目文件更新。", "看到类比、参数、三点、自下而上估算成本，选估算成本。", "估算成本不是制定预算。"],
            ["制定预算", "规划", "成基准", "汇总估算，确定授权的成本基准。", "成本估算、估算依据、进度计划、风险登记册。", "成本基准、项目资金需求、项目文件更新。", "看到成本基准、资金需求、管理储备/应急储备，选制定预算。", "成本基准不含管理储备。"],
            ["控制成本", "监控", "控偏差", "监督项目状态，更新成本，管理成本基准变更。", "成本基准、WPD、项目资金需求。", "WPI、成本预测、变更请求。", "看到 CV/CPI/EAC/ETC/VAC、挣值分析，选控制成本。", "成本超支不能私自动用管理储备或改基准。"],
        ],
        "compare": [
            ["估算成本 vs 制定预算", "估算成本算各活动/工作包成本；制定预算汇总并形成成本基准。"],
            ["应急储备 vs 管理储备", "应急储备用于已知未知，进成本基准；管理储备用于未知未知，不进成本基准。"],
            ["CPI vs SPI", "CPI 看成本效率；SPI 看进度效率。"],
        ],
        "exam": [
            "成本管理计划：规划成本管理。",
            "成本估算、估算依据：估算成本。",
            "成本基准、资金需求：制定预算。",
            "CPI<1 成本超支，CPI>1 成本节约。",
            "EAC/ETC/VAC：控制成本。",
            "成本基准变化：整体变更控制。",
        ],
    },
    {
        "file": "pmp_quality_management_flow.html",
        "title": "质量管理关系流程图",
        "area": "质量管理",
        "summary": "质量管理分三层：先定义质量标准，再管理过程质量，最后检查具体成果质量。",
        "quote": "口诀：规划质量定标准，管理质量改过程，控制质量查成果；查完成果再给客户确认范围。",
        "steps": [
            ["规划质量管理", "规划", "定标准", "识别项目和产品质量要求，规定如何证明符合要求。", "项目章程、需求文件、风险登记册。", "质量管理计划、质量测量指标。", "看到质量标准、质量测量指标、验收标准，选规划质量管理。", "不是执行测试。"],
            ["管理质量", "执行", "改过程", "把质量管理计划转化为可执行质量活动，改进过程。", "质量管理计划、质量测量指标、质量控制测量结果。", "质量报告、测试与评估文件、变更请求。", "看到质量审计、过程分析、根本原因、持续改进，选管理质量。", "不要和控制质量混淆：管理质量偏过程，控制质量偏成果。"],
            ["控制质量", "监控", "查成果", "监测和记录质量活动结果，核实可交付成果是否正确。", "可交付成果、质量测量指标、测试与评估文件、WPD。", "质量控制测量结果、核实的可交付成果、WPI、变更请求。", "看到检查、测试、核实的可交付成果，选控制质量。", "客户正式验收是确认范围，不是控制质量。"],
        ],
        "compare": [
            ["管理质量 vs 控制质量", "管理质量看过程是否有效；控制质量看成果是否合格。"],
            ["控制质量 vs 确认范围", "控制质量内部核实；确认范围客户/发起人验收。"],
            ["质量保证 vs 质量控制", "质量保证偏过程信心；质量控制偏检测结果。"],
        ],
        "exam": [
            "质量测量指标：规划质量管理。",
            "质量审计、过程分析：管理质量。",
            "测试、检查、核实成果：控制质量。",
            "核实的可交付成果：控制质量输出。",
            "验收的可交付成果：确认范围输出。",
            "质量问题影响基准：整体变更控制。",
        ],
    },
    {
        "file": "pmp_communications_management_flow.html",
        "title": "沟通管理关系流程图",
        "area": "沟通管理",
        "summary": "沟通管理解决谁需要什么信息、如何发、发得是否有效。",
        "quote": "口诀：先规划谁要什么信息，再管理沟通把信息发出去，最后监督沟通看是否有效。",
        "steps": [
            ["规划沟通管理", "规划", "定沟通", "基于相关方信息需求，制定沟通方法和计划。", "相关方登记册、项目管理计划、事业环境因素。", "沟通管理计划。", "看到沟通渠道、频率、格式、技术、相关方信息需求，选规划沟通管理。", "不是实际发送报告。"],
            ["管理沟通", "执行", "发信息", "确保项目信息及时、适当生成、收集、发布、存储和处置。", "沟通管理计划、WPR、项目文件。", "项目沟通记录、计划和文件更新。", "看到发布报告、开会、发送信息、管理沟通工件，选管理沟通。", "WPR 是监控项目工作形成，管理沟通负责传递。"],
            ["监督沟通", "监控", "看效果", "确保沟通满足项目和相关方的信息需求。", "沟通管理计划、项目沟通记录、WPD。", "WPI、变更请求、计划和文件更新。", "看到沟通不充分、信息没到位、沟通方式无效，选监督沟通。", "不要和管理相关方参与混淆：沟通关注信息流，相关方关注参与和关系。"],
        ],
        "compare": [
            ["管理沟通 vs 监督沟通", "管理沟通是执行发送信息；监督沟通是检查沟通是否有效。"],
            ["沟通管理 vs 相关方管理", "沟通管理管信息；相关方管理管期望、参与和关系。"],
            ["WPI vs WPR", "WPI 来自控制过程；WPR 是汇总报告，再通过沟通发出。"],
        ],
        "exam": [
            "谁需要什么信息：规划沟通管理。",
            "发送报告、分发信息：管理沟通。",
            "沟通方式无效、信息没满足需求：监督沟通。",
            "沟通问题导致参与不足：可能转到监督相关方参与。",
            "沟通计划要更新：变更请求。",
            "不要用一种报告满足所有相关方。",
        ],
    },
    {
        "file": "pmp_risk_management_flow.html",
        "title": "风险管理关系流程图",
        "area": "风险管理",
        "summary": "风险管理从定规则、识别风险、分析优先级、量化影响、规划应对，到执行和监督应对。",
        "quote": "口诀：先定风险规则，再识别；先定性排序，必要时定量；规划应对后要执行，执行后要监督。",
        "steps": [
            ["规划风险管理", "规划", "定规则", "定义如何开展风险管理活动。", "项目章程、项目管理计划、相关方登记册。", "风险管理计划。", "看到概率影响矩阵、风险类别、角色职责，选规划风险管理。", "不是识别具体风险。"],
            ["识别风险", "规划", "找风险", "识别单个项目风险和整体项目风险来源。", "风险管理计划、需求文件、估算、相关方登记册。", "风险登记册、风险报告。", "看到新风险、风险触发条件、风险登记册新增，选识别风险。", "风险识别贯穿项目，不只早期。"],
            ["实施定性风险分析", "规划", "排优先", "评估风险概率和影响，对风险排序。", "风险登记册、风险管理计划。", "项目文件更新。", "看到概率影响矩阵、风险排序、紧迫性，选定性。", "定性不计算具体金额/日期分布。"],
            ["实施定量风险分析", "规划", "算影响", "定量分析风险对项目目标的综合影响。", "风险登记册、风险报告、进度/成本基准。", "项目文件更新。", "看到蒙特卡洛、决策树、敏感性分析、EMV，选定量。", "不是所有项目都必须定量。"],
            ["规划风险应对", "规划", "定对策", "制定处理整体风险和单个风险的方案。", "风险登记册、风险报告、资源管理计划。", "变更请求、计划和文件更新。", "看到规避/转移/减轻/接受、开拓/分享/提高，选规划应对。", "计划了应对不等于已经执行。"],
            ["实施风险应对", "执行", "做对策", "执行商定的风险应对计划。", "风险管理计划、风险登记册、风险报告。", "变更请求、项目文件更新。", "看到风险责任人执行预定应对，选实施风险应对。", "临时救火不等于实施已规划的风险应对。"],
            ["监督风险", "监控", "看效果", "监督风险应对、跟踪已识别风险、识别新风险。", "风险管理计划、WPD、WPR。", "WPI、变更请求、文件更新。", "看到风险审计、储备分析、风险再评估，选监督风险。", "风险发生后要更新风险/问题并评估应对效果。"],
        ],
        "compare": [
            ["识别风险 vs 监督风险", "识别风险记录新风险；监督风险跟踪风险和应对效果，也会识别新风险。"],
            ["定性 vs 定量", "定性排序；定量计算数值影响。"],
            ["规划应对 vs 实施应对", "规划应对制定方案；实施应对执行方案。"],
        ],
        "exam": [
            "风险登记册初建/新增风险：识别风险。",
            "概率影响矩阵：定性风险分析。",
            "蒙特卡洛/决策树/EMV：定量风险分析。",
            "风险应对策略：规划风险应对。",
            "执行已商定应对：实施风险应对。",
            "风险审计/储备分析/再评估：监督风险。",
        ],
    },
    {
        "file": "pmp_procurement_management_flow.html",
        "title": "采购管理关系流程图",
        "area": "采购管理",
        "summary": "采购管理回答买什么、怎么签、怎么管合同和供应商绩效。",
        "quote": "口诀：先决定买不买、怎么买；再招标选卖方；签约后控制合同绩效和索赔。",
        "steps": [
            ["规划采购管理", "规划", "定采购", "记录采购决策，明确采购方法，识别潜在卖方。", "项目章程、商业文件、资源需求、风险登记册。", "采购管理计划、采购策略、招标文件、供方选择标准、自制或外购决策。", "看到合同类型、自制或外购、招标文件、采购策略，选规划采购。", "不是实际选择卖方。"],
            ["实施采购", "执行", "选卖方", "获取卖方应答，选择卖方并授予合同。", "采购文件、卖方建议书、采购管理计划。", "选定的卖方、协议、变更请求。", "看到投标人会议、建议书评价、合同授予、谈判，选实施采购。", "合同签完后才进入控制采购。"],
            ["控制采购", "监控", "管合同", "管理采购关系，监督合同绩效，必要时变更和关闭合同。", "协议、采购文档、批准的变更请求、WPD。", "结束的采购、WPI、变更请求、文件更新。", "看到供应商绩效、索赔、合同争议、采购审计，选控制采购。", "合同问题不能只当内部团队问题处理。"],
        ],
        "compare": [
            ["规划采购 vs 实施采购", "规划采购准备采购策略和文件；实施采购选择卖方并签协议。"],
            ["实施采购 vs 控制采购", "实施采购签合同；控制采购管理合同履行。"],
            ["采购变更 vs 整体变更", "合同变更影响基准时，也要进入整体变更控制。"],
        ],
        "exam": [
            "自制或外购、合同类型：规划采购管理。",
            "投标人会议、建议书评价：实施采购。",
            "选定卖方、协议：实施采购输出。",
            "索赔、争议、供应商绩效：控制采购。",
            "结束的采购：控制采购输出。",
            "外部资源通过采购获取。",
        ],
    },
    {
        "file": "pmp_stakeholder_management_flow.html",
        "title": "相关方管理关系流程图",
        "area": "相关方管理",
        "summary": "相关方管理从识别人，到规划参与策略，再主动管理关系，最后监督参与效果。",
        "quote": "口诀：先识别人，再定参与策略；执行中争取支持，监控中看策略是否有效。",
        "steps": [
            ["识别相关方", "启动", "找人", "识别相关方并分析其利益、参与度、相互依赖和影响。", "项目章程、商业文件、协议。", "相关方登记册、变更请求。", "看到权力利益方格、相关方登记册、谁影响项目，选识别相关方。", "相关方识别不是只在启动做，项目中也会更新。"],
            ["规划相关方参与", "规划", "定策略", "基于相关方需求、期望和影响制定参与策略。", "相关方登记册、项目章程、项目管理计划。", "相关方参与计划。", "看到当前/期望参与度、参与策略，选规划相关方参与。", "不是实际去沟通解决问题。"],
            ["管理相关方参与", "执行", "促参与", "与相关方沟通协作，满足需求，处理问题并争取支持。", "相关方参与计划、沟通管理计划、变更日志。", "变更请求、问题日志更新、项目文件更新。", "看到主动沟通、处理期望、争取支持、解决相关方问题，选管理相关方参与。", "这属于执行，不是监控。"],
            ["监督相关方参与", "监控", "看效果", "监督相关方关系，调整参与策略。", "相关方参与计划、项目沟通记录、WPD。", "WPI、变更请求、计划和文件更新。", "看到参与度不足、策略无效、需要调整参与计划，选监督相关方参与。", "不要和管理相关方参与混淆：监督是看策略是否有效。"],
        ],
        "compare": [
            ["管理相关方参与 vs 监督相关方参与", "管理是主动沟通和解决问题；监督是评估参与效果并调整策略。"],
            ["沟通管理 vs 相关方管理", "沟通管信息；相关方管期望、关系和支持度。"],
            ["识别相关方 vs 规划参与", "识别回答谁重要；规划回答怎么让他们参与。"],
        ],
        "exam": [
            "权力利益方格、相关方登记册：识别相关方。",
            "当前/期望参与度：规划相关方参与。",
            "相关方反对、需要争取支持：管理相关方参与。",
            "参与策略无效：监督相关方参与。",
            "沟通方法无效：监督沟通。",
            "关键相关方变化：更新相关方登记册。",
        ],
    },
]


TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
{style}
  </style>
</head>
<body>
<main style="--steps:{step_count}">
  <nav class="nav">
    <a href="pmp_knowledge_areas_dashboard.html">知识领域导航</a>
    <a href="pmp_2026_study_dashboard.html">驾驶舱</a>
    <a href="pmp_49_process_flowchart.html">49 过程</a>
    <a href="pmp_resource_management_flow.html">资源专项</a>
  </nav>
  <section class="hero">
    <div class="panel intro">
      <h1>{title}</h1>
      <p>{summary}</p>
      <div class="chips"><span class="chip">{area}</span><span class="chip">{step_count} 个过程</span><span class="chip">流程 + 易混点 + 做题抓手</span></div>
    </div>
    <div class="panel memory">
      <h2>一眼记忆</h2>
      <p>{summary}</p>
      <div class="formula">{formula}</div>
      <div class="quote">{quote}</div>
    </div>
  </section>
  <section class="workspace">
    <div class="panel"><div id="flow" class="flow"></div></div>
    <aside class="panel side">
      <span id="groupBadge" class="badge">{area}</span><span id="typeBadge" class="badge"></span>
      <h2 id="title"></h2><p id="summary"></p>
      <div class="block io">
        <div><b>主要输入/依据</b><br><span id="inputs"></span></div>
        <div><b>核心输出</b><br><span id="outputs"></span></div>
        <div><b>做题抓手</b><br><span id="cue"></span></div>
      </div>
      <div class="block"><h3>容易错成</h3><p id="trap"></p></div>
    </aside>
  </section>
  <section class="panel section">
    <h2>高频混淆边界</h2>
    <div class="compare">{compare}</div>
  </section>
  <section class="panel section">
    <h2>考试化判断</h2>
    <div class="exam-grid">{exam}</div>
  </section>
</main>
<script>
const steps = {steps_json};
const flow = document.getElementById("flow"), title = document.getElementById("title"), summary = document.getElementById("summary"), inputs = document.getElementById("inputs"), outputs = document.getElementById("outputs"), cue = document.getElementById("cue"), trap = document.getElementById("trap"), typeBadge = document.getElementById("typeBadge");
function render() {{
  flow.innerHTML = "";
  steps.forEach((step, index) => {{
    const btn = document.createElement("button");
    btn.className = "step";
    btn.innerHTML = `<small>${{index + 1}}. ${{step.phase}}</small><b>${{step.name}}</b><span>${{step.short}}<br>${{step.summary}}</span>`;
    btn.onclick = () => selectStep(step);
    flow.appendChild(btn);
  }});
  selectStep(steps[0]);
}}
function selectStep(step) {{
  title.textContent = step.name;
  summary.textContent = step.summary;
  inputs.textContent = step.inputs;
  outputs.textContent = step.outputs;
  cue.textContent = step.cue;
  trap.textContent = step.trap;
  typeBadge.textContent = step.phase;
  document.querySelectorAll(".step").forEach((item) => item.classList.toggle("selected", item.textContent.includes(step.name)));
}}
render();
</script>
</body>
</html>
"""


def js_array(steps):
    rows = []
    for s in steps:
        rows.append({
            "name": s[0],
            "phase": s[1],
            "short": s[2],
            "summary": s[3],
            "inputs": s[4],
            "outputs": s[5],
            "cue": s[6],
            "trap": s[7],
        })
    import json
    return json.dumps(rows, ensure_ascii=False)


for area in AREAS:
    formula = "".join(f"<div>{step[2]}</div>" for step in area["steps"])
    compare = "".join(
        f'<div class="card {["teal","amber","rose"][i % 3]}"><h3>{title}</h3><ul><li>{text}</li></ul></div>'
        for i, (title, text) in enumerate(area["compare"])
    )
    exam = "".join(f"<div class='exam'><b>{item.split('：')[0]}</b>{'：'.join(item.split('：')[1:]) if '：' in item else item}</div>" for item in area["exam"])
    html = TEMPLATE.format(
        title=area["title"],
        area=area["area"],
        summary=area["summary"],
        quote=area["quote"],
        step_count=len(area["steps"]),
        style=STYLE,
        formula=formula,
        compare=compare,
        exam=exam,
        steps_json=js_array(area["steps"]),
    )
    (OUT / area["file"]).write_text(html, encoding="utf-8")
    print(area["file"])
