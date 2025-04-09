import random

numero = random.sample(range(0, 11), 10)

print("Números aleatórios sorteados:")
print(numero)

soma = 0
for i in range(len(numero)):
    soma = soma + numero[i]

media = soma / 10

maior = 0
menor = 0
for i in range(len(numero)):
    if numero[i] > media:
        maior += 1
    if numero[i] < media:
        menor += 1
print(f"A soma dos numeros sorteados é {soma}\nA média dos números sorteados é {media}\nNúmeros sorteados maiores que a média {maior}\nNúmeros sorteados menores que a média {menor}")