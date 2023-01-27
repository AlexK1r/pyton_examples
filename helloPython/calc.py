# Пока работает только с одной скобкой в выражении
# Должен работать с любыми варианами +, -, *, / и в любом месте ()
# надо вынести проверку на ( ) и расчет внутри ( ) в отдельную функцию, а результат записывать вместо скобки в тело списка m[]
# после вновь проверять m[] на ( )   


#________переменные_________________________

# укажите выражение (после символа пробел обязателен!)
#n = '12 + 15'
#n = '12 + 15 - 4'
#n = '12 - 4 * 2 + 6 / 3'
n = '( 12 - 4 ) * 2' 

m = n.split()
m2 = [] # применяется в вычислении * и / 
m3 = [] # применяется в решение выражения в скобках

bracket = False # флаг скобки
bracket_count = 0 # для подсчета знаков в скобке
bracket_start = 0
multiply = False # флаг умножения/деления
new_object = True # флаг начала
temp = 0

# _______вспомогательные функции____________

def calc_expression(a, b, oper):
	if oper == '+':
		return (a + b)
	if oper == '-':
		return (a - b)
	if oper == '*':
		return (a * b)
	if oper == '/':
		return (a / b)
		
def multiplication_calculation(m, multiply, new_object):
# проверяем есть ли * или /
    for i in range(1, len(m) - 1, 2): # убрал len(m) - 1
# выполняется если в выражении последующее действие * или /
        if m[i] == '*' and multiply == True or m[i] == '/' and multiply == True:            
            temp = calc_expression(temp, int(m[i + 1]), m[i])
            m2.pop(-1) # удаляем последний знак
            m2.append(temp) # добавляем число
            multiply = True    
# выполняется если в выражении первое действие * или /
        elif m[i] == '*' and multiply == False or m[i] == '/' and multiply == False:              
            if new_object == True: # если это начало то очистим массив
                m2.clear()
            new_object = False
            temp = calc_expression(int(m[i - 1]), int(m[i + 1]), m[i])
            m2.append(temp) # добавляем число
            multiply = True    
# выполняется после операций уножения или деления (если действие + или - после * или /)
        elif m[i] != '*' and multiply == True and i + 2 != len(m) or m[i] != '/' and multiply == True and i + 2 != len(m):
            multiply = False
            m2.append(m[i]) # просто ставлю знак
# проверка начала выражения
        elif i == 1 and multiply == False:                                                                        
            m2.clear() # сначало очистим массив
            new_object = False
            m2.append(int(m[0]))
            m2.append(m[i])
# проверка конца выражения 1 сценарий (если последнее действие + или - после * или / в конце выражения )
        elif i + 2 == len(m) and m[i] != '*' and multiply == True or i + 2 == len(m) and m[i] != '/' and multiply == True:    
            m2.append(m[i])
            m2.append(int(m[i + 1]))
# проверка конца выражения 2 сценарий (если последнее действие + или - в конце выражения)
        elif i + 2 == len(m) and m[i] != '*' or i + 2 == len(m) and m[i] != '/':    
            m2.append(int(m[i - 1]))
            m2.append(m[i])
            m2.append(int(m[i + 1]))
# если в предыдущем действие нет * или / 
# и это небыло мульти циклом этих действий
        elif multiply == False:
            m2.append(int(m[i - 1]))    # ставлю предыдущее число 
            m2.append(m[i])             # ставлю знак "шага"
            multiply = False
        if len(m) == 3 and len(m2) == 2:
            m2.append(int(m[i + 1]))
    return m2

# _______тело программы____________________
#ищю скобку и записываю выражение в новый массив
for i in range(0, len(m) - 1):
    if m[i] == '(':
        bracket_start = i
        bracket = True
        m3.clear()
    if m[i] == ')':            
        bracket = False
    if bracket == True and m[i] != '(':        
        m3.append(m[i])
        bracket_count += 1
# убраем из первичного массива выражение в скобках
if bracket_count != 0 and m3 != None:    
    i = 0
    while i < bracket_count + 2: # двойка чтобы убрать скобки
        m.pop(bracket_start)
        i += 1
    # print(m)
    m3 = multiplication_calculation(m3, multiply, new_object)
# вычисляю скобку и полученное значение записываем в начало массива 
if bracket_count != 0 and len(m3) > 1:
    temp = calc_expression(m3[0], m3[2], m3[1])
    for i in range(4, len(m3), 2):
        temp = calc_expression(temp, m3[i], m3[i - 1])
    m.insert(bracket_start, temp)
    m3.clear()
    #print(m)
elif bracket_count == 0 and len(m3) == 1:
    m.insert(0, temp)
    m3.clear()
    #print(m)
    
#print (m)
m = multiplication_calculation(m, multiply, new_object)
#print (m)
# обобщение полученых вычислений
if len(m) > 1:
    temp = calc_expression(m[0], m[2], m[1])
    for i in range(4, len(m), 2):
        temp = calc_expression(temp, m[i], m[i - 1])
else:
    temp = m[0]
print(f'\nРезультат вычисления выражения: {n}  =  {temp}\n')

