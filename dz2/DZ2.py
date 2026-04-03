from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# 1. Приводим ФИО к правильному формату (lastname, firstname, surname)
for contact in contacts_list[1:]:  
    # объединяем первые три поля (Фамилия, Имя, Отчество) в одну строку
    full_name = " ".join(contact[:3]).split()
    
    # распределение по полям
    if len(full_name) == 3:
        contact[0], contact[1], contact[2] = full_name[0], full_name[1], full_name[2]
    elif len(full_name) == 2:
        contact[0], contact[1] = full_name[0], full_name[1]
        contact[2] = ''
    elif len(full_name) == 1:
        contact[0] = full_name[0]
        contact[1] = ''
        contact[2] = ''

# 2. Приводим телефоны в нужный формат
phone_pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*\(?доб\.?\s*(\d+)\)?)?'

for contact in contacts_list[1:]:
    phone = contact[5]
    if phone:
        match = re.search(phone_pattern, phone)
        if match:
            # основной номер
            formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
            # добавочный номер
            if match.group(7):
                formatted_phone += f" доб.{match.group(7)}"
            contact[5] = formatted_phone

# 3. Объединение дублирующихся записей
contacts_dict = {}
for contact in contacts_list[1:]:  
    key = (contact[0], contact[1])  # группируем по фамилии и имени
    if key not in contacts_dict:
        contacts_dict[key] = contact
    else:
        # объединяем данные
        existing = contacts_dict[key]
        for i in range(len(contact)):
            if contact[i] and not existing[i]:
                existing[i] = contact[i]

# Собираем итоговый список с заголовком
result_list = [contacts_list[0]] + list(contacts_dict.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)

print("\nОбработанная адресная книга:")
pprint(result_list)