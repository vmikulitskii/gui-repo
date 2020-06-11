"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
a = 5
b = 6
c = 7

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b or a == c or b == c:
        if a == b and b == c:
            print('У вас получится равносторонний треугольник')
        else:
            print('У вас получится равнобедренный треугольник')
    else:
        print('У вас получится разносторонний треугольник')
else:
    print('Треугольника с такими сторонам не может существовать')
