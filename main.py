import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

new_contact_list = []
# TODO 1: выполните пункты 1-3 ДЗ
for row in contacts_list:
    fio = row[:3]
    old_data = row[3:]
    fio = ','.join(fio)
    fio_list = fio.replace(',', ' ')
    new_fio = ','.join(list(fio_list.split(' ')[:3]))
    new_row = new_fio.split(',') + old_data
    pattern = r"\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?"
    new_phone = re.sub(pattern, r"+7(\2) \3-\4-\5 \6.\7", new_row[5])
    new_row[5] = new_phone
    new_contact_list.append(new_row)
unique_rows = {}
for row in new_contact_list[1:]:
    key = (row[0], row[1])
    if key not in unique_rows:
        unique_rows[key] = row
    elif not unique_rows[key][-1] and row[-1]:
        unique_rows[key][-1] = row[-1]
unique_contact_list = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']] + list(unique_rows.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',',)
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(unique_contact_list)