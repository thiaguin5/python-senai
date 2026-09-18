#Solicita o login do usuario

login = input ("Digite seu login: ")

#Solicita a senha do usuario

senha = input ("Digite sua senha: ")

# Verifica se o login e a senha estão corretos

if login == "admin" and senha == "1234":
    print ("seja-bem-vindo, administrador!")
else:
    print ("Login ou senha incorretos!")


