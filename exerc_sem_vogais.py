vogais = "aeiouAEIOU"
resultado = ""
frase = input("Digite uma frase: ")

for letra in frase:
    if letra not in vogais:
        resultado += letra

print("Frase sem vogais:", resultado)
