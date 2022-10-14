
mat = [[0 for i in range(4)] for j in range(4)]
mat_diag = []
soma = 0


for i in range(4):
    for j in range(4):
        mat[i][j] = float(input("Qual os dados? "))



for i in range(4):
        for j in range(4):
            print("[ '{:^5}' ]".format(mat[i][j]), end = " ")

            if i == j:
                soma =  soma + mat[i][j]
                mat_diag.append(mat[i][j])
        print()


print("Os números da diagonal principal da matriz é:", mat_diag)       
print("E a soma deles é:", soma)