import contrоl

def finding(searching):
    with open("test.txt", "r") as file:
        lines = file.readlines()
        f = 0
        for line in lines:
            if searching in line:
                print(line)
        
    contrоl.user_choice()

def find_name():
    searching = input('Введите имя: ')
    finding(searching)                

def find_phone():
    searching = input('Введите телефон: ')
    finding(searching)