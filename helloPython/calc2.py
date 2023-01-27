# Выражения для демонстрации работы программы
n1 = '10'
n2 = '12 + 15'                          # должно быть 27
n3 = '12 + 15 - 4'                      # должно быть 23
n4 = '12 - 4 * 2 + 6 / 3'               # должно быть 2
n5 = '( ( 12 - 3 ) * 2 ) + ( 2 + 1 )'    # должно быть 21
n6 = '( 2 + ( 12 - 3 ) * 2 ) + ( 2 + 1 )'    # должно быть 23
n7 = '( 2 + ( 12 - 3 ) * 2 ) / ( 1 + 1 )'    # должно быть 10

n = n7 # поменяйте цифру

m = n.split()
m2 = [] # стэк для чисел 
m3 = [] # стэк для знаков

bracket_count = 0   # для подсчета открытых скобок
prior = 1           # приоритет вычисления

def calc_expression(a, b, oper):
	if oper == '+':
		return (int(a) + int(b))
	if oper == '-':
		return (int(a) - int(b))
	if oper == '*':
		return (int(a) * int(b))
	if oper == '/':
		return (int(a) / int(b))

def bracket_calc_temp(m2, m3):
    i = len(m3) - 1
    while m3[i] != '(':
        b = m2.pop()
        a = m2.pop()
        oper = m3.pop()
        result = calc_expression(a, b, oper)
        m2.append(result)
        i -= 1
    m3.pop()

def mult_calc_temp(m2, m3):
    i = len(m3) - 1
    while m3[i] == '*' or m3[i] == '/':
        b = m2.pop()
        a = m2.pop()
        oper = m3.pop()
        result = calc_expression(a, b, oper)
        m2.append(result)
        i -= 1    

def befor_bracket_calc_temp(m2, m3):
    i = len(m3) - 1
    while m3[i] != '(':
        b = m2.pop()
        a = m2.pop()
        oper = m3.pop()
        result = calc_expression(a, b, oper)
        m2.append(result)
        i -= 1

for i in range(0, len(m)):
#____________________________добавление чисел в стек m2______________
    if m[i].isalnum() == True:
        m2.append(m[i])
#____________________________обработка скобок________________________
    elif m[i] == ')':                       # закрытие скобки
        bracket_count -= 1
        bracket_calc_temp(m2, m3)
        prior = 1
    elif m[i] == '(' and i == 0:            # если скобка открыта вначале
        m3.append(m[i])
        bracket_count += 1 
    elif m[i] == '(' and m[i - 1] == '(' or m[i] == '(' and bracket_count == 0:   # если открываем несколько скобок
        m3.append(m[i])
        bracket_count += 1        
    elif m[i] == '(' and bracket_count >= 1:    # если лополнительная скобка открывается где то в середине 
        save_znak = m3.pop()                # сохраняю знак
        befor_bracket_calc_temp(m2, m3)     # вычисляем то что между открывающихся скобок (1+2+(...
        m3.append(save_znak)                # возвращаем знак в стек
        m3.append(m[i])                     # заносим текущий знак ( из цикла 
        bracket_count += 1
#____________________________добаление знака + или - в стек m2 (приоритет 1)____________________    
    elif m[i] == '+' or m[i] == '-':
        if m[i] == '+' and prior == 1 or m[i] == '-' and prior == 1:
            m3.append(m[i])            
#____________________________добаление знака + или - в стек m2 если перед этим было * или / (приоритет 2)______
        elif m[i] == '+' and prior == 2 or m[i] == '-' and prior == 2:
            mult_calc_temp(m2, m3)
            m3.append(m[i])
            prior = 1
#__________________________добаление знака * или / в стек m2 (приоритет 2)____________________
    elif m[i] == '*' or m[i] == '/':
        m3.append(m[i])
        prior = 2    
 
#____________________________вычисление итога_______________________________________________
i = len(m3) - 1
while i != -1:
    b = m2.pop()
    a = m2.pop()
    oper = m3.pop()
    result = calc_expression(a, b, oper)
    m2.append(result)
    i -= 1


print (f'\nВычисление выражения: {n}\n   \nОтвет:  {m2[0]}\n')


