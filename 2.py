def hello_user():
    name = input('Введите своё имя: ')
    
    return name


print(f'Привет, {hello_user()}')