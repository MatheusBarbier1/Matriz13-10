
mat_alunos = [[" " for i in range(1)] for j in range(3)]
mat_idade = [[0 for i in range(1)] for j in range(3)]

print(mat_alunos)


for i in range(3):
    for j in range(1):
        mat_alunos[i][j] = str(input("Qual o nome do aluno? "))
        mat_idade[i][j] = int(input("Qual a idade? "))


for i in range(3):
        for j in range(1):
            print("[ '{:^10}' ]".format(mat_alunos[i][j]), end = " ")   
            print("[ '{:^5}' ]".format(mat_idade[i][j]), end = " ")   
        print()


