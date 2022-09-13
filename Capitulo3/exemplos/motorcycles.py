from re import M


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# metodo append() adiciona ao final da lista um novo item
motorcycles.append('ducati')
print(motorcycles)

# medoto insert() adiciona elementos em qualquer posição em uma lista

motorcycles.insert(0, 'voltz')
print(motorcycles)

# instrução del remove elementos da lista

del motorcycles[0]
print(motorcycles)

del motorcycles[3]
print(motorcycles)

# metodo pop() retira o ultimo item da lista
#retirando um item de motorcycles e adicionando na variavel popped_motorcycle com metodo pop()
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print('item retirado da lista de motorcycles:', popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


# metodo remove() remove um item sabendo seu valor e não sua posição

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expansive = 'ducati'
motorcycles.remove(too_expansive)
print(motorcycles)
print("\nA " + too_expansive.title() + ' is too expansive for me.')
