#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = "/Users/anastasiiamosina/Library/CloudStorage/GoogleDrive-mossssina@gmail.com/My Drive/and36.studio/sitemap_cluster.xlsx"

# ═══════════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════════

PAGES = [
    ("/",                       "Pillar",      1, "Главная",    "Гости приходят через контент. Возвращаются — потому что бот не забывает.", "and36.studio — AI-маркетинг для HoReCa и beauty", "AI-агентство для кафе, ресторанов и салонов красоты. Контент без съёмок и автоматизация записи. Москва и СПб.", "✅ Готов",          "P0", "copy_homepage.md"),
    ("/services",               "Pillar",      1, "Хаб услуг",  "Два инструмента. Один результат.", "Услуги and36.studio — AI-контент и автоматизация", "AI-контент без фотосъёмок и автоматизация записи для кафе, ресторанов, салонов красоты. Выберите нужный блок услуг.", "✅ Готов",          "P0", "copy_services_hub.md"),
    ("/services/ai-content",    "Услуги",      2, "Услуга",     "AI-контент для кафе и салонов — без фотографа и SMM-щика", "AI-контент без съёмок — and36.studio", "Делаем контент для ресторанов и салонов красоты через нейросети. Без фотографа, без съёмок. 30 единиц в месяц, первый контент за 2–3 дня.", "✅ Готов",          "P0", "copy_ai_content.md"),
    ("/services/automation",    "Услуги",      2, "Услуга",     "Автоматизация записи и коммуникации — бот работает пока вы спите", "Автоматизация записи и ответов — and36.studio", "Telegram и WhatsApp-бот для записи, автоответы на отзывы, реактивация клиентов. Интеграция с YClients, DIKIDI, amoCRM. Москва и СПб.", "✅ Готов",          "P0", "copy_automation.md"),
    ("/solutions/restorany",    "HoReCa",      2, "Индустрия",  "AI-маркетинг для ресторанов и кафе", "AI-маркетинг для ресторанов — and36.studio", "Контент без съёмок, автоответы на Яндекс Картах, бот для резерва столов. Для кафе, ресторанов и баров Москвы и Петербурга.", "✅ Готов",          "P0", "copy_solutions_restorany.md"),
    ("/solutions/salony-krasoty","Beauty",      2, "Индустрия",  "AI-маркетинг для салонов красоты и барбершопов", "AI-маркетинг для салонов красоты — and36.studio", "Бот для записи через WhatsApp и Telegram, реактивация клиентов, AI-контент. Интеграция с DIKIDI и YClients. Для салонов Москвы и СПб.", "✅ Готов",          "P0", "copy_solutions_salony.md"),
    ("/solutions/stomatologii", "Медицина",    2, "Индустрия",  "AI-маркетинг для стоматологических клиник", "AI-маркетинг для стоматологий — and36.studio", "Доверительный AI-контент, бот для записи, автоматическая цепочка возврата пациентов. Интеграция с MedMe и YClients.", "✅ Готов",          "P0", "copy_solutions_stomatologii.md"),
    ("/solutions/fitnes",       "Спорт",       2, "Индустрия",  "AI-маркетинг для фитнес-студий и спортивных клубов", "AI-маркетинг для фитнес-студий — and36.studio", "AI-контент с расписанием и акциями, бот для пробной записи, напоминания об абонементах. Для фитнес-студий Москвы и СПб.", "✅ Готов",          "P1", "copy_solutions_p1_p2.md"),
    ("/solutions/kosmetologiya","Beauty",       2, "Индустрия",  "AI-маркетинг для косметологических клиник", "AI-маркетинг для косметологий — and36.studio", "Экспертный AI-контент и автоматическая курсовая цепочка для косметологических клиник. Реактивация и напоминания через бот.", "✅ Готов",          "P1", "copy_solutions_p1_p2.md"),
    ("/solutions/smm-agency",   "B2B",         2, "Индустрия",  "Контент-фабрика и автоматизация заявок для SMM-агентств", "Автоматизация для SMM-агентств — and36.studio", "Автоматизируем производство контента и приём заявок для маркетинговых агентств. Airtable → Make → Claude API. Масштабирование без найма.", "✅ Готов",          "P1", "copy_solutions_smm_agency.md"),
    ("/solutions/sport-shop",   "E-commerce",  2, "Индустрия",  "AI-автоматизация для интернет-магазинов спортивных товаров", "AI-автоматизация для спортмагазинов — and36.studio", "Генерация описаний товаров, бот для заказов, автоматизация брошенных корзин. Для интернет-магазинов спортивных товаров.", "✅ Готов",          "P1", "copy_solutions_sport_shop.md"),
    ("/solutions/detskie-centry","Образование", 2, "Индустрия", "AI-маркетинг для детских центров и секций", "AI-маркетинг для детских центров — and36.studio", "AI-контент для родителей, бот для записи на пробный урок, автоматический набор в группы. Для детских центров и секций.", "✅ Готов",          "P2", "copy_solutions_p1_p2.md"),
    ("/solutions/veterinary",   "Медицина",    2, "Индустрия",  "AI-маркетинг для ветеринарных клиник", "AI-маркетинг для ветклиник — and36.studio", "AI-контент о заботе о питомцах, прививочный календарь-бот, автоматические напоминания о визитах. Для ветеринарных клиник.", "✅ Готов",          "P2", "copy_solutions_p1_p2.md"),
    ("/solutions/psihologi",    "Услуги",      2, "Индустрия",  "AI-маркетинг для психологов и психотерапевтов", "AI-маркетинг для психологов — and36.studio", "Личный бренд психолога через AI-контент, бот для первого контакта, снижение барьера входа. Москва и СПб.", "✅ Готов",          "P2", "copy_solutions_p1_p2.md"),
    ("/audit",                  "Конверсия",   3, "Лид-магнит", "Бесплатный разбор вашего бизнеса — 30 минут", "Бесплатный разбор бизнеса — and36.studio", "Расскажите о задаче — разберём что работает, что нет, и что именно подойдёт. 30 минут, без давления.", "✅ Готов",          "P0", "copy_utility_pages.md"),
    ("/cases",                  "Доверие",     3, "Кейсы",      "Кейсы — что мы уже сделали", "Кейсы and36.studio — AI-маркетинг для HoReCa", "Реальные результаты: SMM-агентство, стоматология, спортмагазин. AI-контент и автоматизация в действии.", "⚠️ Заглушки",      "P0", "copy_utility_pages.md"),
    ("/pricing",                "Конверсия",   3, "Цены",       "Стоимость — прозрачные цены для вашей ниши", "Цены на AI-маркетинг — and36.studio", "Пакетные предложения для ресторанов, салонов красоты, фитнеса. Прозрачные цены, без скрытых платежей.", "⚠️ Нужно решение", "P1", "packages_by_industry.md"),
    ("/about",                  "Доверие",     3, "О нас",      "and36.studio — кто мы и как работаем", "О нас — and36.studio", "AI-агентство для HoReCa и beauty. Анастасия Мосина, основатель. Москва и Санкт-Петербург.", "🔲 Черновик",       "P1", "copy_utility_pages.md"),
]
# cols: url, cluster, level, type, h1, meta_title, meta_desc, status, priority, file

BLOCKS = [
    # url, num, name, content
    ("/", 1,  "Hero",                    "H1 · подзаголовок · CTA «Получить разбор» (→/audit) · CTA «Смотреть кейсы» (→/cases) · Social proof: 11+ проектов"),
    ("/", 2,  "Боли клиента",            "5 болей: нестабильные записи · медленный администратор · отзывы без ответа · нерегулярный контент · агентства не понимают специфику"),
    ("/", 3,  "Что мы делаем",           "Блок А (AI-контент) + Блок Б (автоматизация) — два столбца с кнопками →/services/ai-content и →/services/automation"),
    ("/", 4,  "Как работает AI-контент", "5 тезисов о работе без съёмок + пример-цитата о кофейне в Петербурге"),
    ("/", 5,  "Сценарии автоматизации",  "3 сценария: запись в 23:00 · ответ на негативный отзыв · реактивация спящего клиента"),
    ("/", 6,  "Три ниши",               "Рестораны · Салоны · Фитнес — боль + решение + ссылка на /solutions/[slug]"),
    ("/", 7,  "Процесс работы",          "4 шага: Разбор (бесплатно) → Стратегия (3–5 дней) → Запуск (1–2 недели) → Ведение"),
    ("/", 8,  "Кейсы",                   "3 заглушки: SMM-агентство · спортмагазин · стоматология + кнопка →/cases"),
    ("/", 9,  "Почему без съёмок — плюс","5 тезисов: скорость · стоимость · масштаб · гибкость · качество"),
    ("/", 10, "FAQ",                      "8 вопросов: AI-контент · бот · жалобы · интеграции · сроки · участие · малый бизнес · как начать"),
    ("/", 11, "Финальный CTA",            "Форма: имя + ниша (выпадающий) + контакт · альтернатива в Telegram · «Отвечаем в течение рабочего дня»"),

    ("/services", 1, "Hero",                  "H1 · краткое описание двух блоков · навигация по странице"),
    ("/services", 2, "Блок А — AI-контент",   "Краткое описание + 3–4 пункта + кнопка →/services/ai-content"),
    ("/services", 3, "Блок Б — Автоматизация","Краткое описание + 3–4 пункта + кнопка →/services/automation"),
    ("/services", 4, "Кому что подходит",     "Таблица: только контент / только автоматизация / оба — по признакам бизнеса"),
    ("/services", 5, "Перекрёстные ссылки",   "10 индустрий с якорями на /solutions/[slug]"),
    ("/services", 6, "CTA",                   "→/audit"),

    ("/services/ai-content", 1, "Hero",                  "H1 · дифференциатор (нет конкурентов в нише) · подзаголовок · CTA"),
    ("/services/ai-content", 2, "Боли",                  "4 боли: нет системы · нет ресурсов · дорогой продакшн · непоследовательность публикаций"),
    ("/services/ai-content", 3, "Что входит",             "7 пунктов: контент-стратегия · AI-визуалы · AI-тексты · Reels-сценарии · ведение TG/IG · таргет · аналитика"),
    ("/services/ai-content", 4, "Как создаётся AI-визуал","3 шага с иллюстрацией: промпт → генерация → адаптация под стиль бренда"),
    ("/services/ai-content", 5, "Сравнение",              "Таблица: традиционный SMM vs AI-контент (8 параметров: скорость · стоимость · объём · гибкость · зависимость · стабильность · масштаб · старт)"),
    ("/services/ai-content", 6, "Ниши",                   "Рестораны · Салоны · Фитнес — краткие примеры применения"),
    ("/services/ai-content", 7, "Сроки и объём",          "Таймлайн: день 1–3 (стратегия) · неделя 1 (первый контент) · месяц 1+ (ведение)"),
    ("/services/ai-content", 8, "FAQ",                    "5 вопросов: выглядит ли AI дёшево · отличие от стока · Reels · правки · авторские права"),
    ("/services/ai-content", 9, "CTA",                    "→/audit"),

    ("/services/automation", 1, "Hero",           "H1 · подзаголовок · CTA"),
    ("/services/automation", 2, "3 сценария",     "Запись в 23:00 · ответ на негативный отзыв (1 клик) · реактивация через 6 недель"),
    ("/services/automation", 3, "Что входит",     "5 пунктов: TG/WA-бот + CRM · единый хаб сообщений · автоответы на отзывы · напоминания · реактивация"),
    ("/services/automation", 4, "Интеграции",     "YClients · DIKIDI · amoCRM · Bitrix24 · WhatsApp Business API · Яндекс Карты · 2ГИС"),
    ("/services/automation", 5, "4 шага",         "Подключение → Настройка → Тест → Запуск"),
    ("/services/automation", 6, "Почему не SaaS", "3 причины: кастомизация под тон · интеграция с вашей CRM · не платите за ненужное"),
    ("/services/automation", 7, "FAQ",            "5 вопросов: как звучит бот · сложные ситуации · интеграции · сроки · изменение расписания"),
    ("/services/automation", 8, "CTA",            "→/audit"),

    ("/solutions/restorany", 1, "Hero",                  "H1 · подзаголовок (специфика HoReCa) · CTA"),
    ("/solutions/restorany", 2, "Боли ресторатора",      "5 болей: меню меняется еженедельно · сезонность · отзывы без ответа · нет времени · нет команды"),
    ("/solutions/restorany", 3, "AI-контент для HoReCa", "Алгоритм: блюдо дня · атмосфера зала · сезонные акции · Reels за 10 минут"),
    ("/solutions/restorany", 4, "Автоматизация",          "Резерв столов · автоответы на Яндекс Картах и 2ГИС · напоминания о брони"),
    ("/solutions/restorany", 5, "Технический стек",       "Таблица: задача → инструмент (Make · YClients · WhatsApp Business · Claude API)"),
    ("/solutions/restorany", 6, "Результаты",             "[Заглушки: охват · записи · рейтинг]"),
    ("/solutions/restorany", 7, "CTA",                    "→/audit"),

    ("/solutions/salony-krasoty", 1, "Hero",                     "H1 · подзаголовок · CTA"),
    ("/solutions/salony-krasoty", 2, "Боли",                     "5 болей: запись через телефон теряется · администратор не успевает · отзывы · фото · клиенты пропадают"),
    ("/solutions/salony-krasoty", 3, "Контент: мастер vs салон", "Два сценария: личный бренд мастера / контент для всего салона — разные стратегии"),
    ("/solutions/salony-krasoty", 4, "Автоматизация записи",     "DIKIDI или YClients + бот → запись без звонка"),
    ("/solutions/salony-krasoty", 5, "Реактивация",              "5–8 недельный цикл: клиент не записался → персональное сообщение"),
    ("/solutions/salony-krasoty", 6, "Специфика индустрии",      "Сезонность (лето / праздники) · тренды · срочные окна записи"),
    ("/solutions/salony-krasoty", 7, "CTA",                      "→/audit"),

    ("/solutions/stomatologii", 1, "Hero",                    "H1 · подзаголовок · CTA"),
    ("/solutions/stomatologii", 2, "Боли",                    "5 болей: доверие строится годами · сарафан · нет времени на контент · отзывы игнорируются · пациент пропал"),
    ("/solutions/stomatologii", 3, "Контент доверия",         "Образовательный формат · до/после (с разрешения) · врач как эксперт · развенчание мифов"),
    ("/solutions/stomatologii", 4, "Автоматизация возврата",  "6-месячная цепочка: первичный визит → 3 мес → 6 мес → год"),
    ("/solutions/stomatologii", 5, "Интеграции",              "MedMe · YClients · WhatsApp Business"),
    ("/solutions/stomatologii", 6, "Кейс",                    "[Заглушка — нужны реальные данные клиники]"),
    ("/solutions/stomatologii", 7, "CTA",                     "→/audit"),

    ("/solutions/fitnes", 1, "Hero",                     "H1 · подзаголовок · CTA"),
    ("/solutions/fitnes", 2, "Боли",                     "4 боли: подписываются но не записываются · отток после 2–3 месяцев · расписание меняется · абонемент висит"),
    ("/solutions/fitnes", 3, "AI-контент",               "Расписание · тренеры · акции на абонементы · трансформации клиентов · мотивационный контент"),
    ("/solutions/fitnes", 4, "Автоматизация удержания",  "Напоминания когда абонемент заканчивается · бот для пробной записи"),
    ("/solutions/fitnes", 5, "Реактивация",              "Спящие клиенты: 30 / 60 / 90 дней без визита → персональное предложение"),
    ("/solutions/fitnes", 6, "CTA",                      "→/audit"),

    ("/solutions/kosmetologiya", 1, "Hero",              "H1 · подзаголовок · CTA"),
    ("/solutions/kosmetologiya", 2, "Боли",              "4 боли: доверие к процедурам · сезонность · курсовые процедуры незакончены · нерегулярный возврат"),
    ("/solutions/kosmetologiya", 3, "Экспертный контент","Разбор процедур · показания/противопоказания · до/после · сезонные протоколы (фотозащита, пилинги)"),
    ("/solutions/kosmetologiya", 4, "Курсовая цепочка",  "Автоматические напоминания: процедура 1 → напоминание через X дней → процедура 2 → ..."),
    ("/solutions/kosmetologiya", 5, "Реактивация",       "Персональные предложения на основе истории визитов"),
    ("/solutions/kosmetologiya", 6, "CTA",               "→/audit"),

    ("/solutions/smm-agency", 1, "Hero",               "H1 · B2B-позиционирование (для агентств, не конечного бизнеса) · CTA"),
    ("/solutions/smm-agency", 2, "Проблема",           "Рост числа клиентов не масштабируется линейно с командой — узкое место: производство контента"),
    ("/solutions/smm-agency", 3, "Контент-фабрика",    "Архитектура: Airtable → Make → Claude API → Replicate → SMMplanner"),
    ("/solutions/smm-agency", 4, "Воронка заявок",     "Авто-квалификация лидов · распределение по менеджерам · автообновление CRM"),
    ("/solutions/smm-agency", 5, "Кейс СтудиоСаксесс","[Заглушка — нужны данные: кол-во клиентов до/после · экономия часов]"),
    ("/solutions/smm-agency", 6, "CTA",                "→/audit"),

    ("/solutions/sport-shop", 1, "Hero",               "H1 · e-commerce контекст · CTA"),
    ("/solutions/sport-shop", 2, "Боли e-commerce",    "Сотни карточек без описаний · брошенные корзины · статусы заказов вручную · нет ресурсов на поддержку"),
    ("/solutions/sport-shop", 3, "Генерация карточек", "Mass SKU: выгрузка каталога → Claude API → уникальные описания с характеристиками"),
    ("/solutions/sport-shop", 4, "Автоматизация заказов","Статус-бот: подтверждение → в пути → доставлен · без нагрузки на операторов"),
    ("/solutions/sport-shop", 5, "Брошенные корзины",  "Сценарий: добавил → не купил → напоминание через 1 ч → скидка через 24 ч"),
    ("/solutions/sport-shop", 6, "Кейс",               "[Заглушка — нужны данные: объём SKU · экономия времени]"),
    ("/solutions/sport-shop", 7, "CTA",                "→/audit"),

    ("/solutions/detskie-centry", 1, "Hero",                  "H1 · подзаголовок (аудитория — родители, не дети) · CTA"),
    ("/solutions/detskie-centry", 2, "Боли",                  "Нет доверия без рекомендации · набор в группы трудозатратный · запись через звонок · летний отток"),
    ("/solutions/detskie-centry", 3, "Контент для родителей", "Жизнь центра изнутри · результаты детей · педагоги как эксперты · ответы на частые вопросы"),
    ("/solutions/detskie-centry", 4, "Воронка пробного урока","Бот: запрос → выбор направления → запись → напоминание → фидбек после"),
    ("/solutions/detskie-centry", 5, "Набор в группы",        "Сезонная кампания (август–сентябрь): AI-контент + рассылка → бот записи"),
    ("/solutions/detskie-centry", 6, "CTA",                   "→/audit"),

    ("/solutions/veterinary", 1, "Hero",                    "H1 · подзаголовок · CTA"),
    ("/solutions/veterinary", 2, "Боли",                    "Нет системы возврата · клиенты забывают о плановых визитах · контент сложно делать интересным"),
    ("/solutions/veterinary", 3, "Контент для владельцев",  "Советы по уходу · сезонные угрозы (клещи, жара) · истории пациентов с разрешения"),
    ("/solutions/veterinary", 4, "Прививочный календарь",   "Killer feature: персональный бот по кличке и виду питомца — напоминание когда пора на прививку"),
    ("/solutions/veterinary", 5, "Автоматизация",           "Плановые осмотры · реактивация «потерянных» владельцев"),
    ("/solutions/veterinary", 6, "CTA",                     "→/audit"),

    ("/solutions/psihologi", 1, "Hero",                  "H1 · деликатный тон · CTA"),
    ("/solutions/psihologi", 2, "Боли",                  "Высокий барьер первого шага · неловко продавать себя · нет времени на контент · нет личного бренда"),
    ("/solutions/psihologi", 3, "Личный бренд",          "Экспертный контент без саморекламы: объяснение подходов · разрушение мифов · как выбрать специалиста"),
    ("/solutions/psihologi", 4, "Бот первого контакта",  "Анонимный первый вопрос → снижение тревоги → предложение первой сессии"),
    ("/solutions/psihologi", 5, "Деликатный подход",     "Что нельзя автоматизировать в терапии — честно о границах инструмента"),
    ("/solutions/psihologi", 6, "CTA",                   "→/audit"),

    ("/audit", 1, "Hero + форма",   "H1 · что будет на разборе · форма (имя + ниша + контакт)"),
    ("/audit", 2, "Что разбираем",  "Соцсети · боты · отзывы · конкуренты · рекомендации что именно подойдёт"),
    ("/audit", 3, "Формат",         "30–40 минут · Zoom или Telegram · без давления · без «спецпредложения только сегодня»"),
    ("/audit", 4, "После разбора",  "Получаете: понимание узких мест + рекомендации + стоимость"),
    ("/audit", 5, "Альтернативы",   "Написать в Telegram напрямую · ответим в течение рабочего дня"),

    ("/cases", 1, "Фильтр",    "По нише · по услуге (контент / автоматизация / оба)"),
    ("/cases", 2, "Кейс 1",    "СтудиоСаксесс — SMM-агентство: контент-фабрика + автоматизация заявок [нужны данные]"),
    ("/cases", 3, "Кейс 2",    "Спортмагазин — генерация карточек + бот статусов заказов [нужны данные]"),
    ("/cases", 4, "Кейс 3",    "Стоматология — AI-контент + 6-месячная цепочка возврата пациентов [нужны данные]"),
    ("/cases", 5, "CTA",       "→/audit"),

    ("/pricing", 1, "Hero",           "H1 · объяснение логики цен (setup + ежемесячное ведение)"),
    ("/pricing", 2, "Навигация",      "Табы или якоря по 10 нишам"),
    ("/pricing", 3, "Пакеты по нишам","30 пакетов (3 на нишу) с ценами «от» — см. packages_by_industry.md"),
    ("/pricing", 4, "FAQ по ценам",   "Что входит · рассрочка · минимальный срок · можно ли только один блок"),
    ("/pricing", 5, "CTA",            "→/audit (для точного расчёта под конкретный бизнес)"),

    ("/about", 1, "Манифест",          "Почему AI-маркетинг именно для малого бизнеса в HoReCa и beauty"),
    ("/about", 2, "Основатель",        "Фото · имя · опыт · почему именно эти ниши [нужны данные]"),
    ("/about", 3, "Принципы работы",   "3–4 принципа: прозрачность · специализация · минимальное участие клиента"),
    ("/about", 4, "Стек инструментов", "Claude API · Make/n8n · Replicate · YClients · DIKIDI · WhatsApp Business · Airtable"),
    ("/about", 5, "CTA",               "→/audit"),
]

QUESTIONS = [
    (1, "Публиковать цены открыто «от X₽» или только форма без цен?",                   "/pricing",    "Открытый"),
    (2, "Собрать данные кейса СтудиоСаксесс: метрики, детали, согласие клиента",         "/cases · /",  "Открытый"),
    (3, "Собрать данные кейса спортмагазина: объём SKU, экономия времени, согласие",     "/cases · /",  "Открытый"),
    (4, "Данные основателя для /about: биография, фото, связь с нишами",                 "/about",       "Открытый"),
    (5, "Верифицировать «11+ проектов» в social proof на главной — актуальна ли цифра?", "/",            "Открытый"),
]

LINKS = [
    ("/ (Главная)",              "→/services",                 "Блок «Что мы делаем»"),
    ("/ (Главная)",              "→/services/ai-content",      "Блок А"),
    ("/ (Главная)",              "→/services/automation",      "Блок Б"),
    ("/ (Главная)",              "→/solutions/restorany",      "Блок «Три ниши»"),
    ("/ (Главная)",              "→/solutions/salony-krasoty", "Блок «Три ниши»"),
    ("/ (Главная)",              "→/solutions/fitnes",         "Блок «Три ниши»"),
    ("/ (Главная)",              "→/audit",                    "CTA (основной)"),
    ("/ (Главная)",              "→/cases",                    "CTA (вторичный) + блок кейсов"),
    ("/services",                "→/services/ai-content",      "Блок А"),
    ("/services",                "→/services/automation",      "Блок Б"),
    ("/services",                "→/solutions/* (все 10)",     "Перекрёстные ссылки"),
    ("/services",                "→/audit",                    "CTA"),
    ("/services/ai-content",     "→/audit",                    "CTA"),
    ("/services/automation",     "→/audit",                    "CTA"),
    ("/solutions/restorany",     "→/audit",                    "CTA"),
    ("/solutions/salony-krasoty","→/audit",                    "CTA"),
    ("/solutions/stomatologii",  "→/audit",                    "CTA"),
    ("/solutions/fitnes",        "→/audit",                    "CTA"),
    ("/solutions/kosmetologiya", "→/audit",                    "CTA"),
    ("/solutions/smm-agency",    "→/audit",                    "CTA"),
    ("/solutions/sport-shop",    "→/audit",                    "CTA"),
    ("/solutions/detskie-centry","→/audit",                    "CTA"),
    ("/solutions/veterinary",    "→/audit",                    "CTA"),
    ("/solutions/psihologi",     "→/audit",                    "CTA"),
    ("/cases",                   "→/audit",                    "CTA"),
    ("/pricing",                 "→/audit",                    "CTA"),
    ("/about",                   "→/audit",                    "CTA"),
    ("Все страницы",             "→/pricing",                  "Футер"),
    ("Все страницы",             "→/about",                    "Футер"),
]

# ═══════════════════════════════════════════════════════════════
# STYLE HELPERS
# ═══════════════════════════════════════════════════════════════

HDR_BG    = "141414"
HDR_FG    = "FFFFFF"
ROW_EVEN  = "FFFFFF"
ROW_ODD   = "F7F7F7"
BORDER_C  = "DEDEDE"

P_CFG = {"P0": ("C62828","FFFFFF"), "P1": ("E65100","FFFFFF"), "P2": ("2E7D32","FFFFFF")}
S_CFG = {
    "✅": ("E8F5E9","1B5E20"),
    "⚠️": ("FFF8E1","BF360C"),
    "🔲": ("F5F5F5","616161"),
}
CLUSTER_CFG = {
    "Pillar":      ("212121","FFFFFF"),
    "Услуги":      ("283593","FFFFFF"),
    "HoReCa":      ("BF360C","FFFFFF"),
    "Beauty":      ("880E4F","FFFFFF"),
    "Медицина":    ("1565C0","FFFFFF"),
    "Спорт":       ("1B5E20","FFFFFF"),
    "B2B":         ("4A148C","FFFFFF"),
    "E-commerce":  ("E65100","FFFFFF"),
    "Образование": ("F57F17","212121"),
    "Конверсия":   ("B71C1C","FFFFFF"),
    "Доверие":     ("01579B","FFFFFF"),
}
LEVEL_CFG = {1: ("212121","FFFFFF"), 2: ("455A64","FFFFFF"), 3: ("78909C","FFFFFF")}

def _thin():
    s = Side(style="thin", color=BORDER_C)
    return Border(left=s, right=s, top=s, bottom=s)

def _fill(hex6):
    return PatternFill("solid", fgColor=hex6)

def _font(bold=False, color="1C1C1C", size=10):
    return Font(name="Arial", bold=bold, color=color, size=size)

def _align(h="left", v="center", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def apply(cell, bg=None, fg="1C1C1C", bold=False, h="left", v="center", size=10, wrap=True):
    cell.font   = Font(name="Arial", bold=bold, color=fg, size=size)
    cell.fill   = _fill(bg) if bg else _fill(ROW_EVEN)
    cell.alignment = Alignment(horizontal=h, vertical=v, wrap_text=wrap)
    cell.border = _thin()

def write_header(ws, cols, row=1):
    for ci, label in enumerate(cols, 1):
        c = ws.cell(row=row, column=ci, value=label)
        apply(c, bg=HDR_BG, fg=HDR_FG, bold=True, h="center", size=10)

def set_col_widths(ws, widths):
    for ci, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(ci)].width = w

def zebra_bg(row_idx):
    return ROW_EVEN if row_idx % 2 == 0 else ROW_ODD

def p_style(cell, p):
    bg, fg = P_CFG.get(p, ("AAAAAA","FFFFFF"))
    apply(cell, bg=bg, fg=fg, bold=True, h="center", v="center")

def s_style(cell, status):
    key = next((k for k in S_CFG if k in status), "🔲")
    bg, fg = S_CFG[key]
    apply(cell, bg=bg, fg=fg, h="center", v="center")

def cluster_style(cell, cluster):
    bg, fg = CLUSTER_CFG.get(cluster, ("AAAAAA","FFFFFF"))
    apply(cell, bg=bg, fg=fg, bold=True, h="center", size=9)

def level_style(cell, level):
    bg, fg = LEVEL_CFG.get(level, ("AAAAAA","FFFFFF"))
    apply(cell, bg=bg, fg=fg, bold=True, h="center")

def len_style(cell, val, limit):
    n = len(val)
    cell.value = n
    bg = "E8F5E9" if n <= limit else "FFEBEE"
    fg = "1B5E20" if n <= limit else "B71C1C"
    apply(cell, bg=bg, fg=fg, h="center")

# ═══════════════════════════════════════════════════════════════
# BUILD WORKBOOK
# ═══════════════════════════════════════════════════════════════

wb = Workbook()

# ─────────────────────────────────────────
# SHEET 1 — ИНДЕКС
# ─────────────────────────────────────────
ws1 = wb.active
ws1.title = "📋 Индекс"

HDR1 = ["URL", "Кластер", "Ур.", "Тип страницы", "Статус", "P", "Файл контента"]
write_header(ws1, HDR1)
ws1.freeze_panes = "A2"
ws1.auto_filter.ref = f"A1:G{len(PAGES)+1}"
set_col_widths(ws1, [34, 14, 6, 14, 22, 6, 32])
ws1.row_dimensions[1].height = 20

# Add a title row above header
ws1.insert_rows(1)
title_cell = ws1["A1"]
title_cell.value = "and36.studio — Карта сайта и кластеризация"
title_cell.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
title_cell.fill = _fill("141414")
title_cell.alignment = Alignment(horizontal="left", vertical="center")
ws1.merge_cells("A1:G1")
ws1.row_dimensions[1].height = 28
ws1.freeze_panes = "A3"
ws1.auto_filter.ref = f"A2:G{len(PAGES)+2}"

for ri, row in enumerate(PAGES, 3):
    url, cluster, level, ptype, h1, mt, md, status, priority, cfile = row
    bg = zebra_bg(ri)

    c_url = ws1.cell(ri, 1, url)
    apply(c_url, bg=bg, bold=True, fg="141414")

    c_cl = ws1.cell(ri, 2, cluster)
    cluster_style(c_cl, cluster)

    c_lv = ws1.cell(ri, 3, level)
    level_style(c_lv, level)

    c_tp = ws1.cell(ri, 4, ptype)
    apply(c_tp, bg=bg, h="center")

    c_st = ws1.cell(ri, 5, status)
    s_style(c_st, status)

    c_pr = ws1.cell(ri, 6, priority)
    p_style(c_pr, priority)

    c_fl = ws1.cell(ri, 7, cfile)
    apply(c_fl, bg=bg, fg="455A64", size=9)

ws1.row_dimensions[2].height = 18

# ─────────────────────────────────────────
# SHEET 2 — SEO
# ─────────────────────────────────────────
ws2 = wb.create_sheet("🎯 SEO")
ws2.insert_rows(1)
t2 = ws2["A1"]
t2.value = "SEO — заголовки и мета-описания"
t2.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
t2.fill = _fill("141414")
t2.alignment = Alignment(horizontal="left", vertical="center")
ws2.merge_cells("A1:I1")
ws2.row_dimensions[1].height = 28

HDR2 = ["URL", "P", "H1", "H1 зн.", "Meta Title (≤60)", "MT зн.", "Meta Description (≤160)", "MD зн.", "Статус"]
write_header(ws2, HDR2, row=2)
ws2.freeze_panes = "A3"
ws2.auto_filter.ref = f"A2:I{len(PAGES)+2}"
set_col_widths(ws2, [30, 6, 52, 8, 40, 8, 58, 8, 20])
ws2.row_dimensions[2].height = 18

for ri, row in enumerate(PAGES, 3):
    url, cluster, level, ptype, h1, mt, md, status, priority, cfile = row
    bg = zebra_bg(ri)

    c_url = ws2.cell(ri, 1, url)
    apply(c_url, bg=bg, bold=True, fg="141414")

    c_pr = ws2.cell(ri, 2, priority)
    p_style(c_pr, priority)

    c_h1 = ws2.cell(ri, 3, h1)
    apply(c_h1, bg=bg)

    c_h1l = ws2.cell(ri, 4)
    len_style(c_h1l, h1, 999)  # H1 no hard limit, just show
    c_h1l.fill = _fill(bg)
    c_h1l.font = Font(name="Arial", color="455A64", size=9)
    c_h1l.alignment = Alignment(horizontal="center", vertical="center")

    c_mt = ws2.cell(ri, 5, mt)
    apply(c_mt, bg=bg)

    c_mtl = ws2.cell(ri, 6)
    len_style(c_mtl, mt, 60)

    c_md = ws2.cell(ri, 7, md)
    apply(c_md, bg=bg)

    c_mdl = ws2.cell(ri, 8)
    len_style(c_mdl, md, 160)

    c_st = ws2.cell(ri, 9, status)
    s_style(c_st, status)

    ws2.row_dimensions[ri].height = 42

# Legend note
note_row = len(PAGES) + 4
nc = ws2.cell(note_row, 5, "Зелёный = в пределах лимита   Красный = превышен лимит")
nc.font = Font(name="Arial", italic=True, color="888888", size=9)

# ─────────────────────────────────────────
# SHEET 3 — БЛОКИ
# ─────────────────────────────────────────
ws3 = wb.create_sheet("🗂 Блоки")
ws3.insert_rows(1)
t3 = ws3["A1"]
t3.value = "Структура блоков — все страницы"
t3.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
t3.fill = _fill("141414")
t3.alignment = Alignment(horizontal="left", vertical="center")
ws3.merge_cells("A1:F1")
ws3.row_dimensions[1].height = 28

HDR3 = ["URL", "Кластер", "№", "Название блока", "Содержание блока", "Статус страницы"]
write_header(ws3, HDR3, row=2)
ws3.freeze_panes = "A3"
ws3.auto_filter.ref = f"A2:F{len(BLOCKS)+2}"
set_col_widths(ws3, [30, 14, 5, 24, 72, 20])
ws3.row_dimensions[2].height = 18

# Build lookup maps
cluster_map  = {p[0]: p[1] for p in PAGES}
status_map   = {p[0]: p[7] for p in PAGES}
priority_map = {p[0]: p[8] for p in PAGES}

for ri, blk in enumerate(BLOCKS, 3):
    url, num, name, content = blk
    cluster = cluster_map.get(url, "—")
    status  = status_map.get(url, "—")
    bg = zebra_bg(ri)

    c_url = ws3.cell(ri, 1, url)
    apply(c_url, bg=bg, bold=True, fg="141414", size=9)

    c_cl = ws3.cell(ri, 2, cluster)
    cluster_style(c_cl, cluster)

    c_num = ws3.cell(ri, 3, num)
    apply(c_num, bg="F0F4FF", fg="283593", bold=True, h="center")

    c_nm = ws3.cell(ri, 4, name)
    apply(c_nm, bg=bg, bold=True, fg="212121")

    c_ct = ws3.cell(ri, 5, content)
    apply(c_ct, bg=bg, fg="455A64", size=9)

    c_st = ws3.cell(ri, 6, status)
    s_style(c_st, status)

    ws3.row_dimensions[ri].height = 28

# ─────────────────────────────────────────
# SHEET 4 — ПЕРЕЛИНКОВКА
# ─────────────────────────────────────────
ws4 = wb.create_sheet("🔗 Перелинковка")
ws4.insert_rows(1)
t4 = ws4["A1"]
t4.value = "Внутренняя перелинковка"
t4.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
t4.fill = _fill("141414")
t4.alignment = Alignment(horizontal="left", vertical="center")
ws4.merge_cells("A1:C1")
ws4.row_dimensions[1].height = 28

HDR4 = ["Источник", "Назначение", "Где / контекст"]
write_header(ws4, HDR4, row=2)
ws4.freeze_panes = "A3"
set_col_widths(ws4, [32, 32, 36])

for ri, lnk in enumerate(LINKS, 3):
    src, dst, ctx = lnk
    bg = zebra_bg(ri)
    c1 = ws4.cell(ri, 1, src); apply(c1, bg=bg, bold=True, fg="141414")
    c2 = ws4.cell(ri, 2, dst); apply(c2, bg=bg, fg="1565C0", bold=True)
    c3 = ws4.cell(ri, 3, ctx); apply(c3, bg=bg, fg="455A64", size=9)

# ─────────────────────────────────────────
# SHEET 5 — ОТКРЫТЫЕ ВОПРОСЫ
# ─────────────────────────────────────────
ws5 = wb.create_sheet("❓ Вопросы")
ws5.insert_rows(1)
t5 = ws5["A1"]
t5.value = "Открытые вопросы — нужно решение"
t5.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
t5.fill = _fill("141414")
t5.alignment = Alignment(horizontal="left", vertical="center")
ws5.merge_cells("A1:D1")
ws5.row_dimensions[1].height = 28

HDR5 = ["№", "Вопрос", "Влияет на страницы", "Статус"]
write_header(ws5, HDR5, row=2)
ws5.freeze_panes = "A3"
set_col_widths(ws5, [5, 60, 28, 14])

for ri, q in enumerate(QUESTIONS, 3):
    num, question, affects, status = q
    bg = "FFFDE7"

    c1 = ws5.cell(ri, 1, num);      apply(c1, bg=bg, fg="BF360C", bold=True, h="center")
    c2 = ws5.cell(ri, 2, question); apply(c2, bg=bg, fg="212121")
    c3 = ws5.cell(ri, 3, affects);  apply(c3, bg=bg, fg="455A64", size=9)
    c4 = ws5.cell(ri, 4, status);   apply(c4, bg="FFCCBC", fg="BF360C", bold=True, h="center")
    ws5.row_dimensions[ri].height = 30

# ─────────────────────────────────────────
# REORDER SHEETS
# ─────────────────────────────────────────
wb._sheets = [ws1, ws2, ws3, ws4, ws5]

wb.save(OUT)
print(f"✅ Saved: {OUT}")
