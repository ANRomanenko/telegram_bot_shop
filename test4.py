# import csv
#
# name_1 = 'Anna'
# name_2 = 'Victor'
# Variant = ['Svetka', 'Ira', 'Vika']

# with open('data.csv', 'w') as file: # Открываем файл на запись
#      writer = csv.writer(file)
#      writer.writerow(
#           #Variant
#           ('user_name', 'user_address')
#      )

# users_data = [
#      ('user_name', 'user_address'),
#      ["user1", "address1"],
#      ["user2", "address2"],
#      ["user3", "address3"],
# ]

# with open('data.csv', 'w', encoding='cp1251', newline='') as file:
#      writer = csv.writer(file, delimiter=';')
#      writer.writerows(
#           users_data
#      )

# for user in users_data:
#      with open('data.csv', 'a') as file: # используем флаг "a" тоесть append()
#           writer = csv.writer(file)
#           writer.writerow(
#                user
#           )


poem = '''\
Программировать весело.
Если работа скуча,
Чтобы придать ей веселый тон -
    используй Python!
'''

with open('poem.txt', 'w') as file:
    print(file)


# f = open('poem.txt', 'w') # открываем для записи (writing)
# f.write(poem) # Записываем текст в файл
# f.close() # закрываем файл
#
# f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
#                     # режим чтения ('r' eading)
#
# while True:
#     line = f.readline()
#     if len(line) == 0: # Нулевая длинна обозночает конец файла (EOF)
#         break
#     print(line, end='')
#
# f.close() # закрываем файл

