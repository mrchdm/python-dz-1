# a , b = map (input().split())
# приводит все элементы к одному и тому же виду map
# метод сплит делает из строки список

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# print("Напишите цифру, обозначающую день недели")
# number = int(input())
# if 0 < number < 8:
#     if number < 6:
#         print("нет")
#     else: 
#         print("да")
# else:
#     print("Введтие число от 1 до 7")



# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# print("Ввведите X")
# x = int(input())
# print("Ввведите Y")
# y = int(input())
# if x == 0 or y == 0:
#     print("x и y не должны быть равны нулю")
# else:
#     if x > 0 and y > 0:
#         print(1)
#     elif x > 0 and y < 0:
#         print(2)
#     elif x < 0 and y < 0:
#         print(3)
#     else:
#         print(4)



# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# print("Введите номер четверти")
# quarter = int(input())
# if quarter ==  1:
#     print("(0,+беск);(0,+беск)")
# elif quarter == 2:
#     print("(0,+беск);(0,-беск)")
# elif quarter == 3:
#     print("(0,-беск);(0,-беск)")
# elif quarter == 4:
#     print("(0,-беск);(0,+беск)")
# else:
#     print("Введите число от 1 до 4")



# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# формула - AB = sqrt (x2-x1)2+(y2-y1) 
# from cmath import sqrt
# print("Введите значение x точки A")
# x1 = int(input())
# print("Введите значение y точки A")
# y1 = int(input())
# print("Введите значение x точки B")
# x2 = int(input())
# print("Введите значение y точки B")
# y2 = int(input())
# AB = sqrt((x2-x1)**2 + (y2-y1)**2)
# print(AB)

'''def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a
def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result
statement = inputNumbers(3)
if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")'''
