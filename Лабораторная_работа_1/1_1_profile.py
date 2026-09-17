surname = input('Фамилия: ')
name = input('Имя: ')
group = input('Группа: ')
city = input('Город: ')
age = int(input('Возраст: '))
subject = input('Любимый предмет: ')
study_hours = float(input("Часов подготовки в неделю: "))
age_4 = age + 4
hours_4 = study_hours * 4
hours_per_day = study_hours / 7
print()
print('         КАРТОЧКА СТУДЕНТА')
print('Имя и фамилия:', name, surname)
print('Группа:', group)
print('Город:', city)
print('Возраст через 4 года:', age_4)
print('Любимый предмет:', subject)
print('Подготовка за 4 недели:', f'{hours_4:.2f}', 'ч.')
print('Подготовка в день:', f'{hours_per_day:.2f}', 'ч.')
