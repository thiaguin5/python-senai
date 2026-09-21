# Entrada de dados básicos
nome = input ("informe seu nome: ")
Nota1 = float (input ("digite a nota 1: "))
Nota2 = float (input ("digite a nota 2: "))

#processamento computacional
media = (Nota1 + Nota2) / 2 



#Saida de informações
print (f"Aluno : {nome}")

#Formatação com uma casa decimal
#f ->  significa numeros de ponto flutuante (decimal)
# .1  -> significa mostrar 1 casa decimal 
print (f"Média Final: {media: .1f}")