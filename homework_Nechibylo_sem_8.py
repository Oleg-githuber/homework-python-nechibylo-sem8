'''
В программе можно выбрать один из трёх режимов:
r - чтение из файла phone.csv;
w- запись нового контакта в файл phone.csv
c - копирование контакта из файла phone.csv в файл new_phone.csv
'''


from csv import DictReader, DictWriter
from os.path import exists


file_name = 'phone.csv'
new_file_name = 'new_phone.csv'

# Функция добавления данных в новый контакт телефонной книги
def get_info():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')

    return [first_name, last_name, phone_number]

# Создание файла
def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()

# Функция чтения данных из файла. Возвращает список словарей
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

# Функция записи в файл. Считывает файл и добавляет один словарь в список словарей
def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'имя': lst[0], 'фамилия': lst[1], 'телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)

#  Функция записи в новый файл
def write_new_file(new_file_name, lst):
    res = read_file(new_file_name)
    res.append(lst)
    with open(new_file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_w.writeheader()
        f_w.writerows(res)


# Функция копирования телефонного контакта по номеру строки
def copy_row(file_name=file_name, new_file_name=new_file_name):
    #number = int(input("Введите номер строки: "))
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)      # Чтение списка словарей из файла
        lst_1 = []                  # Создание пустого списка
        for row in f_r:             # Запись в пустой список списка словарей из файла
            lst_1.append(row)
        flag = False
        while not flag:
            try:
                number = int(input("Введите номер строки: "))   # Ввод номера контакта
                if number > len(lst_1):         # Проверка номера контакта на превышение размера списка
                    print(f"Вводимое число не должно превышать количество строк ({len(lst_1)})!")
                else:
                    flag = True
            except ValueError:
                print('Невалидный номер')           # Проверка на ввод невалидных символов
        if not exists(new_file_name):
            create_file(new_file_name)          # создание нового файла
        write_new_file(new_file_name, lst_1[number - 1])    # Запись выбранного контакта в файл

# Главная функция
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его.')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_row(file_name)

main()