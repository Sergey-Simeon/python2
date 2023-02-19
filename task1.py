N = abs(int(input('Введите количество элементов: ')))
list1 = input("Введите список: ").split()
num = list(map(int, list1))

X = int(input('Введите искомое число Х: '))
count = 0
for i in range(N):
    if num[i] == X:
        count += 1
print(f'Число {X} встречается в списке {count} раз') 