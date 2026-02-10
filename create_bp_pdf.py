#!/usr/bin/env python3
『『『
Create a professional business plan PDF from bp.md content
Using reportlab for professional formatting
『『『

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Check if Chinese fonts are available
try:
    # Try to register a system font that supports Chinese
    # On macOS, we can use PingFang SC or STHeiti
    pdfmetrics.registerFont(TTFont('PingFang', '/System/Library/Fonts/PingFang.ttc', subfontIndex=1))
    chinese_font = 'PingFang'
except:
    try:
        pdfmetrics.registerFont(TTFont('STHeiti', '/System/Library/Fonts/STHeiti Medium.ttc'))
        chinese_font = 'STHeiti'
    except:
        # Fallback to Helvetica (won't display Chinese properly, but won't crash)
        chinese_font = 'Helvetica'
        print(『Warning: Chinese fonts not available, using Helvetica as fallback『)

# Create PDF
doc = SimpleDocTemplate(『bp.pdf『, pagesize=A4,
                       rightMargin=0.75*inch, leftMargin=0.75*inch,
                       topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for the 'Flowable' objects
elements = []

# Define custom styles
styles = getSampleStyleSheet()

# Title style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName=chinese_font,
    fontSize=28,
    textColor=colors.HexColor('#028090'),
    spaceAfter=30,
    alignment=TA_CENTER,
    bold=True
)

# Subtitle style
subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Heading2'],
    fontName=chinese_font,
    fontSize=18,
    textColor=colors.HexColor('#028090'),
    spaceAfter=20,
    spaceBefore=20,
    bold=True
)

# Section header style
section_style = ParagraphStyle(
    'SectionHeader',
    parent=styles['Heading2'],
    fontName=chinese_font,
    fontSize=16,
    textColor=colors.HexColor('#00A896'),
    spaceAfter=12,
    spaceBefore=16,
    bold=True
)

# Subsection style
subsection_style = ParagraphStyle(
    'SubsectionHeader',
    parent=styles['Heading3'],
    fontName=chinese_font,
    fontSize=14,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=10,
    spaceBefore=12,
    bold=True
)

# Body text style
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontName=chinese_font,
    fontSize=11,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=8,
    alignment=TA_JUSTIFY,
    leading=16
)

# Bullet style
bullet_style = ParagraphStyle(
    'CustomBullet',
    parent=body_style,
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=6
)

# Cover Page
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph(『AI Agent 企业解决方案『, title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(『商业计划书『, subtitle_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(『让 AI 成为企业核心生产力『, body_style))
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph(『2026『, body_style))
elements.append(PageBreak())

# Section 1: 市场分析与痛点
elements.append(Paragraph(『1. 市场分析与痛点『, subtitle_style))

elements.append(Paragraph(『1.1 市场现状『, section_style))
elements.append(Paragraph(
    『2026年，我们正站在 ChatGPT 之后的又一个AI奇点上。AI 早已超越了『提效工具『的范畴，『
    『不再只是帮人写写邮件、查查资料的辅助角色。它正在深刻重构我们的工作流程、企业运作模式乃至生活方式。『
    'AI 已进化为能够与人类并肩作战、承担复杂任务的『核心队友『，成为维系未来企业生存与发展的『关键员工『。',
    body_style
))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(『1.2 核心痛点『, section_style))

pain_points = [
    (『隐私安全『不敢用『『, 『企业核心财务数据、客户名单、战略方案上传至公有云大模型，存在严重的数据泄露风险和合规隐患。『),
    (『资源困境『用不起/用不到『『, 『传统英伟达 GPU 方案采购及维护成本动辄 100万+，中小企业难以承担。顶尖模型在国内难以合规使用。『),
    (『技术门槛『搞不定『『, 『绝大多数传统企业缺乏专业的 AI 工程团队，面对复杂的环境部署、依赖管理以及模型微调难以落地。『),
    (『业务落地『水土不服『『, 『国外主流 AI 栈与中国企业特有的企微/钉钉/飞书生态无法直接互通，通用大模型不懂企业实际业务逻辑。『)
]

for title, desc in pain_points:
    elements.append(Paragraph(f『<b>{title}：</b>{desc}『, bullet_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(『1.3 我们的解决方案『, section_style))
elements.append(Paragraph(
    '针对上述痛点，我们提供一套<b>高性价比、完全私有化、且懂中国业务</b>的一站式 AI Agent 解决方案：',
    body_style
))

solutions = [
    (『高性价比私有算力『, 『采用 2台 Mac Studio (M3 Ultra) 集群方案，替代昂贵的英伟达GPU服务器。以极低成本运行高性能开源模型，实现数据完全本地化。『),
    (『『交钥匙『交付『, 『提供开箱即用的完整系统。预装企业微信/钉钉/飞书集成插件，打通国内主流办公生态。企业无需组建 AI 团队。『),
    (『深度业务定制『, 『结合企业实际业务场景，定制开发专属 Skill（技能）。无论是对接老旧 ERP 系统，还是执行复杂的财务核算流程，都能通过定制化开发完美适配。『)
]

for title, desc in solutions:
    elements.append(Paragraph(f『<b>{title}：</b>{desc}『, bullet_style))

elements.append(PageBreak())

# Section 2: 重新定义生产力
elements.append(Paragraph(『2. 重新定义生产力：从『对话『到『行动『『, subtitle_style))
elements.append(Paragraph(
    『我们将 AI 从简单的『问答机器『升级为拥有<b>长期记忆</b>、<b>主动执行力</b>和<b>工具使用能力</b>的『数字员工『。『
    '它运行在企业本地硬件上，数据不出域，能力可成长。',
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# Scenario 1
elements.append(Paragraph(『场景一：全能差旅与行政专家『, subsection_style))
elements.append(Paragraph(『<b>核心能力：</b>跨应用执行 + 主动服务『, body_style))
scenarios_1 = [
    '<b>全流程接管：</b>不仅是『订票『，而是全周期管理。实时监控航班状态，当检测到延误时，无需指令，主动改签并调整接送机与酒店时间。',
    '<b>自然交互：</b>员工通过企业微信/钉钉像给同事发消息一样下达指令：『下周去上海，按老规矩办『。',
    '<b>记忆回溯：</b>Agent 拥有长期记忆，自动调用老板『不住一楼『、『只要靠窗位『等历史偏好，无需每次重复交代。'
]
for item in scenarios_1:
    elements.append(Paragraph(item, bullet_style))
elements.append(Spacer(1, 0.15*inch))

# Scenario 2
elements.append(Paragraph(『场景二：企业私有大脑与分析师『, subsection_style))
elements.append(Paragraph(『<b>核心能力：</b>本地化部署 + 上下文连贯『, body_style))
scenarios_2 = [
    '<b>数据主权：</b>运行在本地，完全离线，物理隔绝公有云风险。',
    '<b>深度理解：</b>记得上个月的战略会纪要，当这月问『销售额为什么未达标『时，能结合上个月定下的 KPI 和 CRM 中的最新数据进行对比分析。',
    『<b>多模态洞察：</b>能『看懂『复杂的 Excel 报表、PDF 合同甚至监控截图，直接生成业务结论。『
]
for item in scenarios_2:
    elements.append(Paragraph(item, bullet_style))
elements.append(Spacer(1, 0.15*inch))

# Scenario 3
elements.append(Paragraph(『场景三：金牌客服与销售助理『, subsection_style))
elements.append(Paragraph(『<b>核心能力：</b>多渠道响应 + 情绪感知『, body_style))
scenarios_3 = [
    '<b>秒级响应：</b>接入企业微信/公众号后台。无论是凌晨 2 点的客户咨询，还是周末的售后投诉，Agent 都能在 3 秒内给予专业、有温度的回复。',
    '<b>金牌话术：</b>学习公司内部的金牌销售话术库。面对客户刁钻的询价，它能像拥有 10 年经验的老销售一样，巧妙化解异议。',
    『<b>无缝流转：</b>当检测到客户意向强烈或情绪激动时，自动生成摘要并无缝转接人工客服，确保服务体验。『
]
for item in scenarios_3:
    elements.append(Paragraph(item, bullet_style))

elements.append(PageBreak())

# Section 3: 核心业务价值
elements.append(Paragraph(『3. 核心业务价值『, subtitle_style))

values = [
    (『<b>7x24小时全天候待命：</b>『, 『机器不休息，生产力不打烊。无论是深夜的服务器报警，还是周末的紧急合同审核，Agent 随时响应，确保业务连续性。『),
    (『<b>『以一抵百『的万能助理：</b>『, 『打破岗位边界，一个 Agent 就是一支队伍。它既是财务专员（核算报销），也是客服主管（回复客户咨询），更是行政助理（安排行程）。『),
    (『<b>解放人类，告别重复劳动：</b>『, 『将员工从『填表、搬运数据、整理发票『等低价值重复性工作中彻底解放出来，专注于创造性决策和高价值客户服务。『),
    (『<b>私有安全，越用越懂你：</b>『, 『所有数据本地闭环，无需担心机密外泄。且随着交互数据的积累，它会越来越懂企业的业务逻辑和『潜规则『。『)
]

for title, desc in values:
    elements.append(Paragraph(f『{title}{desc}『, body_style))
    elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# Section 4: 产品与服务体系
elements.append(Paragraph(『4. 产品与服务体系『, subtitle_style))
elements.append(Paragraph(『我们提供从算力部署到上层应用的全栈式解决方案。『, body_style))
elements.append(Spacer(1, 0.2*inch))

# Create product matrix table
product_data = [
    ['产品层级', '产品名称', '核心特性'],
    ['硬件层', 'AI 私有云一体机', 'Mac Studio M3 Ultra 集群\n预装环境，插电即用'],
    ['系统层', 'Agent Core 企业版', '长期记忆 + 任务编排 + 工具调度\n50+ 企业连接器，安全网关'],
    ['应用层', '场景化 Skill Store', '通用技能包 + 行业技能包\n（制造版/电商版等）'],
    ['服务层', '陪跑式落地服务', '部署调试 + 定制开发\n员工培训 + 运维更新']
]

product_table = Table(product_data, colWidths=[1.2*inch, 2*inch, 3.3*inch])
product_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#028090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), chinese_font),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('FONTNAME', (0, 1), (-1, -1), chinese_font),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('TOPPADDING', (0, 1), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E2E8F0')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')])
]))

elements.append(product_table)
elements.append(PageBreak())

# Section 5: 商业模式
elements.append(Paragraph(『5. 商业模式『, subtitle_style))
elements.append(Paragraph(
    『我们采用 <b>『一次性交付 + 持续订阅 + 增值服务『</b> 的混合盈利模式，『
    '在降低企业准入门槛的同时，确保双方长期的共赢关系。',
    body_style
))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(『5.1 硬件与基础软件销售（一次性）『, section_style))
biz_items_1 = [
    'AI 一体机硬件销售：包含 Mac Studio 集群硬件成本及系统预装费用',
    『Agent Core 企业版授权：包含核心系统的永久使用权，让企业真正拥有资产『
]
for item in biz_items_1:
    elements.append(Paragraph(f『• {item}『, bullet_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(『5.2 软件订阅服务（年费）『, section_style))
biz_items_2 = [
    '模型与 Skill 升级包：按年收取订阅费，提供最新的LLM，以及通用 Skill 库的功能迭代',
    『企业连接器维护：确保企微、钉钉等第三方接口变动时，系统连接器能及时更新适配『
]
for item in biz_items_2:
    elements.append(Paragraph(f『• {item}『, bullet_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(『5.3 增值服务（按需定价）『, section_style))
biz_items_3 = [
    'Skill 定制开发：针对企业特殊业务流程（如特殊的报销审批链），提供定制开发服务',
    '培训与咨询：教会员工如何与『数字员工『协作，提供 Prompt 编写培训',
    『运维与技术支持：处理版本更新，故障修复，确保企业稳定使用最先进的AI能力『
]
for item in biz_items_3:
    elements.append(Paragraph(f『• {item}『, bullet_style))

elements.append(PageBreak())

# Section 6: 目标客户与市场定位
elements.append(Paragraph(『6. 目标客户与市场定位『, subtitle_style))

elements.append(Paragraph(『6.1 目标客户画像『, section_style))
target_customers = [
    (『<b>中小型制造企业（50-500人）：</b>『, 『需要生产排班、设备维护、订单管理等场景化 AI 助手。『),
    (『<b>成长型电商公司：</b>『, 『需要智能客服、商品描述生成、竞品监控等电商专属功能。『),
    (『<b>专业服务公司（法律/咨询/财务）：</b>『, 『对数据安全要求极高，需要文档分析、知识管理等能力。『),
    (『<b>重视数据安全的传统企业：</b>『, 『拒绝使用公有云AI服务，但希望享受AI红利的保守型企业。『)
]
for title, desc in target_customers:
    elements.append(Paragraph(f『{title}{desc}『, bullet_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(『6.2 竞争优势『, section_style))
advantages = [
    '<b>成本优势：</b>相比传统 GPU 方案节省 70% 初期投入，相比长期使用商业 API 节省 80% 运营成本。',
    '<b>合规优势：</b>完全私有化部署，满足数据安全法及行业合规要求（金融、医疗等）。',
    '<b>落地优势：</b>深度集成国内企业生态（企微、钉钉、飞书），开箱即用，无需二次开发。',
    『<b>成长优势：</b>随着使用积累长期记忆和业务理解，成为企业独有的 AI 资产。『
]
for item in advantages:
    elements.append(Paragraph(item, bullet_style))

elements.append(PageBreak())

# Section 7: 实施路线图
elements.append(Paragraph(『7. 实施路线图『, subtitle_style))

phases = [
    (『第一阶段（0-3个月）：『, [
        '交付硬件与基础系统',
        '完成企微/钉钉/飞书接入',
        '部署通用 Skill 包（会议纪要、文档处理、日程管理）',
        『培训关键用户『
    ]),
    (『第二阶段（3-6个月）：『, [
        '根据业务需求定制 1-2 个核心 Skill',
        '接入企业现有系统（ERP/CRM/OA）',
        '建立企业知识库',
        『扩大用户范围至全员『
    ]),
    (『第三阶段（6-12个月）：『, [
        '持续优化 Skill 库',
        '根据使用数据微调模型',
        '探索高级应用场景',
        『评估 ROI 与扩展需求『
    ])
]

for phase, items in phases:
    elements.append(Paragraph(phase, subsection_style))
    for item in items:
        elements.append(Paragraph(f『• {item}『, bullet_style))
    elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# Final page
elements.append(Spacer(1, 2.5*inch))
elements.append(Paragraph(『让 AI 成为您企业的核心生产力『, title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(『联系我们，开启数字化转型之旅『, body_style))

# Build PDF
doc.build(elements)
print(『✅ PDF created successfully: bp.pdf『)
