import contrоl

def view_all(file):
    with open(file, "r") as f:
        for line in f:
            print(line)

def read_data_from_file(file):
    rawdata_list = []
    with open(file, 'r', encoding='utf8') as f: # , encoding='utf8'
        for line in f:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list

def view_buses():
    view_all('buses.txt')
    contrоl.user_choice()

def view_drivers():
    view_all('drivers.txt')
    contrоl.user_choice()

def view_bus_routes():
    routes = read_data_from_file('bus_routes.txt')
    buses = read_data_from_file('buses.txt')
    drivers = read_data_from_file('drivers.txt')
    print("Список маршрутов: \n")
    for r_name,r_number,r_bus,r_driver in routes:
        bus_number = get_item_by_id(r_bus,buses)
        driver_name = get_item_by_id(r_driver,drivers)        
        print("{:>7} {:>4} {:>12} {:>9}".format(r_name, r_number, driver_name, bus_number))
    contrоl.user_choice()

# вспомогательные
def view_buses_add():
    view_all('buses.txt')

def view_drivers_add():
    view_all('drivers.txt')

def get_item_by_id(id,records):
    for id_record,item_record in records:
        if id==id_record:
            return item_record
            break
    return None

