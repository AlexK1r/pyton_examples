# Вычислить значение выражения 
# 12 + 15 
# 12 / 15 
# t = 112 * 15

# где операторы?
# где числовые значения?

# Уровень 1

# 1 действие 
# 2 аргумента

# Уровень 2

# количество действий не определено

# 12 + 4 - 25

# Уровень 3

# действия имеют приоритет

# 12 - 4 * 3

# Уровень 4
# действия со скобками

# (12 - 4) * 2
#__________________________РЕШЕНИЕ_________________________________
# n = '23 * 100'
# m = n.split()

# a = int(m[0])
# oper = m[1]
# b = int(m[2])

# if oper == '+':
#     print(a + b)
# if oper == '*':
#     print(a * b)
# if oper == '-':
#     print(a - b)
# if oper == '/':
#     print(a / b)
# уровень 1 реализован

def calc_expression (a, b, oper):
    if oper == '+':
        return(a + b)
    if oper == '*':
        return(a * b)
    if oper == '-':
        return(a - b)
    if oper == '/':
        return(a / b)

n = '3 * 3 + 0 + 1'
m = n.split()

a = int(m[0])
oper = m[1]
b = int(m[2])
temp = calc_expression(a, b, oper)

del m[0:3]
long = len(m)

if long >= 2:
    for i in range(0, len(m), 2):
        a = temp
        oper = m[i]
        b = int(m[i + 1])
        temp = calc_expression(a, b, oper)
else:
    print(temp)

print(f'Ответ: {temp}')


