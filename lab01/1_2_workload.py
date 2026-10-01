subject1 = input('Название первого предмета: ')
lessons1 = int(input('Количество занятий первого предмета в неделю: '))
min1 = int(input('Продолжительность одного занятия первого предмета (мин): '))

subject2 = input('Название второго предмета: ')
lessons2 = int(input('Количество занятий второго предмета в неделю: '))
min2 = int(input('Продолжительность одного занятия второго предмета (мин): '))

hours = float(input('Доступное время на неделю (ч): '))

total1 = lessons1 * min1
total2 = lessons2 * min2
total_min = total1 + total2
total_hours = total_min / 60
free_hours = hours - total_hours
four_weeks = total_hours * 4

print()
print('    Учебная нагрузка')
print(subject1, ':', total1, 'минут')
print(subject2, ':', total2, 'минут')
print('Всего:', total_min, 'минут')
print('Всего:', f'{total_hours:.2f}', 'часов')
print('Свободное время:', f'{free_hours:.2f}', 'часов')
print('За 4 недели:', f'{four_weeks:.2f}', 'часов')
