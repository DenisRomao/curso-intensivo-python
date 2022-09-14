# metodo sort() para ordenar lista

cars = ['bmw', 'audi', 'toyota', 'subaru']

#ordena de forma alfabética permanentemente
cars.sort()
print(cars)

# argumento rever=True dentro do metodo sort() ordena a ordem alfabética de forma inversa

cars.sort(reverse=True)
print(cars)


# função sorted() altera a ordem de uma lista temporariamente

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)
print("\nHere ir the sorted list:")
print(sorted(cars))
print("\nHere is trhe original list again:")
print(cars)

# metodo reverse() inverte uma ordem original
cars.reverse()
print(cars)


# função len mostra o tamanho da lista

print(len(cars))
