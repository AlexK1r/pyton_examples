import input_check

def start():
    print('Привет! Вы в главном меню базы автобусов.\n')

def menu():
    menuitem = [
    ('Выберете пункт меню:', ''),
    ('1.', 'Показать все автобусы'),
    ('2.', 'Добавить новый автобус'),
    ('3.', 'Удалить автобус'),
    ('4.', 'Показать всех водителей'),
    ('5.', 'Добавить нового водителя'),
    ('6.', 'Удалить водителя'),
    ('7.', 'Показать все маршруты'),
    ('8.', 'Добавить новый маршрут'),
    ('9.', 'Удалить маршрут'),
    ('0.', 'Выход')]
    for i in menuitem:
        print(i[0], i[1])
    return input_check.digit_check()



