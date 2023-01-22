list1 = ['1','2', '3']
list2 = ['4','5', '6']
list3 = ['7','8', '9']
print(list1)
print(list2)
print(list3)
print()
def hod1(u1):
    if u1 == 1:
        list1[0] = 'X'
    elif u1 == 2:
        list1[1] = 'X'
    elif u1 == 3:
        list1[2] = 'X'
    elif u1 == 4:
        list2[0] = 'X'
    elif u1 == 5:
        list2[1] = 'X'
    elif u1 == 6:
        list2[2] = 'X'
    elif u1 == 7:
        list3[0] = 'X'
    elif u1 == 8:
        list3[1] = 'X'
    elif u1 == 9:
        list3[2] = 'X'
    print(list1)
    print(list2)
    print(list3)
u1 = int(input('Игрок_1, делай ход в любую свободную клетку: '))
print(hod1(u1))

def hod2(u2):
    if u2 == 1:
        list1[0] = 'O'
    elif u2 == 2:
        list1[1] = 'O'
    elif u2 == 3:
        list1[2] = 'O'
    elif u2 == 4:
        list2[0] = 'O'
    elif u2 == 5:
        list2[1] = 'O'
    elif u2 == 6:
        list2[2] = 'O'
    elif u2 == 7:
        list3[0] = 'O'
    elif u2 == 8:
        list3[1] = 'O'
    elif u2 == 9:
        list3[2] = 'O'
    print(list1)
    print(list2)
    print(list3)
u2 = int(input('Игрок_2, делай ход в любую свободную клетку: '))
print(hod2(u2))

print(hod1(u1 = int(input('Игрок_1, делай ход в любую свободную клетку: '))))
print(hod2(u2 = int(input('Игрок_2, делай ход в любую свободную клетку: '))))
print(hod1(u1 = int(input('Игрок_1, делай ход в любую свободную клетку: '))))


if (list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[0] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[2] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[1] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
else:
    print(hod2(u2 = int(input('Игрок_2, делай ход в любую свободную клетку: '))))

if (list1[0] == 'O' and list1[1] == 'O' and list1[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[0] == 'O' and list2[0] == 'O' and list3[0] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[1] == 'O' and list2[1] == 'O' and list3[1] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[2] == 'O' and list2[2] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[2] == 'O' and list2[1] == 'O' and list3[0] == 'O'):
    print('Победа Игрока_2!!!')
else:
    print(hod1(u1 = int(input('Игрок_1, делай ход в любую свободную клетку: '))))


if (list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[0] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[2] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[1] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
else:
    print(hod2(u2 = int(input('Игрок_2, делай ход в любую свободную клетку: '))))

if (list1[0] == 'O' and list1[1] == 'O' and list1[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[0] == 'O' and list2[0] == 'O' and list3[0] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[1] == 'O' and list2[1] == 'O' and list3[1] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[2] == 'O' and list2[2] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O'):
    print('Победа Игрока_2!!!')
elif (list1[2] == 'O' and list2[1] == 'O' and list3[0] == 'O'):
    print('Победа Игрока_2!!!')
else:
    print(hod1(u1 = int(input('Игрок_1, делай ход в любую свободную клетку: '))))

if (list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[0] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[2] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[0] == 'X' and list2[1] == 'X' and list3[2] == 'X'):
    print('Победа Игрока_1!!!')
elif (list1[2] == 'X' and list2[1] == 'X' and list3[0] == 'X'):
    print('Победа Игрока_1!!!')
else:
    print('Ничья :)')

