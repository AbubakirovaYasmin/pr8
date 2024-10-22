a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))
if(isinstance(a, int) and isinstance(b, int)):
    start = min(a, b) + 1
    end = max(a, b)

    for num in range(start, end):
        print(num, end=' ')
else:
    print("Ошибка ввода")