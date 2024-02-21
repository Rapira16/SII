import numpy
from sys import exit

x = float(input('Введите 1 число:'))
operator = input('Введите оператор(+, -, *, /, sin, cos, ^, exp)')
y = float(input('Введите 2 число:'))
if (y == 0.0) and (operator == '/'):
    print('Деление на 0')
    exit()
match operator:
    case '+':
        print('x+y', x + y)
    case '-':
        print('x-y', x - y)
    case '*':
        print('x*y', x * y)
    case '/':
        print('x/y', x / y)
    case 'sin':
        print('sin(x+y)', numpy.sin(x + y))
    case 'cos':
        print('cos(x+y)', numpy.cos(x + y))
    case '^':
        print('x^y', numpy.power(x, y))
    case 'exp':
        print('exp(x+y)', numpy.exp(x + y))
    case _:
        print('Нет такого оператора')