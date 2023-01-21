import user_menu
import add_contact as ac
import find_phone_number as ftif
import delete_contact as dc
import change_phone_number as cpn
import view_all as va

def user_choice():
    choice_num = user_menu.menu()
    if choice_num < 0 or choice_num > 6:
        print('\nОшибка ввода! Попробуйте еще раз...\n')
        user_choice()    
    elif choice_num == 1:
        va.view_all()      
    elif choice_num == 2: 
        ftif.find_name()         
    elif choice_num == 3: 
        ftif.find_phone()         
    elif choice_num == 4:
        ac.add_to_txt()     
    elif choice_num == 5:
        dc.del_to_txt()     
    elif choice_num == 6:
        cpn.change_phone()    
    elif choice_num == 0:
        print('\nУдачи!')
        exit()

