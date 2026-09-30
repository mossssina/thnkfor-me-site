// ════════════════════════════════════════════════════════
// THNKFOR.ME — Brand Style Guide
// Запуск: Figma → Plugins → Development → New Plugin
//         → вставь этот код в code.js → Run
// ════════════════════════════════════════════════════════

(async function () {

  // ── Цвета (0–1 диапазон) ────────────────────────────
  const C = {
    orange : { r: 1.000, g: 0.231, b: 0.000 }, // #FF3B00
    black  : { r: 0.039, g: 0.039, b: 0.039 }, // #0A0A0A
    bone   : { r: 0.973, g: 0.973, b: 0.973 }, // #F8F8F8
    dark   : { r: 0.078, g: 0.078, b: 0.078 }, // #141414
    muted  : { r: 0.400, g: 0.400, b: 0.400 }, // #666666
    white  : { r: 1.000, g: 1.000, b: 1.000 }, // #FFFFFF
  };

  function solid(color, opacity = 1) {
    return [{ type: 'SOLID', color, opacity }];
  }

  // ── Загрузка шрифтов ─────────────────────────────────
  await Promise.all([
    figma.loadFontAsync({ family: 'Space Grotesk', style: 'Medium'  }),
    figma.loadFontAsync({ family: 'Space Grotesk', style: 'Regular' }),
    figma.loadFontAsync({ family: 'IBM Plex Mono', style: 'Medium'  }),
    figma.loadFontAsync({ family: 'IBM Plex Mono', style: 'Regular' }),
  ]);

  // ── Хелперы ──────────────────────────────────────────
  function makeText(content, family, style, size, color) {
    const t = figma.createText();
    t.fontName = { family, style };
    t.fontSize = size;
    t.fills = solid(color);
    t.characters = content;
    return t;
  }

  function makeRect(w, h, color, opacity = 1) {
    const r = figma.createRectangle();
    r.resize(w, h);
    r.cornerRadius = 0;
    r.fills = solid(color, opacity);
    return r;
  }

  // Свободная позиция — правее существующего контента
  let startX = 0;
  for (const child of figma.currentPage.children) {
    startX = Math.max(startX, child.x + child.width + 200);
  }

  const W   = 1440;
  const PAD = 80;

  // ════════════════════════════════════════════════════
  // 1. COLORS
  // ════════════════════════════════════════════════════
  const f1 = figma.createFrame();
  f1.name = '01 — Colors';
  f1.resize(W, 580);
  f1.fills = solid(C.bone);
  f1.x = startX;
  f1.y = 0;
  figma.currentPage.appendChild(f1);

  // Секционная метка
  const lbl1 = makeText('01 — COLORS', 'IBM Plex Mono', 'Medium', 10, C.muted);
  lbl1.letterSpacing = { unit: 'PERCENT', value: 14 };
  lbl1.textCase = 'UPPER';
  lbl1.x = PAD; lbl1.y = PAD;
  f1.appendChild(lbl1);

  // Горизонтальная линия после метки
  const line1 = makeRect(W - PAD - lbl1.width - 24, 1, C.black, 0.1);
  line1.x = PAD + lbl1.width + 16; line1.y = PAD + 5;
  f1.appendChild(line1);

  // Плашки цветов
  const swatches = [
    { name: 'Signal Orange', hex: '#FF3B00', color: C.orange, w: 280, h: 200, light: false },
    { name: 'Machine Black', hex: '#0A0A0A', color: C.black,  w: 280, h: 200, light: false },
    { name: 'Bone',          hex: '#F8F8F8', color: C.bone,   w: 280, h: 200, light: true  },
    { name: 'Dark Surface',  hex: '#141414', color: C.dark,   w: 180, h: 120, light: false },
    { name: 'Muted',         hex: '#666666', color: C.muted,  w: 180, h: 120, light: false },
  ];

  let sx = PAD, sy = 120;
  swatches.forEach((s, i) => {
    if (i === 3) { sx = PAD; sy = 380; }

    const swatch = makeRect(s.w, s.h, s.color);
    if (s.light) {
      swatch.strokes = [{ type: 'SOLID', color: C.black, opacity: 0.12 }];
      swatch.strokeWeight = 1;
    }
    swatch.x = sx; swatch.y = sy;
    f1.appendChild(swatch);

    const nameT = makeText(s.name, 'Space Grotesk', 'Medium', 13, C.black);
    nameT.x = sx; nameT.y = sy + s.h + 12;
    f1.appendChild(nameT);

    const hexT = makeText(s.hex, 'IBM Plex Mono', 'Regular', 11, C.muted);
    hexT.x = sx; hexT.y = sy + s.h + 30;
    f1.appendChild(hexT);

    sx += s.w + 40;
  });

  // ════════════════════════════════════════════════════
  // 2. TYPOGRAPHY
  // ════════════════════════════════════════════════════
  const f2 = figma.createFrame();
  f2.name = '02 — Typography';
  f2.resize(W, 860);
  f2.fills = solid(C.bone);
  f2.x = startX;
  f2.y = 660;
  figma.currentPage.appendChild(f2);

  const lbl2 = makeText('02 — TYPOGRAPHY', 'IBM Plex Mono', 'Medium', 10, C.muted);
  lbl2.letterSpacing = { unit: 'PERCENT', value: 14 };
  lbl2.textCase = 'UPPER';
  lbl2.x = PAD; lbl2.y = PAD;
  f2.appendChild(lbl2);

  const line2 = makeRect(W - PAD - lbl2.width - 24, 1, C.black, 0.1);
  line2.x = PAD + lbl2.width + 16; line2.y = PAD + 5;
  f2.appendChild(line2);

  const typoRows = [
    { meta: 'Hero  /  Space Grotesk Medium  /  96px',  text: 'THNKFOR.ME',                  fam: 'Space Grotesk', sty: 'Medium',  sz: 96, ls: -2 },
    { meta: 'H1  /  Space Grotesk Medium  /  56px',    text: 'Думаем системами',              fam: 'Space Grotesk', sty: 'Medium',  sz: 56, ls: -1 },
    { meta: 'H2  /  Space Grotesk Regular  /  40px',   text: 'AI-агентство нового типа',      fam: 'Space Grotesk', sty: 'Regular', sz: 40 },
    { meta: 'Body  /  Space Grotesk Regular  /  18px', text: 'Мы строим системы, а не выполняем задачи.',  fam: 'Space Grotesk', sty: 'Regular', sz: 18 },
    { meta: 'Mono Label  /  IBM Plex Mono Medium  /  11px  /  UPPERCASE', text: 'SIGNAL ORANGE / #FF3B00 / BRAND COLOR', fam: 'IBM Plex Mono', sty: 'Medium', sz: 11, ls: 14, upper: true },
  ];

  let ty = 130;
  typoRows.forEach(row => {
    const metaT = makeText(row.meta, 'IBM Plex Mono', 'Regular', 10, C.muted);
    metaT.letterSpacing = { unit: 'PERCENT', value: 4 };
    metaT.x = PAD; metaT.y = ty;
    f2.appendChild(metaT);
    ty += 20;

    const sampleT = makeText(row.text, row.fam, row.sty, row.sz, C.black);
    if (row.ls) sampleT.letterSpacing = { unit: 'PERCENT', value: row.ls };
    if (row.upper) sampleT.textCase = 'UPPER';
    sampleT.x = PAD; sampleT.y = ty;
    f2.appendChild(sampleT);
    ty += row.sz * 1.4 + 32;

    const divider = makeRect(W - PAD * 2, 1, C.black, 0.08);
    divider.x = PAD; divider.y = ty;
    f2.appendChild(divider);
    ty += 28;
  });

  // ════════════════════════════════════════════════════
  // 3. COMPONENTS
  // ════════════════════════════════════════════════════
  const f3 = figma.createFrame();
  f3.name = '03 — Components';
  f3.resize(W, 560);
  f3.fills = solid(C.bone);
  f3.x = startX;
  f3.y = 1620;
  figma.currentPage.appendChild(f3);

  const lbl3 = makeText('03 — COMPONENTS', 'IBM Plex Mono', 'Medium', 10, C.muted);
  lbl3.letterSpacing = { unit: 'PERCENT', value: 14 };
  lbl3.textCase = 'UPPER';
  lbl3.x = PAD; lbl3.y = PAD;
  f3.appendChild(lbl3);

  const line3 = makeRect(W - PAD - lbl3.width - 24, 1, C.black, 0.1);
  line3.x = PAD + lbl3.width + 16; line3.y = PAD + 5;
  f3.appendChild(line3);

  // ── Кнопки ──
  const blbl = makeText('BUTTONS', 'IBM Plex Mono', 'Medium', 10, C.muted);
  blbl.letterSpacing = { unit: 'PERCENT', value: 8 }; blbl.textCase = 'UPPER';
  blbl.x = PAD; blbl.y = 120;
  f3.appendChild(blbl);

  // Primary
  const bp = makeRect(224, 52, C.black);
  bp.x = PAD; bp.y = 146;
  f3.appendChild(bp);
  const bpt = makeText('Запустить проект →', 'Space Grotesk', 'Medium', 14, C.bone);
  bpt.x = PAD + (224 - bpt.width) / 2;
  bpt.y = 146 + 18;
  f3.appendChild(bpt);

  // Ghost
  const bg = makeRect(224, 52, C.bone);
  bg.strokes = [{ type: 'SOLID', color: C.black }];
  bg.strokeWeight = 1;
  bg.x = PAD + 264; bg.y = 146;
  f3.appendChild(bg);
  const bgt = makeText('Узнать подробнее', 'Space Grotesk', 'Regular', 14, C.black);
  bgt.x = PAD + 264 + (224 - bgt.width) / 2;
  bgt.y = 146 + 18;
  f3.appendChild(bgt);

  // ── Header Badge ──
  const hblbl = makeText('HEADER BADGE', 'IBM Plex Mono', 'Medium', 10, C.muted);
  hblbl.letterSpacing = { unit: 'PERCENT', value: 8 }; hblbl.textCase = 'UPPER';
  hblbl.x = PAD; hblbl.y = 250;
  f3.appendChild(hblbl);

  const hbBg = makeRect(210, 28, C.black);
  hbBg.x = PAD; hbBg.y = 275;
  f3.appendChild(hbBg);
  const hbDot = makeRect(6, 6, C.orange);
  hbDot.x = PAD + 10; hbDot.y = 275 + 11;
  f3.appendChild(hbDot);
  const hbTxt = makeText('AI CONTENT AGENCY', 'IBM Plex Mono', 'Medium', 10, C.bone);
  hbTxt.letterSpacing = { unit: 'PERCENT', value: 14 };
  hbTxt.textCase = 'UPPER';
  hbTxt.x = PAD + 24; hbTxt.y = 275 + 9;
  f3.appendChild(hbTxt);

  // ── Section Label ──
  const slbl = makeText('SECTION LABEL', 'IBM Plex Mono', 'Medium', 10, C.muted);
  slbl.letterSpacing = { unit: 'PERCENT', value: 8 }; slbl.textCase = 'UPPER';
  slbl.x = PAD; slbl.y = 355;
  f3.appendChild(slbl);

  const stxt = makeText('01 — SERVICES', 'IBM Plex Mono', 'Medium', 10, C.muted);
  stxt.letterSpacing = { unit: 'PERCENT', value: 14 };
  stxt.x = PAD; stxt.y = 380;
  f3.appendChild(stxt);
  const sline = makeRect(W - PAD * 2 - stxt.width - 16, 1, C.black, 0.1);
  sline.x = PAD + stxt.width + 16; sline.y = 385;
  f3.appendChild(sline);

  // ── Tag ──
  const tlbl = makeText('TAG / CHIP', 'IBM Plex Mono', 'Medium', 10, C.muted);
  tlbl.letterSpacing = { unit: 'PERCENT', value: 8 }; tlbl.textCase = 'UPPER';
  tlbl.x = PAD; tlbl.y = 430;
  f3.appendChild(tlbl);

  const tagBg = makeRect(196, 32, C.bone);
  tagBg.strokes = [{ type: 'SOLID', color: C.black, opacity: 0.12 }];
  tagBg.strokeWeight = 1;
  tagBg.x = PAD; tagBg.y = 456;
  f3.appendChild(tagBg);
  const tagTxt = makeText('CONTENT MACHINE', 'IBM Plex Mono', 'Medium', 10, C.black);
  tagTxt.letterSpacing = { unit: 'PERCENT', value: 8 };
  tagTxt.textCase = 'UPPER';
  tagTxt.x = PAD + 14; tagTxt.y = 456 + 11;
  f3.appendChild(tagTxt);

  // Финал — зум на созданные фреймы
  figma.viewport.scrollAndZoomIntoView([f1, f2, f3]);
  figma.closePlugin('✅ THNKFOR.ME фирстиль создан — Colors, Typography, Components');

})();
