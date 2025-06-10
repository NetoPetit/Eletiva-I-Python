salario = int(input("Informe o salário do vendedor: "))
vendas = int(input("Qual o valor total de vendas no mês: "))

if vendas >= 1000 and vendas <= 5000 :
    salario = salario + 500
    print(f"O salário do vendedor com premiação será R${salario}")
elif vendas > 5000 and vendas <=7500 :
    salario = salario + 750
    print(f"O salário do vendedor com premiação será R${salario}")
elif vendas > 7500 :
    salario = salario + 1000
    print(f"O salário do vendedor com premiação será R${salario}")
else :
    print("O vendedor não atingiu nenhuma meta e não terá premiação.")

