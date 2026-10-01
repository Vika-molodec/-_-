a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
operation = input('Введите операцию (+, -, *, /): ')

if operation == '+':
    result = a + b
    print('{:.2f}'.format(result))
elif operation == '-':
    result = a - b
    print('{:.2f}'.format(result))
elif operation == '*':
    result = a * b
    print('{:.2f}'.format(result))
elif operation == '/':
    if b == 0:
        print('Деление на ноль запрещено')
    else:
        result = a / b
        print('{:.2f}'.format(result))
else:
    print('Неизвестная операция')
