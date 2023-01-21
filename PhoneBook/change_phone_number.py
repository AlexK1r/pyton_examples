import contrоl

def change_phone():
    search_phone = input('Введите номер телефона который следует заменить: ')
    replace_phone_new = input('Введите новый номер телефона: ')
    with open("test.txt", "r") as file:
        lines = file.read()
        lines = lines.replace(search_phone, replace_phone_new)
                
    with open("test.txt", "w") as file:
         file.write(lines)

    print('\nУспешно изменено!\n')
    contrоl.user_choice()