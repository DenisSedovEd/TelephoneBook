import os
import json

command_list = {
    '1': 'Просмотреть весь список контактов',
    '2': 'Найти контакт',
    '3': 'Добавить новый контакт',
    '4': 'Изменить существующий',
    '5': 'Удалить существующий контакт',
    '6': 'Ничего, я передумал, пока:)'
}


def commands():
    print('Приветствую тебя в телефонном справочнике, что ты хотел сделать?')
    for key, value in command_list.items():
        print(f'{key} - {value}')
    print('Веди номер команды, которую ты хотел сделать:')


commands()


def open_file():
    with open('data_base.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def edit_file(data):
    with open('data_base.json', 'w', encoding='utf-8' ) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def view_all():
    data = open_file()
    for idx, contact in data.items():
        print(f'Контакт №{idx}')
        for key, value in contact.items():
            print(f'\t{key:<12} - {value}')
        print('_' * 50)


def search_contact():
    search_param = input('Введите имя или номер телефона: ')
    data = open_file()
    for idx, contact in data.items():
        if search_param == idx:
            return data[idx]
        for key, value in contact.items():
            if search_param == value:
                return data[idx]


def add_contact(data):
    name = input('Имя: ')
    phone_number = input('Номер телефона: ')
    comment = input('Комментарий: ')
    data[f'{len(data)+1}'] = {
        'Имя': name,
        'Телефон': phone_number,
        'Комментарий': comment
    }
    print(f'Добавить контакт {name}?')
    answer = input('y/n?')

    if answer.lower() == 'y':
        with open('data_base.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        return None


def change_contact():
    print('Изменяем')


def delete_contact():
    view_all()
    data = open_file()
    del_index = input('Введите ID контакта, который необходимо удалить: ')
    print(f'Удалить указанный контакт?')
    answer = input('y/n?')
    if answer.lower() == 'y':
        data.pop(del_index)
        edit_file(data)



def input_command():
    command = input()
    if command == '1':
        view_all()
    elif command == '2':
        data = search_contact()
        for key, value in data.items():
            print(f'\t{key:<12} - {value}')
    elif command == '3':
        data = open_file()
        add_contact(data)
    elif command == '4':
        change_contact()
    elif command == '5':
        delete_contact()
    elif command == '6':
        print('Как хочешь, пока')
    else:
        print('Такой команды нету...')


input_command()
