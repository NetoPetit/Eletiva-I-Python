soma = 0
opcao = input("Deseja inserir um valor? [s / n]: ")

while opcao == "s" or opcao == "S" :
    valor = int(input("Digite um valor: "))
    soma = soma + (valor ** 2)
    opcao = input("Deseja inserir outro valor? [s / n]: ")

print(f"A soma dos quadrados dos números informados é: {soma}")