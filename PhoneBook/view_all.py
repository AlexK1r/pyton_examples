import contrоl

def view_all():

    with open("test.txt", "r") as file:
        for line in file:
            print(line)
    
    fl = input('Для выхода в главное меню введите * : ')
    if fl == '*':
        contrоl.user_choice()