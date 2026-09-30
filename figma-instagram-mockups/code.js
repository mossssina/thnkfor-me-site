// ════════════════════════════════════════════════════════════════
// THNKFOR.ME — Instagram Mockups (все форматы 2026)
// Запуск: Plugins → Development → Import plugin from manifest...
//         → выбери manifest.json → Run
// ════════════════════════════════════════════════════════════════

(async function () {

  // ── Цветовая палитра (0–1) ───────────────────────────────────
  const C = {
    orange : { r: 1.000, g: 0.231, b: 0.000 }, // #FF3B00
    black  : { r: 0.039, g: 0.039, b: 0.039 }, // #0A0A0A
    bone   : { r: 0.973, g: 0.973, b: 0.973 }, // #F8F8F8
    muted  : { r: 0.400, g: 0.400, b: 0.400 }, // #666666
    white  : { r: 1.000, g: 1.000, b: 1.000 }, // #FFFFFF
  };

  function solid(color, opacity = 1) {
    return [{ type: 'SOLID', color, opacity }];
  }

  // ── Загрузка шрифтов ─────────────────────────────────────────
  await Promise.all([
    figma.loadFontAsync({ family: 'Space Grotesk', style: 'Medium'  }),
    figma.loadFontAsync({ family: 'Space Grotesk', style: 'Regular' }),
    figma.loadFontAsync({ family: 'IBM Plex Mono', style: 'Medium'  }),
    figma.loadFontAsync({ family: 'IBM Plex Mono', style: 'Regular' }),
  ]);

  // ── Хелперы ──────────────────────────────────────────────────
  function txt(content, family, style, size, color, opts = {}) {
    const t = figma.createText();
    t.fontName = { family, style };
    t.fontSize = size;
    t.fills = solid(color);
    if (opts.letterSpacing) t.letterSpacing = { unit: 'PERCENT', value: opts.letterSpacing };
    if (opts.textCase) t.textCase = opts.textCase;
    if (opts.lineHeight) t.lineHeight = { unit: 'PERCENT', value: opts.lineHeight };
    if (opts.width) { t.textAutoResize = 'HEIGHT'; t.resize(opts.width, 100); }
    t.characters = content;
    if (opts.width) t.resize(opts.width, t.height);
    return t;
  }

  function rect(w, h, color, opacity = 1) {
    const r = figma.createRectangle();
    r.resize(w, h);
    r.cornerRadius = 0;
    r.fills = solid(color, opacity);
    return r;
  }

  // Найти свободное место правее существующего контента
  let startX = 0;
  for (const child of figma.currentPage.children) {
    startX = Math.max(startX, child.x + child.width + 120);
  }

  const GAP = 80; // отступ между мокапами
  const allFrames = [];

  // ══════════════════════════════════════════════════════════════
  // ЛЕЙБЛ-ХЕЛПЕР (метка над каждым мокапом)
  // ══════════════════════════════════════════════════════════════
  function addLabel(label, x, y) {
    const l = txt(label, 'IBM Plex Mono', 'Medium', 11, C.muted, { letterSpacing: 10, textCase: 'UPPER' });
    l.x = x;
    l.y = y - 28;
    figma.currentPage.appendChild(l);
  }

  // ══════════════════════════════════════════════════════════════
  // 1. FEED POST PORTRAIT 4:5 — «Доказательство»
  //    Реальный: 1080×1350px | Figma: 540×675px
  // ══════════════════════════════════════════════════════════════
  const f1 = figma.createFrame();
  f1.name = 'Feed Post 4:5 — Доказательство';
  f1.resize(540, 675);
  f1.fills = solid(C.black);
  f1.x = startX;
  f1.y = 100;
  figma.currentPage.appendChild(f1);
  allFrames.push(f1);
  addLabel('Feed Portrait 4:5  |  1080×1350px  |  ПРИОРИТЕТ ①', f1.x, f1.y);

  // Верхний label
  const f1label = txt('RESULT / 2026', 'IBM Plex Mono', 'Medium', 10, C.muted, { letterSpacing: 14, textCase: 'UPPER' });
  f1label.x = 32; f1label.y = 36;
  f1.appendChild(f1label);

  // Главное число
  const f1num = txt('×12', 'Space Grotesk', 'Medium', 96, C.orange);
  f1num.x = 32; f1num.y = 220;
  f1.appendChild(f1num);

  // Пояснение
  const f1sub = txt('постов в месяц автоматически', 'Space Grotesk', 'Regular', 16, C.bone, { width: 476, lineHeight: 140 });
  f1sub.x = 32; f1sub.y = 340;
  f1.appendChild(f1sub);

  // Горизонтальная линия-акцент
  const f1line = rect(476, 1, C.orange, 0.3);
  f1line.x = 32; f1line.y = 330;
  f1.appendChild(f1line);

  // Нижний логотип
  const f1logo = txt('THNKFOR.ME', 'IBM Plex Mono', 'Medium', 10, C.muted, { letterSpacing: 14, textCase: 'UPPER' });
  f1logo.x = 32; f1logo.y = 628;
  f1.appendChild(f1logo);

  // Оранжевая точка — правый нижний угол
  const f1dot = rect(6, 6, C.orange);
  f1dot.x = 502; f1dot.y = 630;
  f1.appendChild(f1dot);

  let curX = f1.x + f1.width + GAP;

  // ══════════════════════════════════════════════════════════════
  // 2. STORIES 9:16 — вопрос/опрос
  //    Реальный: 1080×1920px | Figma: 540×960px
  // ══════════════════════════════════════════════════════════════
  const f2 = figma.createFrame();
  f2.name = 'Stories 9:16 — Опрос';
  f2.resize(540, 960);
  f2.fills = solid(C.bone);
  f2.x = curX;
  f2.y = 100;
  figma.currentPage.appendChild(f2);
  allFrames.push(f2);
  addLabel('Stories 9:16  |  1080×1920px  |  Safe zone 250/400px', f2.x, f2.y);

  // Safe zone — верхняя (250px реал → 125px Figma)
  const f2safeTop = rect(540, 125, C.black, 0.04);
  f2safeTop.x = 0; f2safeTop.y = 0;
  f2.appendChild(f2safeTop);
  const f2safeTopTxt = txt('safe zone', 'IBM Plex Mono', 'Regular', 9, C.muted, { letterSpacing: 8 });
  f2safeTopTxt.x = 16; f2safeTopTxt.y = 54;
  f2.appendChild(f2safeTopTxt);

  // Safe zone — нижняя (400px реал → 200px Figma)
  const f2safeBot = rect(540, 200, C.black, 0.04);
  f2safeBot.x = 0; f2safeBot.y = 760;
  f2.appendChild(f2safeBot);
  const f2safeBotTxt = txt('safe zone', 'IBM Plex Mono', 'Regular', 9, C.muted, { letterSpacing: 8 });
  f2safeBotTxt.x = 16; f2safeBotTxt.y = 840;
  f2.appendChild(f2safeBotTxt);

  // Метка секции
  const f2meta = txt('01 — ВОПРОС', 'IBM Plex Mono', 'Medium', 11, C.muted, { letterSpacing: 14, textCase: 'UPPER' });
  f2meta.x = 32; f2meta.y = 160;
  f2.appendChild(f2meta);

  // Вопрос
  const f2q = txt('Сколько времени вы тратите на создание контента в неделю?', 'Space Grotesk', 'Medium', 28, C.black, { width: 476, lineHeight: 130 });
  f2q.x = 32; f2q.y = 220;
  f2.appendChild(f2q);

  // Кнопки-варианты
  const f2btn1bg = rect(476, 56, C.black);
  f2btn1bg.x = 32; f2btn1bg.y = 640;
  f2.appendChild(f2btn1bg);
  const f2btn1txt = txt('1–3 часа', 'Space Grotesk', 'Medium', 15, C.bone);
  f2btn1txt.x = 32 + (476 - f2btn1txt.width) / 2;
  f2btn1txt.y = 657;
  f2.appendChild(f2btn1txt);

  const f2btn2bg = rect(476, 56, C.bone);
  f2btn2bg.strokes = [{ type: 'SOLID', color: C.black }];
  f2btn2bg.strokeWeight = 1;
  f2btn2bg.x = 32; f2btn2bg.y = 706;
  f2.appendChild(f2btn2bg);
  const f2btn2txt = txt('4+ часов', 'Space Grotesk', 'Regular', 15, C.black);
  f2btn2txt.x = 32 + (476 - f2btn2txt.width) / 2;
  f2btn2txt.y = 723;
  f2.appendChild(f2btn2txt);

  curX += f2.width + GAP;

  // ══════════════════════════════════════════════════════════════
  // 3. REELS 9:16 — заставка
  //    Реальный: 1080×1920px | Figma: 540×960px
  // ══════════════════════════════════════════════════════════════
  const f3 = figma.createFrame();
  f3.name = 'Reels 9:16 — Заставка';
  f3.resize(540, 960);
  f3.fills = solid(C.black);
  f3.x = curX;
  f3.y = 100;
  figma.currentPage.appendChild(f3);
  allFrames.push(f3);
  addLabel('Reels 9:16  |  1080×1920px  |  до 3 мин  |  ПРИОРИТЕТ ①', f3.x, f3.y);

  // Верхняя строка
  const f3top = txt('THNKFOR.ME / REELS', 'IBM Plex Mono', 'Medium', 10, C.muted, { letterSpacing: 14, textCase: 'UPPER' });
  f3top.x = 32; f3top.y = 36;
  f3.appendChild(f3top);

  // Play-иконка SVG (треугольник)
  const playSvg = '<svg width="56" height="56" viewBox="0 0 56 56"><polygon points="16,10 46,28 16,46" fill="#FF3B00"/></svg>';
  const playIcon = figma.createNodeFromSvg(playSvg);
  playIcon.x = 32; playIcon.y = 360;
  playIcon.resize(56, 56);
  f3.appendChild(playIcon);

  // Заголовок
  const f3h = txt('Как мы запустили контент-машину за 2 недели', 'Space Grotesk', 'Medium', 32, C.white, { width: 476, lineHeight: 125 });
  f3h.x = 32; f3h.y = 436;
  f3.appendChild(f3h);

  // Оранжевая линия под заголовком
  const f3line = rect(476, 2, C.orange);
  f3line.x = 32; f3line.y = 560;
  f3.appendChild(f3line);

  // Счётчик
  const f3dur = txt('0:47', 'IBM Plex Mono', 'Medium', 13, C.muted);
  f3dur.x = 32; f3dur.y = 880;
  f3.appendChild(f3dur);

  // Нижний логотип
  const f3logo = txt('THNKFOR.ME', 'IBM Plex Mono', 'Medium', 10, C.muted, { letterSpacing: 14, textCase: 'UPPER' });
  f3logo.x = 430; f3logo.y = 880;
  f3.appendChild(f3logo);

  curX += f3.width + GAP;

  // ══════════════════════════════════════════════════════════════
  // 4. КАРУСЕЛЬ — слайд 1 (обложка)
  //    Реальный: 1080×1350px | Figma: 540×675px
  // ══════════════════════════════════════════════════════════════
  const f4 = figma.createFrame();
  f4.name = 'Carousel Slide 1 — Обложка';
  f4.resize(540, 675);
  f4.fills = solid(C.black);
  f4.x = curX;
  f4.y = 100;
  figma.currentPage.appendChild(f4);
  allFrames.push(f4);
  addLabel('Карусель 4:5  |  до 20 слайдов  |  Portrait  |  ПРИОРИТЕТ ②', f4.x, f4.y);

  // Счётчик слайда
  const f4counter = txt('1 / 5', 'IBM Plex Mono', 'Regular', 10, C.muted, { letterSpacing: 8 });
  f4counter.x = 32; f4counter.y = 36;
  f4.appendChild(f4counter);

  // Заголовок
  const f4h = txt('5 систем которые заменили нам отдел маркетинга', 'Space Grotesk', 'Medium', 36, C.white, { width: 476, lineHeight: 120 });
  f4h.x = 32; f4h.y = 220;
  f4.appendChild(f4h);

  // Оранжевая линия-акцент
  const f4accent = rect(476, 2, C.orange);
  f4accent.x = 32; f4accent.y = 420;
  f4.appendChild(f4accent);

  // CTA "листай"
  const f4cta = txt('→ листай', 'IBM Plex Mono', 'Medium', 11, C.orange, { letterSpacing: 8 });
  f4cta.x = 32; f4cta.y = 628;
  f4.appendChild(f4cta);

  // Нижний правый: номер
  const f4num = txt('01', 'IBM Plex Mono', 'Medium', 32, C.muted, { letterSpacing: -2 });
  f4num.x = 474; f4num.y = 610;
  f4.appendChild(f4num);

  curX += f4.width + GAP;

  // ══════════════════════════════════════════════════════════════
  // 5. КАРУСЕЛЬ — стек (визуализация глубины)
  // ══════════════════════════════════════════════════════════════
  // Рисуем 3 фрейма со смещением (задние → передние)
  // Задний — слайд 3
  const f5back = figma.createFrame();
  f5back.name = 'Carousel Stack — Slide 3 (back)';
  f5back.resize(540, 675);
  f5back.fills = solid({ r: 0.10, g: 0.10, b: 0.10 });
  f5back.x = curX + 32;
  f5back.y = 84;
  figma.currentPage.appendChild(f5back);
  allFrames.push(f5back);

  const f5bt = txt('Система 3 — Аналитика', 'Space Grotesk', 'Regular', 18, C.muted, { width: 440 });
  f5bt.x = 32; f5bt.y = 300;
  f5back.appendChild(f5bt);
  const f5bc = txt('3 / 5', 'IBM Plex Mono', 'Regular', 10, C.muted, { letterSpacing: 8 });
  f5bc.x = 32; f5bc.y = 36;
  f5back.appendChild(f5bc);

  // Средний — слайд 2
  const f5mid = figma.createFrame();
  f5mid.name = 'Carousel Stack — Slide 2 (mid)';
  f5mid.resize(540, 675);
  f5mid.fills = solid({ r: 0.08, g: 0.08, b: 0.08 });
  f5mid.x = curX + 16;
  f5mid.y = 92;
  figma.currentPage.appendChild(f5mid);
  allFrames.push(f5mid);

  const f5mt = txt('Система 2 — Автопостинг', 'Space Grotesk', 'Regular', 18, C.muted, { width: 440 });
  f5mt.x = 32; f5mt.y = 300;
  f5mid.appendChild(f5mt);
  const f5mc = txt('2 / 5', 'IBM Plex Mono', 'Regular', 10, C.muted, { letterSpacing: 8 });
  f5mc.x = 32; f5mc.y = 36;
  f5mid.appendChild(f5mc);

  // Передний — слайд 1 (такой же как f4)
  const f5front = figma.createFrame();
  f5front.name = 'Carousel Stack — Slide 1 (front)';
  f5front.resize(540, 675);
  f5front.fills = solid(C.black);
  f5front.x = curX;
  f5front.y = 100;
  figma.currentPage.appendChild(f5front);
  allFrames.push(f5front);
  addLabel('Карусель — стек (визуализация глубины)', f5front.x, f5front.y);

  const f5counter = txt('1 / 5', 'IBM Plex Mono', 'Regular', 10, C.muted, { letterSpacing: 8 });
  f5counter.x = 32; f5counter.y = 36;
  f5front.appendChild(f5counter);

  const f5h = txt('5 систем которые заменили нам отдел маркетинга', 'Space Grotesk', 'Medium', 36, C.white, { width: 476, lineHeight: 120 });
  f5h.x = 32; f5h.y = 220;
  f5front.appendChild(f5h);

  const f5accent = rect(476, 2, C.orange);
  f5accent.x = 32; f5accent.y = 420;
  f5front.appendChild(f5accent);

  const f5cta = txt('→ листай', 'IBM Plex Mono', 'Medium', 11, C.orange, { letterSpacing: 8 });
  f5cta.x = 32; f5cta.y = 628;
  f5front.appendChild(f5cta);

  // Стрелка вправо — показывает свайп
  const arrowSvg = '<svg width="48" height="48" viewBox="0 0 48 48"><line x1="4" y1="24" x2="44" y2="24" stroke="#FF3B00" stroke-width="2"/><polyline points="32,12 44,24 32,36" fill="none" stroke="#FF3B00" stroke-width="2"/></svg>';
  const arrow = figma.createNodeFromSvg(arrowSvg);
  arrow.resize(48, 48);
  arrow.x = f5front.x + 540 + 16;
  arrow.y = f5front.y + 313;
  figma.currentPage.appendChild(arrow);

  // ══════════════════════════════════════════════════════════════
  // ФИНАЛ
  // ══════════════════════════════════════════════════════════════
  figma.viewport.scrollAndZoomIntoView(allFrames);
  figma.closePlugin('✅ THNKFOR.ME — 5 Instagram мокапов созданы');

})();
