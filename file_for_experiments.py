import os
# import test_module
assert 2 == 2, 'Равенство не соблюдено'

print('Путь к текущему файлу:', __file__)
print(os.path.dirname(__file__)) # получаем путь к папке, в которой находится скрипт
print(type(os.path.dirname(__file__)))
print(os.getcwd()) # получаем путь к текущей папке, в которой находимся
print(os.path.abspath(os.path.dirname(__file__)) ) # нормализуем путь

