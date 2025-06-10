produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
valor = float(input("Digite o valor da unidade: "))
percentual = float(input("Digite o percentual do desconto: "))

desconto = (valor * quantidade) * (percentual / 100)
total = (valor * quantidade) - desconto

print(f"O produto da venda é {produto}, e o seu total com {percentual}% de desconto é R${total}")
