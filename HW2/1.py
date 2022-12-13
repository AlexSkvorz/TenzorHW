def operations_with_digits():
    while True:
        try:
            x = float(input('Введите первое число: '))
            y = float(input('Введите второе число: '))
            break
        except ValueError:
            print('Введите число:')
    
    print()
    print(f'Результат сложения: {x + y}')
    print(f'Результат вычитания: {x - y} | {y - x}')
    print(f'Результат умножения: {x * y}')
    print(f'Результат деления: {x / y} | {y / x}')
    print(f'Результат возведения в степень: {x ** y} | {y ** x}')
    print(f'Результат деления по модулю: {x % y} | {y % x}')
    print(f'Результат целочисленного деления: {x // y} | {y // x}')



operations_with_digits()