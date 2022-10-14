
mat = [[0 for i in range(3)] for j in range(3)]



for i in range(3):
    for j in range(3):
        mat[i][j] = float(input("Qual os dados? "))


for i in range(3):
        for j in range(3):
            print("[ '{:^5}' ]".format(mat[i][j]), end = " ")

        print()

print()

for i in range(3):
        for j in range(3):
            print("[ '{:^5}' ]".format(mat[j][i]), end = " ")

        print()