lista_convidados = ['katy', 'gabriel', 'samuel',
                    'rebecca', 'layna', 'israel', 'clara']

print(lista_convidados[0].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[1].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[2].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[3].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[4].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[5].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[6].title(),
      'gostaria de jantar em minha casa hoje',)


print('Infelizmente minha mesa maior nao chegara a tempo,\n poderei convidar apenas dois para jantar em minha casa')

remove_1 = lista_convidados.pop(0)

print('Me desculpe nao poder convida-lo(a) para o jantar', remove_1.title())

remove_2 = lista_convidados.pop(0)
print('Me desculpe nao poder convida-lo(a) para o jantar', remove_2.title())

remove_3 = lista_convidados.pop(0)
print('Me desculpe nao poder convida-lo(a) para o jantar', remove_3.title())

remove_4 = lista_convidados.pop(0)
print('Me desculpe nao poder convida-lo(a) para o jantar', remove_4.title())

remove_5 = lista_convidados.pop(0)
print('Me desculpe nao poder convida-lo(a) para o jantar', remove_5.title())

print(lista_convidados[0].title(), 'voce ainda e meu convidado\n',
      lista_convidados[1].title(), 'voce ainda e meu convidado')

del lista_convidados[0]
del lista_convidados[0]

print(lista_convidados)
