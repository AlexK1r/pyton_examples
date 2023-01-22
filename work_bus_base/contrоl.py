import user_menu
import view_all as va
import add_instance as ai
import delete as de


def user_choice():
    choice_num = user_menu.menu()
    if choice_num < 0 or choice_num > 9:
        print('\nОшибка ввода! Попробуйте еще раз...\n')
        user_choice()    
    elif choice_num == 1:
        va.view_buses()      
    elif choice_num == 2: 
        ai.add_bus()         
    elif choice_num == 3: 
        de.delete_bus()         
    elif choice_num == 4:
        va.view_drivers()     
    elif choice_num == 5:
        ai.add_driver()     
    elif choice_num == 6:
        de.delete_driver()
    elif choice_num == 7:
        va.view_bus_routes()
    elif choice_num == 8:
        ai.add_route()
    elif choice_num == 9:
        de.delete_route()        
    elif choice_num == 0:
        print('\nУдачи!')
        exit()

