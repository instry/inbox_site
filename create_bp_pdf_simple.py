#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Chinese font
try:
    pdfmetrics.registerFont(TTFont('PingFang', '/System/Library/Fonts/PingFang.ttc', subfontIndex=1))
    chinese_font = 'PingFang'
except:
    try:
        pdfmetrics.registerFont(TTFont('STHeiti', '/System/Library/Fonts/STHeiti Medium.ttc'))
        chinese_font = 'STHeiti'
    except:
        chinese_font = 'Helvetica'

# Create PDF
doc = SimpleDocTemplate("bp.pdf", pagesize=A4,
                       rightMargin=0.75*inch, leftMargin=0.75*inch,
                       topMargin=0.75*inch, bottomMargin=0.75*inch)

elements = []
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'],
    fontName=chinese_font, fontSize=28, textColor=colors.HexColor('#028090'),
    spaceAfter=30, alignment=TA_CENTER, bold=True)

subtitle_style = ParagraphStyle('CustomSubtitle', parent=styles['Heading2'],
    fontName=chinese_font, fontSize=18, textColor=colors.HexColor('#028090'),
    spaceAfter=20, spaceBefore=20, bold=True)

section_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'],
    fontName=chinese_font, fontSize=16, textColor=colors.HexColor('#00A896'),
    spaceAfter=12, spaceBefore=16, bold=True)

subsection_style = ParagraphStyle('SubsectionHeader', parent=styles['Heading3'],
    fontName=chinese_font, fontSize=14, textColor=colors.HexColor('#1E293B'),
    spaceAfter=10, spaceBefore=12, bold=True)

body_style = ParagraphStyle('CustomBody', parent=styles['Normal'],
    fontName=chinese_font, fontSize=11, textColor=colors.HexColor('#1E293B'),
    spaceAfter=8, alignment=TA_JUSTIFY, leading=16)

bullet_style = ParagraphStyle('CustomBullet', parent=body_style,
    leftIndent=20, bulletIndent=10, spaceAfter=6)

# Cover Page
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("AI Agent 企业解决方案", title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("商业计划书", subtitle_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("让 AI 成为企业核心生产力", body_style))
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph("2026", body_style))
elements.append(PageBreak())

# Section 1
elements.append(Paragraph("1. 市场分析与痛点", subtitle_style))
elements.append(Paragraph("1.1 市场现状", section_style))
elements.append(Paragraph("2026年，AI 已进化为能够与人类并肩作战、承担复杂任务的核心队友，成为维系未来企业生存与发展的关键员工。", body_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph("1.2 核心痛点", section_style))
elements.append(Paragraph("• 隐私安全问题：企业核心数据上传至公有云存在严重的数据泄露风险", bullet_style))
elements.append(Paragraph("• 资源困境：传统GPU方案成本100万+，中小企业难以承担", bullet_style))
elements.append(Paragraph("• 技术门槛：缺乏专业AI工程团队，部署维护困难", bullet_style))
elements.append(Paragraph("• 业务落地：生态割裂，不懂业务，工具僵硬", bullet_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph("1.3 我们的解决方案", section_style))
elements.append(Paragraph("针对上述痛点，我们提供一套高性价比、完全私有化、且懂中国业务的一站式 AI Agent 解决方案。", body_style))
elements.append(Paragraph("• 高性价比私有算力：采用Mac Studio集群，以极低成本运行高性能模型", bullet_style))
elements.append(Paragraph("• 交钥匙交付：预装企微/钉钉/飞书集成，开箱即用", bullet_style))
elements.append(Paragraph("• 深度业务定制：定制开发专属Skill，完美适配企业实际业务场景", bullet_style))
elements.append(PageBreak())

# Section 2
elements.append(Paragraph("2. 重新定义生产力", subtitle_style))
elements.append(Paragraph("我们将 AI 从简单的问答机器升级为拥有长期记忆、主动执行力和工具使用能力的数字员工。", body_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph("场景一：全能差旅与行政专家", subsection_style))
elements.append(Paragraph("核心能力：跨应用执行 + 主动服务", body_style))
elements.append(Paragraph("• 全流程接管：实时监控航班状态，主动改签并调整行程", bullet_style))
elements.append(Paragraph("• 自然交互：像给同事发消息一样下达指令", bullet_style))
elements.append(Paragraph("• 记忆回溯：自动调用历史偏好，无需重复交代", bullet_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("场景二：企业私有大脑与分析师", subsection_style))
elements.append(Paragraph("核心能力：本地化部署 + 上下文连贯", body_style))
elements.append(Paragraph("• 数据主权：完全离线运行，物理隔绝风险", bullet_style))
elements.append(Paragraph("• 深度理解：结合历史数据进行对比分析", bullet_style))
elements.append(Paragraph("• 多模态洞察：看懂Excel/PDF，直接生成业务结论", bullet_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("场景三：金牌客服与销售助理", subsection_style))
elements.append(Paragraph("• 秒级响应：7x24小时专业回复", bullet_style))
elements.append(Paragraph("• 金牌话术：学习内部销售话术库", bullet_style))
elements.append(Paragraph("• 无缝流转：智能识别并转接人工客服", bullet_style))
elements.append(PageBreak())

# Section 3
elements.append(Paragraph("3. 核心业务价值", subtitle_style))
elements.append(Paragraph("• 7x24小时全天候待命：机器不休息，生产力不打烊", bullet_style))
elements.append(Paragraph("• 以一抵百的万能助理：一个Agent就是一支队伍", bullet_style))
elements.append(Paragraph("• 解放人类告别重复劳动：专注创造性决策和高价值服务", bullet_style))
elements.append(Paragraph("• 私有安全越用越懂你：数据本地闭环，越来越懂企业业务", bullet_style))
elements.append(PageBreak())

# Section 4
elements.append(Paragraph("4. 产品与服务体系", subtitle_style))
product_data = [
    ['产品层级', '产品名称', '核心特性'],
    ['硬件层', 'AI私有云一体机', 'Mac Studio集群\n预装环境，插电即用'],
    ['系统层', 'Agent Core企业版', '长期记忆+任务编排+工具调度\n50+企业连接器'],
    ['应用层', '场景化Skill Store', '通用+行业技能包\n开箱即连'],
    ['服务层', '陪跑式落地服务', '部署+定制+培训+运维']
]
product_table = Table(product_data, colWidths=[1.2*inch, 2*inch, 3.3*inch])
product_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#028090')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, -1), chinese_font),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E2E8F0')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
]))
elements.append(product_table)
elements.append(PageBreak())

# Section 5
elements.append(Paragraph("5. 商业模式", subtitle_style))
elements.append(Paragraph("我们采用一次性交付+持续订阅+增值服务的混合盈利模式。", body_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("5.1 硬件与基础软件销售", section_style))
elements.append(Paragraph("• AI一体机硬件销售：包含硬件成本及系统预装费用", bullet_style))
elements.append(Paragraph("• Agent Core企业版授权：永久使用权", bullet_style))
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("5.2 软件订阅服务（年费）", section_style))
elements.append(Paragraph("• 模型与Skill升级包：提供最新LLM和功能迭代", bullet_style))
elements.append(Paragraph("• 企业连接器维护：确保第三方接口及时更新适配", bullet_style))
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("5.3 增值服务（按需定价）", section_style))
elements.append(Paragraph("• Skill定制开发：针对特殊业务流程定制开发", bullet_style))
elements.append(Paragraph("• 培训与咨询：员工协作培训和Prompt编写培训", bullet_style))
elements.append(Paragraph("• 运维与技术支持：版本更新，故障修复", bullet_style))
elements.append(PageBreak())

# Final page
elements.append(Spacer(1, 2.5*inch))
elements.append(Paragraph("让 AI 成为您企业的核心生产力", title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("联系我们，开启数字化转型之旅", body_style))

# Build PDF
doc.build(elements)
print("✅ PDF created successfully: bp.pdf")
