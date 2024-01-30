import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
for row in contacts_list:
    fio = row[:3]
    old_data = row[3:]
    fio = ','.join(fio)
    fio_list = fio.replace(',',' ')
    new_fio = ','.join(list(fio_list.split(' ')[:3]))
    new_row = new_fio.split(',')+ old_data
    find_phone = re.findall('[0-9]', new_row[5])
    if len(find_phone) > 11:
        normalized_phone = ''.join(find_phone[:11])
        add_phone = ''.join(find_phone[11:])
        new_phone = normalized_phone[-10:]
        new_row[5] = f'+7({new_phone[:3]}){new_phone[3:6]}-{new_phone[6:8]}-{new_phone[8:10]} доб.{add_phone}'
    elif len(find_phone) <= 11 and len(find_phone) >= 6:
        normalized_phone = ''.join(find_phone[:11])
        new_phone = normalized_phone[-10:]
        new_row[5] = f'+7({new_phone[:3]}){new_phone[3:6]}-{new_phone[6:8]}-{new_phone[8:10]}'
    elif new_row[5] == 'phone':
        new_row[5] = 'phone'
    else:
        new_row[5] = ''







# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)