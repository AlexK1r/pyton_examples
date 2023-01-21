

def digit_check():
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        print('Ошибка ввода! Попробуйте еще раз...\n')
        return digit_check()
        