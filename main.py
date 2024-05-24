nomes = ['Adão', "Helião", "Chups", 'Carminha', 'Maria Baixinha', 'João Boca Azeda', 'Beltiza', 'Erondina', 'Juninho Lobrega', 'Orizonmarden', 'Zequinha', 'Ninoca', 'Joabe', 'Noemia', 'Rosa', 'Juscelino']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# retorna o índice do nome pesquisado

# verifica se o nome está na lista ou não
try:
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')