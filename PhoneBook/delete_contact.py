import contrоl

def del_to_txt():
    pos = int(input('Для удаления введите номер строки: '))
    pos = pos - 1

    with open("test.txt", "r") as file:
        lines = file.readlines()
        if (pos >= 0) and (pos < len(lines)): # Проверка, корректна ли позиция pos
            del lines[pos]
            print('\nЗапись успешно удалена!\n')
        else:
            print(f'\nЗаписи с порядковым номером {pos + 1} не существует!\n')

    with open("test.txt", "w") as file:
        file.writelines(lines)

    contrоl.user_choice()