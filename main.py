from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
import re

# numder_tel = r"(\+7|8)?\s*\(\d+\)\s*\d+[\s-]\d+[\s-]\d+"
# pprint(contacts_list)
name_list = []
# dict_otdel = {}
# parametr = contacts_list[0]
contacts_list.pop(0)
# pprint(parametr)
for name in contacts_list:

    #сделал правильный формат имени

    name_lname = ' '.join(name[0:3])
    name_lname_pattern = r"([А-Яёа-я]+)\s([А-Яёа-я]+)\s([А-Яёа-я]*)(\s*)"
    new_name = r"\1, \2, \3"
    res_name = re.sub(name_lname_pattern, new_name, name_lname)
    name.pop(0)
    name.pop(1)
    name.pop(2)

    #сделал прафильный формат доб. номера

    number_sec_pattern = r"[\s(]*(\D+)\.\s(\d+)[\s)]*"
    new_number_sec = r" \1.\2"
    res_num_sec = re.sub(number_sec_pattern, new_number_sec, name[2])
    name[2] = res_num_sec

    #сделал прафильный формат номера

    number_pattern = r"(\+7|8)\s*[\s(]*(\d+)[\s)]*[\s-]*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
    new_number = r"+7(\2)\3-\4-\5"
    res_number = re.sub(number_pattern, new_number, name[2])
    name[2] = res_number
    name_list.append(res_name.split(', ') + name)

pprint(name_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#
#     ## Вместо contacts_list подставьте свой список:
#     datawriter.writerows(contacts_list)