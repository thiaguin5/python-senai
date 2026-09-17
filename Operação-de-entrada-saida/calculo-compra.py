# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

#Entrada de dados 
nome = input ("Diga o nome de um produto: ")
preco = float(input ("Diga seu preço : "))
quantidade = int(input ("Diga a quantidade comprada : "))

#Processamneto computacional

total = preco * quantidade 


#saida de informações 
print (f"O valor total sera: {total}")