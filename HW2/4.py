from math import pi

def circle_area():
    while True:
        try:
            radius = float(input('Введите радиус: '))
            break
        except ValueError:
            print('Радиус должен быть числом')
    
    return pi * radius * radius

print(f'Площадь круга = {circle_area()}')