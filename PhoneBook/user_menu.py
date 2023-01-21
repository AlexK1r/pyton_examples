import input_check
# from export_in_file import export_txt

def start():
    hi = 'Привет! Вы в главном меню телефонной книги.\n'

    print(f'{hi}\n')

def menu():
    what_to_do = 'Укажи цифру меню:'
    view_all_contact = '1. Показать все'
    find_name = '2. Найти запись по вхождению частей имени'
    find_phone = '3. Найти запись по телефону'
    new_contact = '4. Добавить контакт'
    delete_contact = '5. Удалить контакт'
    change_to_phone = '6. Изменить номер телефона у контакта'
    to_exit = '0. Выход'
    print(f'{what_to_do}\n\n{view_all_contact}\n{find_name}\n{find_phone}\n{new_contact}\n{delete_contact}\n{change_to_phone}\n{to_exit}')
    return input_check.digit_check()



