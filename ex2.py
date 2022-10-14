import random

mat_usuario = [[0 for i in range(3)] for j in range(3)]
mat_aleatoria = [[0 for i in range(3)] for j in range(3)]
mat_soma = [[0 for i in range(3)] for j in range(3)]
mat_produto = [[0 for i in range(3)] for j in range(3)]


for i in range(3):
    for j in range(3):
        mat_usuario[i][j] = float(input("Qual o valor? "))
        mat_aleatoria[i][j] = random.randrange(0, 100)
        mat_soma[i][j] = mat_usuario[i][j] + mat_aleatoria[i][j]
        mat_produto[i][j] = mat_usuario[i][j] * mat_aleatoria[i][j]

def roda_matriz(mat):
    for i in range(3):
        for j in range(3):
            print("[ '{:^6}' ]".format(mat[i][j]), end = " ")   
        print()

def mostra_matriz():
    print("Matriz usuário:")
    roda_matriz(mat_usuario)
    print("Matriz aleatória")
    roda_matriz(mat_aleatoria)
    print("Matriz soma")
    roda_matriz(mat_soma)
    print("Matrz produto")
    roda_matriz(mat_produto)

mostra_matriz()
