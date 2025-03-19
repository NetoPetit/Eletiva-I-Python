print("Calcule a quantidade de dias corridos entre duas datas:")

data1 = int(input("Informe a primeira data: "))
data2 = int(input("Informe a segunda data: "))

dias = 0
for x in range(data1, data2, 1) :
    dias += 1

print(f"A quantidade de dias corridos entre as duas datas é {dias} dias")
