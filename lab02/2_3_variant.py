total = int(input('Количество студентов: '))
capacity = int(input('Мест в автобусе: '))

full = total // capacity
remainder = total % capacity
needed = (total + capacity - 1) // capacity

print('Полных автобусов:', full)
print('Остаток:', remainder)
print('Всего автобусов:', needed)
