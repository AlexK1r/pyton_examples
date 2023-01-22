import contrоl

def delete_string(file):
    pos = int(input('Для удаления введите номер строки: '))
    pos = pos - 1

    with open(file, "r") as f:
        lines = f.readlines()
        if (pos >= 0) and (pos < len(lines)): # Проверка, корректна ли позиция pos
            del lines[pos]
            print('\nЗапись успешно удалена!\n')
        else:
            print(f'\nЗаписи с порядковым номером {pos + 1} не существует!\n')

    with open(file, "w") as f:
        f.writelines(lines)

def delete_bus():
    delete_string('buses.txt')
    contrоl.user_choice()

def delete_driver():
    delete_string('drivers.txt')
    contrоl.user_choice()
   
def delete_route():
    delete_string('bus_routes.txt')
    contrоl.user_choice()