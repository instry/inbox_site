#!/usr/bin/env node

const pptxgen = require("pptxgenjs");

// Create presentation
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'AI Agent Solutions';
pres.title = 'AI Agent 企业解决方案商业计划';

// Color palette - Teal Trust (适合科技/AI主题)
const colors = {
  primary: "028090",      // Teal
  secondary: "00A896",    // Seafoam
  accent: "02C39A",       // Mint
  dark: "1E293B",         // Slate
  lightBg: "F8FAFC",      // Light gray
  white: "FFFFFF"
};

// Helper function to create shadow
const makeShadow = () => ({
  type: "outer",
  blur: 6,
  offset: 2,
  angle: 135,
  color: "000000",
  opacity: 0.15
});

// Slide 1: Title Slide
let slide1 = pres.addSlide();
slide1.background = { color: colors.primary };
slide1.addText("AI Agent 企业解决方案", {
  x: 0.5, y: 2, w: 9, h: 1,
  fontSize: 44, bold: true, color: colors.white,
  align: "center", fontFace: "Arial"
});
slide1.addText("让 AI 成为企业核心生产力", {
  x: 0.5, y: 3.2, w: 9, h: 0.6,
  fontSize: 24, color: colors.white,
  align: "center", fontFace: "Arial"
});
slide1.addText("2026", {
  x: 0.5, y: 4.5, w: 9, h: 0.4,
  fontSize: 16, color: colors.white,
  align: "center", fontFace: "Arial"
});

// Slide 2: 市场分析 - 核心痛点
let slide2 = pres.addSlide();
slide2.background = { color: colors.lightBg };
slide2.addText("市场分析：企业面临的核心痛点", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

const painPoints = [
  { title: "隐私安全'不敢用'", desc: "核心数据上传公有云存在泄露风险" },
  { title: "资源困境'用不起/用不到'", desc: "传统GPU方案成本100万+，顶尖模型难合规" },
  { title: "技术门槛'搞不定'", desc: "缺乏AI工程团队，部署维护困难" },
  { title: "业务落地'水土不服'", desc: "生态割裂，不懂业务，工具僵硬" }
];

let yPos = 1.3;
painPoints.forEach((point, idx) => {
  // Card background
  slide2.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 0.9,
    fill: { color: colors.white },
    shadow: makeShadow()
  });

  // Accent bar
  slide2.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 0.08, h: 0.9,
    fill: { color: colors.secondary }
  });

  // Title
  slide2.addText(point.title, {
    x: 0.8, y: yPos + 0.15, w: 4, h: 0.3,
    fontSize: 18, bold: true, color: colors.dark,
    fontFace: "Arial"
  });

  // Description
  slide2.addText(point.desc, {
    x: 0.8, y: yPos + 0.5, w: 8.4, h: 0.3,
    fontSize: 14, color: "64748B",
    fontFace: "Arial"
  });

  yPos += 1.05;
});

// Slide 3: 我们的解决方案
let slide3 = pres.addSlide();
slide3.background = { color: colors.lightBg };
slide3.addText("我们的解决方案", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

const solutions = [
  { title: "高性价比私有算力", desc: "2台 Mac Studio (M3 Ultra) 替代昂贵GPU服务器，数据完全本地化" },
  { title: "'交钥匙'交付", desc: "预装企微/钉钉/飞书集成，开箱即用，无需AI团队" },
  { title: "深度业务定制", desc: "定制开发专属Skill，完美适配企业实际业务场景" }
];

yPos = 1.5;
solutions.forEach((sol, idx) => {
  slide3.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 1.1,
    fill: { color: colors.white },
    shadow: makeShadow()
  });

  slide3.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 0.08,
    fill: { color: colors.accent }
  });

  slide3.addText(sol.title, {
    x: 0.8, y: yPos + 0.25, w: 8.4, h: 0.35,
    fontSize: 20, bold: true, color: colors.dark,
    fontFace: "Arial"
  });

  slide3.addText(sol.desc, {
    x: 0.8, y: yPos + 0.65, w: 8.4, h: 0.35,
    fontSize: 14, color: "64748B",
    fontFace: "Arial"
  });

  yPos += 1.3;
});

// Slide 4: 应用场景 - 全能差旅与行政专家
let slide4 = pres.addSlide();
slide4.background = { color: colors.lightBg };
slide4.addText("应用场景：全能差旅与行政专家", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

slide4.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 4.3, h: 3.8,
  fill: { color: colors.white },
  shadow: makeShadow()
});

slide4.addText("核心能力", {
  x: 0.8, y: 1.5, w: 3.7, h: 0.4,
  fontSize: 18, bold: true, color: colors.primary,
  fontFace: "Arial"
});

slide4.addText([
  { text: "跨应用执行", options: { bullet: true, breakLine: true } },
  { text: "主动服务", options: { bullet: true, breakLine: true } },
  { text: "持久记忆", options: { bullet: true } }
], {
  x: 1.0, y: 2.0, w: 3.5, h: 1.2,
  fontSize: 14, color: colors.dark,
  fontFace: "Arial"
});

slide4.addText("典型应用", {
  x: 0.8, y: 3.4, w: 3.7, h: 0.4,
  fontSize: 18, bold: true, color: colors.primary,
  fontFace: "Arial"
});

slide4.addText([
  { text: "全流程差旅管理", options: { bullet: true, breakLine: true } },
  { text: "航班延误主动改签", options: { bullet: true, breakLine: true } },
  { text: "记住老板所有偏好", options: { bullet: true } }
], {
  x: 1.0, y: 3.9, w: 3.5, h: 1.0,
  fontSize: 14, color: colors.dark,
  fontFace: "Arial"
});

// Right side
slide4.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 1.3, w: 4.3, h: 3.8,
  fill: { color: colors.primary },
  shadow: makeShadow()
});

slide4.addText("价值亮点", {
  x: 5.5, y: 1.6, w: 3.7, h: 0.5,
  fontSize: 22, bold: true, color: colors.white,
  fontFace: "Arial"
});

slide4.addText([
  { text: "7x24小时全天候", options: { breakLine: true } },
  { text: "像给同事发消息一样自然", options: { breakLine: true } },
  { text: "越用越懂你的需求", options: {} }
], {
  x: 5.5, y: 2.3, w: 3.7, h: 2.5,
  fontSize: 16, color: colors.white,
  fontFace: "Arial",
  lineSpacing: 24
});

// Slide 5: 应用场景 - 企业私有大脑
let slide5 = pres.addSlide();
slide5.background = { color: colors.lightBg };
slide5.addText("应用场景：企业私有大脑与分析师", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

const grid = [
  { title: "数据主权", desc: "完全离线运行\n物理隔绝风险" },
  { title: "深度理解", desc: "记住历史决策\n结合实时数据" },
  { title: "多模态洞察", desc: "看懂Excel/PDF\n直接生成结论" },
  { title: "上下文连贯", desc: "跨时间理解\n前后逻辑关联" }
];

const gridX = [0.5, 5.2];
const gridY = [1.5, 3.5];
let gridIdx = 0;

for (let row = 0; row < 2; row++) {
  for (let col = 0; col < 2; col++) {
    const item = grid[gridIdx];
    slide5.addShape(pres.shapes.RECTANGLE, {
      x: gridX[col], y: gridY[row], w: 4.3, h: 1.6,
      fill: { color: colors.white },
      shadow: makeShadow()
    });

    slide5.addText(item.title, {
      x: gridX[col] + 0.3, y: gridY[row] + 0.25, w: 3.7, h: 0.4,
      fontSize: 20, bold: true, color: colors.primary,
      fontFace: "Arial"
    });

    slide5.addText(item.desc, {
      x: gridX[col] + 0.3, y: gridY[row] + 0.75, w: 3.7, h: 0.7,
      fontSize: 14, color: colors.dark,
      fontFace: "Arial"
    });

    gridIdx++;
  }
}

// Slide 6: 核心业务价值
let slide6 = pres.addSlide();
slide6.background = { color: colors.lightBg };
slide6.addText("核心业务价值", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

const values = [
  { num: "7x24", label: "小时全天候待命", desc: "机器不休息，生产力不打烊" },
  { num: "1:100", label: "以一抵百", desc: "一个Agent=一支队伍" },
  { num: "100%", label: "私有安全", desc: "数据本地闭环，越用越懂你" }
];

yPos = 1.5;
values.forEach((val) => {
  slide6.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 1.1,
    fill: { color: colors.white },
    shadow: makeShadow()
  });

  // Big number
  slide6.addText(val.num, {
    x: 0.8, y: yPos + 0.15, w: 2, h: 0.8,
    fontSize: 48, bold: true, color: colors.accent,
    align: "center", valign: "middle",
    fontFace: "Arial"
  });

  // Label
  slide6.addText(val.label, {
    x: 3.0, y: yPos + 0.2, w: 3, h: 0.4,
    fontSize: 20, bold: true, color: colors.dark,
    fontFace: "Arial"
  });

  // Description
  slide6.addText(val.desc, {
    x: 3.0, y: yPos + 0.6, w: 6.2, h: 0.35,
    fontSize: 14, color: "64748B",
    fontFace: "Arial"
  });

  yPos += 1.3;
});

// Slide 7: 产品与服务体系
let slide7 = pres.addSlide();
slide7.background = { color: colors.lightBg };
slide7.addText("产品与服务体系", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

const products = [
  { layer: "硬件层", name: "AI 私有云一体机", desc: "Mac Studio M3 Ultra 集群，插电即用" },
  { layer: "系统层", name: "Agent Core 企业版", desc: "长期记忆+任务编排+工具调度" },
  { layer: "应用层", name: "场景化 Skill Store", desc: "通用+行业技能包，开箱即连" },
  { layer: "服务层", name: "陪跑式落地服务", desc: "部署+定制+培训+运维" }
];

yPos = 1.3;
products.forEach((prod) => {
  slide7.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 0.9,
    fill: { color: colors.white },
    shadow: makeShadow()
  });

  // Layer label
  slide7.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: yPos + 0.25, w: 1.2, h: 0.4,
    fill: { color: colors.secondary }
  });

  slide7.addText(prod.layer, {
    x: 0.7, y: yPos + 0.25, w: 1.2, h: 0.4,
    fontSize: 12, bold: true, color: colors.white,
    align: "center", valign: "middle",
    fontFace: "Arial"
  });

  // Product name
  slide7.addText(prod.name, {
    x: 2.1, y: yPos + 0.15, w: 3.5, h: 0.3,
    fontSize: 18, bold: true, color: colors.dark,
    fontFace: "Arial"
  });

  // Description
  slide7.addText(prod.desc, {
    x: 2.1, y: yPos + 0.5, w: 7.1, h: 0.3,
    fontSize: 14, color: "64748B",
    fontFace: "Arial"
  });

  yPos += 1.05;
});

// Slide 8: 商业模式
let slide8 = pres.addSlide();
slide8.background = { color: colors.lightBg };
slide8.addText("商业模式", {
  x: 0.5, y: 0.4, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.dark,
  fontFace: "Arial"
});

slide8.addText("一次性交付 + 持续订阅 + 增值服务", {
  x: 0.5, y: 1.1, w: 9, h: 0.4,
  fontSize: 18, color: colors.primary, italic: true,
  align: "center",
  fontFace: "Arial"
});

const bizModel = [
  {
    title: "硬件与基础软件销售",
    items: ["AI 一体机硬件销售", "Agent Core 永久授权"]
  },
  {
    title: "软件订阅服务 (年费)",
    items: ["模型与 Skill 升级包", "企业连接器维护"]
  },
  {
    title: "增值服务",
    items: ["定制开发服务", "培训与运维支持"]
  }
];

yPos = 1.8;
bizModel.forEach((model) => {
  slide8.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: yPos, w: 9, h: 1.2,
    fill: { color: colors.white },
    shadow: makeShadow()
  });

  slide8.addText(model.title, {
    x: 0.8, y: yPos + 0.2, w: 8.4, h: 0.35,
    fontSize: 18, bold: true, color: colors.dark,
    fontFace: "Arial"
  });

  slide8.addText(
    model.items.map((item, idx) => ({
      text: item,
      options: { bullet: true, breakLine: idx < model.items.length - 1 }
    })),
    {
      x: 1.2, y: yPos + 0.6, w: 7.8, h: 0.5,
      fontSize: 14, color: "64748B",
      fontFace: "Arial"
    }
  );

  yPos += 1.4;
});

// Slide 9: Thank You / Contact
let slide9 = pres.addSlide();
slide9.background = { color: colors.primary };
slide9.addText("让 AI 成为您企业的核心生产力", {
  x: 0.5, y: 2.2, w: 9, h: 0.8,
  fontSize: 36, bold: true, color: colors.white,
  align: "center", fontFace: "Arial"
});

slide9.addText("感谢您的关注", {
  x: 0.5, y: 3.2, w: 9, h: 0.5,
  fontSize: 20, color: colors.white,
  align: "center", fontFace: "Arial"
});

// Save presentation
pres.writeFile({ fileName: "bp.pptx" });
console.log("✅ Presentation created: bp.pptx");
