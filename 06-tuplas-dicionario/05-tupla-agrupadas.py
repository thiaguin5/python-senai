#tupla contendo outras tuplas
alunos = (
    ("Carlos", 17),
    ("Ana", 18),
    ("João", 16)


)

#Acessando a primeira dupla 
print(alunos[0])

#Carlos
print (alunos[0][0])

#idade do carlos
print(alunos [0][1])

#percorrendo os alunos 
for aluno in alunos:
    print("Nome: ", aluno[0])
    print("idade: ", aluno[1])
    print("-----------------")