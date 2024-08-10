import os
import time


# for i in os.walk('.'):
#     print(i)
# print(os.path.join(r'C:\Users\Айрат\PycharmProjects\Praktik\Homework\Module_7'))
# mtime = os.path.getmtime('.')
# import time
#
# print(time.ctime(mtime))
# print(os.path.getsize('.'))
# print(os.path.dirname(r'C:\Users\Айрат\PycharmProjects\Praktik\Homework\Module_7'))

directory = '.'
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = r'C:\Users\Айрат\PycharmProjects\Praktik\Homework\Module_7'
    filetime = os.path.getmtime('.')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize('.')
    parent_dir = os.path.dirname(r'C:\Users\Айрат\PycharmProjects\Praktik\Homework\Module_7')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
