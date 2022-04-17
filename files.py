"""
работа с файлами
"""

# простое считывание
# f = open('data')
# content = f.read()
# print(content)
# f.close()

# на запись
# f = open('data', 'w')
# print(content)
# f.close()

# # считывание по строчно
# f = open('data')
# for line in f:
#     print(line)
# f.close()

# #менеджер контекста файла
# with open('data') as f:
#     line = f.readline()
#     print(line)
#     # for line in f:
#     #     print(line)

# # запись файла
# with open('new_data', 'w') as f:
#     f.write('This is new file')

# data = ['1','2','3']
# # запись файла
# with open('new_data', 'w') as f:
#     f.writelines(data)

# #считываение побайтно
# with open('data') as f:
#     line = f.read(5)
#     print(line)
#     # for line in f:
#     #     print(line)
