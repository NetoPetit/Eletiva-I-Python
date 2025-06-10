real = float(input("Qual valor em R$ deseja converter para U$: "))
cotacao = float(input("Qual o valor da cotação: "))

dolar = real / cotacao

print(f"R${real} convertido em Dólar na cotação informada será U${dolar:.2f}")