# exercicio 3.10

lista_desejo = [
    'onePlus 10S pro',
    'fone bluetooth',
    'nissan versa',
    'soundBar samSung',
    'ar condicionado'
]

print('Quantidade de itens: ', len(lista_desejo), '\n')
print('Lista de desejo:')

lista_desejo.sort()
print(' Primeiro item da lista: ', lista_desejo[0].title(), '\n',
      'Segundo item da lista: ', lista_desejo[1].title(), '\n',
      'Terceiro item da lista: ', lista_desejo[2].title(), '\n',
      'Quarto item da lista: ', lista_desejo[3].title(), '\n',
      'Quinto item da lista: ', lista_desejo[4].title())

print('------------------------------------------------')

lista_desejo.remove('ar condicionado')
lista_desejo.append('macbook pro')

print(' Primeiro item da lista: ', lista_desejo[0].title(), '\n',
      'Segundo item da lista: ', lista_desejo[1].title(), '\n',
      'Terceiro item da lista: ', lista_desejo[2].title(), '\n',
      'Quarto item da lista: ', lista_desejo[3].title(), '\n',
      'Quinto item da lista: ', lista_desejo[4].title())

print('------------------------------------------------')

lista_desejo.insert(0, 'ipad pro')

print(' Primeiro item da lista: ', lista_desejo[0].title(), '\n',
      'Segundo item da lista: ', lista_desejo[1].title(), '\n',
      'Terceiro item da lista: ', lista_desejo[2].title(), '\n',
      'Quarto item da lista: ', lista_desejo[3].title(), '\n',
      'Quinto item da lista: ', lista_desejo[4].title(), '\n'
      'Sexto item da lista: ', lista_desejo[5].title())

print('------------------------------------------------')

remove1 = lista_desejo.pop(1)

print('Esse item nao e tao importante agora: ', remove1)

lista_desejo.reverse()
print(len(lista_desejo))

print('------------------------------------------------')


print(' Primeiro item da lista: ', lista_desejo[0].title(), '\n',
      'Segundo item da lista: ', lista_desejo[1].title(), '\n',
      'Terceiro item da lista: ', lista_desejo[2].title(), '\n',
      'Quarto item da lista: ', lista_desejo[3].title(), '\n',
      'Quinto item da lista: ', lista_desejo[4].title())

print('------------------------------------------------')

lista_desejo.sort(reverse=True)


print(' Primeiro item da lista: ', lista_desejo[0].title(), '\n',
      'Segundo item da lista: ', lista_desejo[1].title(), '\n',
      'Terceiro item da lista: ', lista_desejo[2].title(), '\n',
      'Quarto item da lista: ', lista_desejo[3].title(), '\n',
      'Quinto item da lista: ', lista_desejo[4].title())

print('------------------------------------------------')

print(sorted(lista_desejo))
