#exercicio 3.5 alterando um convidado da lista
lista_convidados = ['gabriel', 'samuel', 'layna', 'debora']

print(lista_convidados[0].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[1].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[2].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[3].title(),
      'gostaria de jantar em minha casa hoje')
lista_convidados.remove('debora')
print('Debora nao podera comparecer')

print(lista_convidados)

lista_convidados.append('Israel')

print(lista_convidados[0].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[1].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[2].title(),
      'gostaria de jantar em minha casa hoje \n', lista_convidados[3].title(),
      'gostaria de jantar em minha casa hoje')
