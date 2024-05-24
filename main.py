nomes = ['Adão', "Helião", "Chups", 'Carminha', 'Maria Baixinha', 'João Boca Azeda', 'Beltiza', 'Erondina', 'Juninho Lobrega', 'Orizonmarden', 'Zequinha', 'Ninoca', 'Joabe', 'Noemia', 'Rosa', 'Juscelino']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ')

# retorna o índice do nome pesquisado
indice = nomes.index(nome)

# verifica se o nome está na lista ou não
if nome in nomes:
    print(f'Nome encontrado: {nome} no índice {indice}.')
else:
    print(f'{nome} não encontrado na lista.')