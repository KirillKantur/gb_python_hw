def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: list[str], info: str) -> list[str] or str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return 'совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('----------')
        print('\n' .join(result))
        new_info = input('введите данные для уточнения')
        return search(result, new_info)


def change() -> None:
    """Изменение/удаление данных в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_edit = input('Введите данные для поиска')
    data_to_edit = search(data, data_to_edit)
    print(f'Выбранный контакт: {data_to_edit}')
    mode = input('Удалить или изменить? 1-удалить,2-изменить')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_contact()

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def enter_contact() -> str:
    fio = input('Ввведите ФИО: ')
    phone = input('Введите номер телефона: ')
    return f' {fio}|{phone}'
