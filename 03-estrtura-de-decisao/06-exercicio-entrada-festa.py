# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

#Solicite a idade

idade = int(input("Digite sua idade: "))

#condição 

if idade >= 18:
   print("voce pode entrar na festa")
elif idade >= 16:
    print("voce pode entrar apenas com o responsavel")
else:
    print("voce nao pode entrar")