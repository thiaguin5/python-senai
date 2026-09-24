# Crie uma lista vazia para armazenar nomes.

# Use um for para pedir 3 nomes ao usuário.

# A cada nome digitado, adicione o nome na lista usando append().

# No final, mostre todos os nomes cadastrados.

# Exemplo:

# Digite um nome: João
# Digite um nome: Maria
# Digite um nome: Pedro

# Nomes cadastrados: ['João', 'Maria', 'Pedro']

nomes = []

# Repete 3 vezes 
for i in range (3):
    nome = input("digite um nome: ")

    #adiciona um nome na lista 
    nomes.append(nome)

    print("Nomes cadastradatros: ", nomes)

for nome in nomes:
    print ("-", nomes)






   