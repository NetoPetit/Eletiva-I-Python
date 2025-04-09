tamanho = 19

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for i in range(tamanho):
    ultimo = lista.pop()
    lista.insert(0, ultimo)
print(lista)

for i in range(tamanho):
    primeiro = lista.pop(0)
    lista.append(primeiro)
print(lista)