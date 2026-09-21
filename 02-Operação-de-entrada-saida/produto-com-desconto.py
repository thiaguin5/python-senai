#Entrada de dados
preco = float (input("digite o preço do produto: "))
desconto = float (input ("Digite o desconto (%):  "))


# Processameneto Computacional 
valor_desconto = preco * desconto / 100
valor_final = preco - valor_desconto 


#Saida de Informações 
print (f"Preço digitado: R$ {preco:.2f}")
print (f"desconto digitado: R$ {desconto:.1f}%")
print (f"valor de desconto: R$ {valor_desconto:.2f}")
print (f"valor final: R$ {valor_final:.2f}")

