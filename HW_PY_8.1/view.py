def user_menu():
    menu = ["Показать всех сотрудников", "Добавить сотрудника",
            "Удалить сотрудника", "Изменить данные сотрудника",]
    for item in enumerate(menu, 1):
        print(*item)
    num = int(input("Выберите пункт меню: "))
    return num


def user_data_entry():
    name = input("Имя -> ")
    surname = input("Фамилия -> ")
    post = input("Должность -> ")
    directory_entry = [name, surname, post]
    return directory_entry


def view_user(data):
    for row in enumerate(data, 1):
        print(*row)


def up_del_user():
    num = int(input("Введите номер записи для изменения = "))
    return num - 1
