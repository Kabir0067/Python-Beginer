# Поле шахматной доски определяется парой чисел (a, b), каждое от 1 до 8, первое число задает номер столбца, второе – номер строки. Заданы две клетки.
# Определите, может ли шахматный король попасть с первой клетки на вторую за один ход.
# Входные данные
# Даны 4 целых числа от 1 до 8 каждое, первые два задают начальную клетку, вторые два задают конечную клетку. Начальная и конечная клетки не совпадают.
# Числа записаны в отдельных строках.
# Выходные данные
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую, или NO в противном случае.
x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if abs(x - x1) <= 1 and abs(y - y1) <= 1:
    print("YES")
else:
    print("NO")