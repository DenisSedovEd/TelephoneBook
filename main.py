import os
from shutil import which

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
    print('Веди номер команды, которую ты хотел сделать:\n')


commands()
def view_all():
    with open('data_base.json', 'r', encoding='utf-8') as file:
        data = file.readlines()
        res = []
        for line in data:
            res.append(line.strip().split(','))
        for row in res:
            contact = {
                'ID': row[0],
                'Имя': row[1],
                'Телефон': row[2],
                'Комментарий': row[3],
            }
        print(contact)

def search_contact():
    print('Ищем')


def add_contact():
    print('Добавляем')


def change_contact():
    print('Изменяем')


def delete_contact():
    print('Удаляем')


def input_command():
    command = input()
    if command == '1':
        view_all()
    elif command == '2':
        search_contact()
    elif command == '3':
        add_contact()
    elif command == '4':
        change_contact()
    elif command == '5':
        delete_contact()
    elif command == '6':
        print('Как хочешь, пока')
    else:
        print('Такой команды нету...')


input_command()


