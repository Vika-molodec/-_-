room1 = input('Первая аудитория: ')
room2 = input('Вторая аудитория: ')

temporary = room1
room1 = room2
room2 = temporary

print('Первая аудитория:', room1)
print('Вторая аудитория:', room2)
