# Programa: Verificação de passagem

# Faça um programa em Python que peça a idade de uma pessoa
# e verifique se ela paga passagem inteira ou meia passagem.

# Idade menor ou igual a 12 → Meia passagem
# Idade maior que 12 → Passagem inteira

#solicite idade
idade = int(input("diga a sua idade: "))

if idade >= 12 :
    print ("voce pagara passagem inteira -> 10$")
else:
    print ("voce pagara meia passagem -> 5$")


