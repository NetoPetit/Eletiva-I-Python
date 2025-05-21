primos = {1,2,3,5,7,11,13,17,19,23,29}
nroStr = input("Nro: ")

while nroStr:
    nro = int(nroStr)

    if nro in primos:
        print("O nro %d = Primo" % nro)
    else:
        print("O nro %d = Ñ Primo" % nro)
    nroStr = input("Nro: ")

print("***FIM***")