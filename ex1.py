mat = [[0 for i in range(3)] for j in range(3)]

print(mat)

for i in range(3):
    for j in range(3):
        mat[i][j] = int(input("Qual o valor da posição [{} {}] : ".format(i, j) ))
    
for i in range(3):
    for j in range(3):
        print("[ '{:^5}' ]".format(mat[i][j]), end = " ")
    print()


