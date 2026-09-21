#define a senha correta 

senha_correta = "1234"

#solivita a senha ao suario
senha = input("digite a senha: ")

#enquanto a senha estiver errada
while senha != senha_correta:

#informa que a senha esta errada
   print("Senha incorreta!")

#Solicita a senha novamente
   senha = input ("Digite a senha novamente: ")

#Quando a condição ficar falsa, a senha esta correta 
print ("senha correta! Acesso permitido.")