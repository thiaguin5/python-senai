# Cria um programa que percorra os números de 1 a 10 
# e mostre se cada número é par ou ímpar.
# % 2 == 0 

#lista 

for numero in range (1,11):
  if numero % 2 == 0:
    print (numero , "numero par") 
  else:
    print (numero , "numero impar")