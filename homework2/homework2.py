while True:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
        num1 = int(float(num1))
        num2 = int(float(num2))

        result = num1 + num2
        print(f"Сумма: {result}")
    else:
        print("Ошибка ввода")
    print("Пожалуйста, вводите числовые значения.")