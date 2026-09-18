# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso


peso = float (input("qual o seu peso: "))
altura =float (input("qual a sua altura: "))

#calculo de IMC
imc = peso / (altura * altura )

#condição
if imc >= 18.5 :
    print ("peso normal")
elif imc >= 25 :
    print ("acima do peso")
else: 
    print ("abaixo do peso")
