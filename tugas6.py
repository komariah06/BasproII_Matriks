nested_list_1 = [
    [4, 2, 7, 1, 5],
    [3, 6, 2, 8, 9],
    [5, 1, 3, 4, 2],
    [9, 2, 6, 7, 3],
    [8, 5, 1, 2, 4]
]

nested_list_2 = [
    [6, 3, 2, 7, 1],
    [4, 8, 9, 5, 2],
    [1, 7, 3, 6, 8],
    [5, 2, 4, 3, 9],
    [9, 6, 1, 4, 7]
]

nested_list_3 = []

for i in range(5):
    baris = []
    for j in range(5):
        jumlah = 0
        for k in range(5):
            jumlah += nested_list_1[i][k] * nested_list_2[k][j]
        baris.append(jumlah)
    nested_list_3.append(baris)

print("Hasil Perkalian Matriks:")
for row in nested_list_3:
    print(row)
