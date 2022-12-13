from random import randint


array = [randint(-100, 100) for _ in range (100)]
arrayTwo = [randint(-100, 100) for _ in range (100)]

array = set(array)
arrayTwo = set(arrayTwo)

print(f'Первый массив: {array} \nВторой массив: {arrayTwo}')
print(f'A⋂B - {array.intersection(arrayTwo)}')
print(f'A\(A⋂B) - {array.difference(arrayTwo)}')
print(f'B\(A⋂B) - {array.difference(arrayTwo)}')
print(f'(AUB)\(A⋂B) - {array.symmetric_difference(arrayTwo).union(arrayTwo.symmetric_difference(array))}')
