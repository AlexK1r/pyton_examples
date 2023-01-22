import contrоl
import view_all as va

def find_end_in_file(file, searching):
    with open(file, 'r') as f:
        lines = f.readlines()        
        count = 0
        for line in lines: #проверка на дубли
            if searching in line:
                print('\nТакая запись уже есть!\n')
                contrоl.user_choice()
            count += 1 # считаем строки в файле        
        return(count)

def add_bus():
    reg_number = input("Введите регистрационный знак: ")
    #дальше ловлю количество строк, добавляю 1 и это чило будет номером следующей записи в файле    
    sequence_number_bus = str(find_end_in_file("buses.txt", reg_number) + 1) 

    with open("buses.txt", "a") as f:
        f.write('bus' + sequence_number_bus + ',' + reg_number + '\n')
        print('\nНовая запись успешно добавлена!\n')
        contrоl.user_choice()    
    
def add_driver():
    name = input("Введите имя водителя: ")
    sequence_number_driver = str(find_end_in_file("drivers.txt", name) + 1)
        
    with open("drivers.txt", "a") as f:
        f.write('driver' + sequence_number_driver + ',' + name + '\n')
           
    print('\nНовая запись успешно добавлена!\n')
    contrоl.user_choice()
 
def add_route():
    route_number = input("Введите номер маршрута (номер на табличке автобуса): ")
    sequence_number_route = str(find_end_in_file("drivers.txt", route_number = 'пока такой бред') + 1)
    print("доступны автобусы: ")
    va.view_buses_add()
    sequence_number_bus = input("Введите порядковый номер автобуса (только цифру): ")
    print("доступны водители: ")
    va.view_drivers_add()
    sequence_number_driver = input("Введите порядковый номер водителя (только цифру): ")
        
    with open("bus_routes.txt", "a") as f:
        f.write('m' + sequence_number_route + ',' + route_number + ',bus' + sequence_number_bus + ',driver' + sequence_number_driver + '\n')
           
    print('\nНовая запись успешно добавлена!\n')
    contrоl.user_choice()

   