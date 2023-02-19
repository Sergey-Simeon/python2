N = abs(int(input('Введите длину списка: ')))
List1 = input("Введите список: ").split()
num = list(map(int, List1))
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - num[0])
index = 0
for i in range(1, N):
    count = abs(X - num[i])
    if count < min:
        min = count
        index = i
print(f'Число {num[index]} в списке A наиболее близко по величине к числу {X}')