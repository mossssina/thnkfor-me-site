import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from copy import copy

FILE = "niches_analysis.xlsx"

INTEGRATIONS = {
    "Рестораны":                    "iiko / r_keeper, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Салоны красоты":               "YClients, DIKIDI, amoCRM, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Барбершопы":                   "YClients, DIKIDI, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Ногтевые студии":              "YClients, DIKIDI, Яндекс Карты, WA/TG-бот",
    "Косметологические клиники":    "YClients, MedMe, amoCRM, Prodoctorov, Яндекс Карты, WA/TG-бот",
    "SPA-салоны":                   "YClients, DIKIDI, amoCRM, Яндекс Карты, WA/TG-бот",
    "Стоматологические клиники":    "InfoDoc / 1С-Медицина, amoCRM, Prodoctorov, Яндекс Карты, WA/TG-бот",
    "Фитнес-клубы":                 "1С-Фитнес / FitBase, amoCRM, Яндекс Карты, WA/TG-бот",
    "Йога-студии":                  "YClients, amoCRM, Яндекс Карты, WA/TG-бот",
    "Пилатес-студии":               "YClients, amoCRM, Яндекс Карты, WA/TG-бот",
    "Кафе":                         "iiko / r_keeper, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Бары и пабы":                  "iiko / r_keeper, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Студии лазерной эпиляции":     "YClients, DIKIDI, Яндекс Карты, WA/TG-бот",
    "Перманентный макияж":          "YClients, DIKIDI, WA/TG-бот",
    "Бровисты / лешмейкеры":       "YClients, DIKIDI, WA/TG-бот",
    "Массажные студии":             "YClients, DIKIDI, Яндекс Карты, WA/TG-бот",
    "Частные клиники (много.)":     "MedMe / 1С-Медицина / Medesk, amoCRM, Prodoctorov, WA/TG-бот",
    "Кроссфит-боксы":               "YClients / FitBase, amoCRM, WA/TG-бот",
    "Детские центры развития":      "amoCRM / Битрикс24, WA/TG-бот",
    "Ветеринарные клиники":         "VetManager, amoCRM, Яндекс Карты, WA/TG-бот",
    "SMM-агентства":                "amoCRM / Битрикс24, TG-бот",
    "Отели (бутик, 3–4*)":         "amoCRM / Битрикс24, Яндекс Путешествия, WA/TG-бот",
    "Доставка еды (свой бренд)":   "iiko, Яндекс Еда, Delivery Club, WA/TG-бот",
    "Веганские и здоровые кафе":    "iiko / r_keeper, Яндекс Карты, 2ГИС, WA/TG-бот",
    "Санатории и курорты":          "amoCRM / Битрикс24, Яндекс Путешествия, WA/TG-бот",
    "Глэмпинг":                     "amoCRM, Airbnb API, WA/TG-бот",
    "Дерматологические клиники":    "MedMe / 1С-Медицина, amoCRM, Prodoctorov, WA/TG-бот",
    "Пластическая хирургия":        "amoCRM / Битрикс24, Prodoctorov, WA/TG-бот",
    "Студии растяжки":              "YClients, amoCRM, WA/TG-бот",
    "Танцевальные студии":          "YClients, amoCRM, WA/TG-бот",
    "Груминг-салоны":               "YClients / DIKIDI, Яндекс Карты, WA/TG-бот",
    "Детейлинг-студии":             "amoCRM, Яндекс Карты, WA/TG-бот",
    "Флористы":                     "amoCRM, WA/TG-бот",
    "Квесты":                       "amoCRM, Яндекс Карты, WA/TG-бот",
    "Кофейни":                      "Яндекс Карты, 2ГИС, WA/TG-бот",
    "Пекарни и кондитерские":       "Яндекс Карты, 2ГИС, WA/TG-бот",
    "Загородные базы отдыха":       "amoCRM, Airbnb API, WA/TG-бот",
    "Татуировки и пирсинг":         "YClients, Яндекс Карты, WA/TG-бот",
    "Реабилитационные центры":      "1С-Медицина / Medesk, amoCRM, Prodoctorov, WA/TG-бот",
    "Офтальмологические клиники":   "MedMe / 1С-Медицина, amoCRM, Prodoctorov, WA/TG-бот",
    "Гинекологические клиники":     "MedMe / 1С-Медицина, amoCRM, Prodoctorov, WA/TG-бот",
    "Психологи (частные)":          "amoCRM, TG-бот",
    "Психотерапевты":               "amoCRM, TG-бот",
    "Коучи":                        "GetCourse / amoCRM, TG-бот",
    "Нутрициологи":                 "GetCourse / amoCRM, TG-бот",
    "Единоборства (бокс, MMA)":    "YClients / FitBase, amoCRM, WA/TG-бот",
    "Батутные центры":              "YClients, amoCRM, Яндекс Карты, WA/TG-бот",
    "Скалодромы":                   "YClients, amoCRM, WA/TG-бот",
    "Конные клубы":                 "amoCRM, WA/TG-бот",
    "Теннисные клубы":              "YClients / amoCRM, WA/TG-бот",
    "Языковые школы":               "amoCRM / Битрикс24, GetCourse, WA/TG-бот",
    "Музыкальные школы":            "amoCRM, WA/TG-бот",
    "Художественные школы":         "amoCRM, WA/TG-бот",
    "Робототехника / STEM":         "amoCRM / GetCourse, WA/TG-бот",
    "Частные детские сады":         "amoCRM / Битрикс24, WA/TG-бот",
    "Онлайн-курсы / EdTech":        "GetCourse / Антитренинги, amoCRM, TG-бот",
    "Частные школы":                "amoCRM / Битрикс24, WA/TG-бот",
    "Зоогостиницы (передержка)":    "amoCRM, Яндекс Карты, WA/TG-бот",
    "Автосервисы":                  "amoCRM / 1С, Яндекс Карты, WA/TG-бот",
    "Аренда автомобилей":           "amoCRM / Битрикс24, WA/TG-бот",
    "Автосалоны (независимые)":     "amoCRM / Битрикс24, WA/TG-бот",
    "Клининговые компании":         "amoCRM / Битрикс24, WA/TG-бот",
    "Дизайнеры интерьера":          "amoCRM / Битрикс24, WA/TG-бот",
    "Коворкинги":                   "amoCRM / Битрикс24, WA/TG-бот",
    "Застройщики (малые)":          "amoCRM / Битрикс24, WA/TG-бот",
    "Маркетинговые агентства":      "amoCRM / Битрикс24, TG-бот",
    "Онлайн-школы (B2B-контент)":  "GetCourse, amoCRM, TG-бот",
    "Кондитеры (торты на заказ)":  "amoCRM, WA/TG-бот",
    "Организаторы свадеб":          "amoCRM / Битрикс24, WA/TG-бот",
    "Инт. магазины (спортивные)":   "1С / МойСклад, amoCRM, WA/TG-бот",
    "Инт. магазины (мода/одежда)":  "1С / МойСклад, amoCRM, WA/TG-бот",
    "Инт. магазины (косметика)":    "1С / МойСклад, amoCRM, WA/TG-бот",
    "Зоомагазины":                  "1С / МойСклад, amoCRM, WA/TG-бот",
    "Ландшафтные дизайнеры":        "amoCRM, WA/TG-бот",
    "Кейтеринг":                    "amoCRM / Битрикс24, WA/TG-бот",
    "Посуточная аренда (AirBnB)":  "Airbnb API / amoCRM, WA/TG-бот",
    "Бассейны (частные)":           "YClients / FitBase, amoCRM, WA/TG-бот",
    "Шинные центры":                "amoCRM, Яндекс Карты, WA/TG-бот",
    "Агентства недвижимости":       "amoCRM / Битрикс24, WA/TG-бот",
    "Юридические фирмы":            "amoCRM / Битрикс24, WA/TG-бот",
    "Фотографы (коммерческие)":     "amoCRM, WA/TG-бот",
    "Event-агентства":              "amoCRM / Битрикс24, WA/TG-бот",
    "Частные музеи и галереи":      "amoCRM, Яндекс Карты, WA/TG-бот",
    "Инт. магазины (детские тов.)": "1С / МойСклад, amoCRM, WA/TG-бот",
    "Зоотовары онлайн":             "1С / МойСклад, amoCRM, WA/TG-бот",
    "Туристические агентства":      "amoCRM / Битрикс24, WA/TG-бот",
    "Фуд-траки":                    "Яндекс Карты, 2ГИС, WA/TG-бот",
    "Тёмные кухни (dark kitchen)":  "iiko, Яндекс Еда, Delivery Club, WA/TG-бот",
    "Хостелы":                      "amoCRM, Airbnb API, WA/TG-бот",
    "Студии загара":                "YClients / DIKIDI, Яндекс Карты, WA/TG-бот",
    "Медицинские лаборатории":      "MedMe / 1С-Медицина, amoCRM, WA/TG-бот",
    "Автомойки":                    "amoCRM, Яндекс Карты, WA/TG-бот",
    "Ремонт квартир (бригады)":     "amoCRM / Битрикс24, WA/TG-бот",
    "Частные риелторы":             "amoCRM, WA/TG-бот",
    "Бухгалтерские бюро":           "amoCRM / Битрикс24, TG-бот",
    "IT-компании / разработка":     "amoCRM / Битрикс24, TG-бот",
    "Рекрутинговые агентства":      "amoCRM / Битрикс24, TG-бот",
    "Прокат снаряжения":            "amoCRM, WA/TG-бот",
    "Астрологи / таро":             "amoCRM, TG-бот",
    "Шахматные клубы":              "amoCRM, WA/TG-бот",
    "Репетиторы (частные)":         "amoCRM, TG-бот",
    "Установка окон и дверей":      "amoCRM / Битрикс24, WA/TG-бот",
    "Натяжные потолки":             "amoCRM / Битрикс24, WA/TG-бот",
    "Частные гиды":                 "amoCRM, WA/TG-бот",
}

wb = openpyxl.load_workbook(FILE)
ws = wb.active

# Find header row (row 2) and add new column
new_col = ws.max_column + 1

# Copy style from last header cell
header_cell = ws.cell(row=2, column=ws.max_column)
new_header = ws.cell(row=2, column=new_col, value="Интеграции\n(сервисы)")
if header_cell.font:
    new_header.font = copy(header_cell.font)
if header_cell.fill:
    new_header.fill = copy(header_cell.fill)
if header_cell.alignment:
    new_header.alignment = copy(header_cell.alignment)

# Fill integrations for each niche row
for row in ws.iter_rows(min_row=3, max_row=ws.max_row):
    niche = row[0].value
    if niche and niche in INTEGRATIONS:
        cell = ws.cell(row=row[0].row, column=new_col, value=INTEGRATIONS[niche])
        cell.alignment = Alignment(wrap_text=True, vertical="top")

# Set column width
ws.column_dimensions[openpyxl.utils.get_column_letter(new_col)].width = 45

wb.save(FILE)
print(f"✓ Столбец 'Интеграции' добавлен в {FILE}")
print(f"  Заполнено ниш: {len(INTEGRATIONS)}")
