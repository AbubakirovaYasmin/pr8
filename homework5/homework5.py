total_sum = 0
print("Для завершенния ввода воспользуйтесь 'stop' или 'end' ")
while True:
    user_input = input("Введите число: ")

    if user_input.lower() in ['stop', 'end']:
        break

    if user_input.replace('.', '', 1).isdigit() or (user_input.startswith('-') and user_input[1:].replace('.', '', 1).isdigit()):
        total_sum += int(float(user_input))
    else:
        print("Пожалуйста, вводите только числа.")

print(f"Сумма чисел: {total_sum}")