import os
import json

class Contact:

    def __init__(self, name, phone_number, comment):
        self.name = name
        self.phone_number = phone_number
        self.comment = comment

    def __str__(self):
        return str(f'Контакт {self.name}, его номер {self.phone_number}. Комментарий: {self.comment}')

    def add(self):
        pass

    def edit(self):
        pass

    def remove(self):
        pass

    def show(self):
        '''

        :return:
        '''
        pass


def show_contacts(data):
    '''
    Вывод в консоль всех существующих контактов.
    :param data:
    :return:
    '''
    for idx, contact in data.items():
        print(f'Контакт №{idx}')
        for key, value in contact.items():
            print(f'\t{key:<12} - {value}')
        print('_' * 50)


def open_file():
    '''
    Открытие json файла с данными.
    :return:
    '''
    with open('data_base.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def edit_file(data):
    '''
    Внесение изменений в json файл.
    :param data:
    :return:
    '''
    with open('data_base.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

class Storage:
    def __init__(self):
        pass



def view_all():
    '''
    Пункт меню №1. Вывод всех контактов.
    :return:
    '''
    data = open_file()
    show_contacts(data)


def search_contact():
    '''
    Пункт меню №2. Поиск контакта по ID, имени или номеру телефона.
    :return:
    '''
    search_param = input('Введите порядковый номер, имя или номер телефона: ')
    data = open_file()
    for idx, contact in data.items():
        if search_param == idx:
            for key, value in data[idx].items():
                print(f'\t{key:<12} - {value}')
            return None
        for key, value in contact.items():
            if search_param.lower() == value.lower():
                for keys, values in data[idx].items():
                    print(f'\t{keys:<12} - {values}')
                return None
    return 'Такого контакта не существует'


def add_contact():
    '''
    Пункт меню №3. Добавление нового контакта.
    :return:
    '''
    data = open_file()
    name = input('Имя: ')
    phone_number = input('Номер телефона: ')
    if not phone_number.isdigit():
        phone_number = input('Номер телефона не может содержать буквы или специальные символы. Введите еще раз.\n')
        if not phone_number.isdigit():
            print('Некорректно введен номер телефона.')
            return None
    comment = input('Комментарий: ')
    key = []
    for el in data:
        key.append(int(el))
    new_key = max(key) + 1
    data[new_key] = {
        'Имя': name,
        'Телефон': phone_number,
        'Комментарий': comment
    }
    print(f'Добавить контакт {name}?')
    answer = input('y/n?')

    if answer.lower() == 'y' or answer.lower() == 'н':
        edit_file(data)
    else:
        return None


def edit_contact():
    '''
    Пункт меню №4. Внесение изменений в существующий контакт.
    Выбор производится по ID.
    :return:
    '''
    data = open_file()
    show_contacts(data)
    edit_index = input('Введите ID контакта, который необходимо изменить: ')
    print('Заполните поле, которое необходимо изменить. В противном случае оставьте пустым.')
    name = input('Имя: ')
    if name == '':
        name = data[edit_index]['Имя']
    phone_number = input('Номер телефона: ')

    if phone_number == '':
        phone_number = data[edit_index]['Телефон']
    if not phone_number.isdigit():
        phone_number = input('Номер телефона не может содержать буквы или специальные символы. Введите еще раз.\n')
        if not phone_number.isdigit():
            print('Некорректно введен номер телефона.')
            return None
    comment = input('Комментарий: ')
    if comment == '':
        comment = data[edit_index]['Комментарий']
    print(f'Измеить контакт {data[edit_index]['Имя']}?')
    answer = input('y/n?')

    if answer.lower() == 'y' or answer.lower() == 'н':
        data[edit_index] = {
            'Имя': name,
            'Телефон': phone_number,
            'Комментарий': comment
        }
        edit_file(data)
    else:
        return None


def delete_contact():
    '''
    Пункт меню №5. Удаление контакта по ID.
    :return:
    '''
    data = open_file()
    show_contacts(data)
    del_index = input('Введите ID контакта, который необходимо удалить: ')
    print(f'Удалить указанный контакт?')
    answer = input('y/n?')
    if answer.lower() == 'y' or answer.lower() == 'н':
        data.pop(del_index)
        edit_file(data)


def input_command():
    '''
    Функция меню. Выводит доступные пользователю команды.
    :return:
    '''
    command_list = {
        '1': 'Просмотреть весь список контактов',
        '2': 'Найти контакт',
        '3': 'Добавить новый контакт',
        '4': 'Изменить существующий',
        '5': 'Удалить существующий контакт',
        '6': 'Ничего, я передумал, пока:)'
    }
    print('Приветствую тебя в телефонном справочнике, что ты хотел сделать?')
    print('_ ' * 30)
    for key, value in command_list.items():
        print(f'{key} - {value}')
    command = input('Веди номер команды, которую ты хотел сделать:\n')
    os.system('cls')
    if command == '1':
        view_all()
    elif command == '2':
        data = search_contact()
        if data:
            print(data)
    elif command == '3':
        add_contact()
    elif command == '4':
        edit_contact()
    elif command == '5':
        delete_contact()
    elif command == '6':
        print('Ну как хочешь, пока')
    else:
        print('Такой команды нету...')


input_command()
