import contrоl

def add_to_txt():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона без +7: ')
    
    with open("test.txt", "a") as file:
        file.write(surname + ' ' + name + ' +7' + phone + '\n')
           
    print('\nНовый контакт успешно добавлен!\n')
    contrоl.user_choice()