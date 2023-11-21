tuple = (4, 6, 9, True, 'text', 1.5) # Кортеж
print(tuple[0:2]) # Выводит с такого то по такой то элемент
# tuple[1] = 'text' # Не работает
print(tuple.count(False)) # Выводит сколько таких элементов
print(tuple) # Выводит кортеж

data = True, 7 # Можно писать без скобок
print(data)

for i in tuple: # Перебор кортежа
    print(i)

numbers = [1, 2, 3, 4.5] # Список
new_date = tuple(numbers) # Кортеж-список
word = tuple('Hello world') # Кортеж (неполноправный - для перебора)
print(word) # Перебор