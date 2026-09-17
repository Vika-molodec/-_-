order = input('Название заказа: ')
customer = input('Имя заказчика: ')

name1 = input('Название первой позиции: ')
quantity1 = int(input('Количество первой позиции: '))
price1 = float(input('Цена первой позиции: '))

name2 = input('Название второй позиции: ')
quantity2 = int(input('Количество второй позиции: '))
price2 = float(input('Цена второй позиции: '))

delivery = float(input('Стоимость доставки: '))
paid = float(input('Внесено: '))

cost1 = quantity1 * price1
cost2 = quantity2 * price2
products = cost1 + cost2
total = products + delivery
quantity = quantity1 + quantity2
change = paid - total

print()
print('      ЗАКАЗ')
print('Название заказа:', order)
print('Заказчик:', customer)
print()
print('Название | Количество | Цена | Стоимость')
print(name1, '|', quantity1, '|', f'{price1:.2f}', '|', f'{cost1:.2f}')
print(name2, '|', quantity2, '|', f'{price2:.2f}', '|', f'{cost2:.2f}')
print()
print('Товары:', f'{products:.2f}', 'руб.')
print('Доставка:', f'{delivery:.2f}', 'руб.')
print('Всего:', f'{total:.2f}', 'руб.')
print('Количество единиц:', quantity)
print('Сдача:', f'{change:.2f}', 'руб.')
