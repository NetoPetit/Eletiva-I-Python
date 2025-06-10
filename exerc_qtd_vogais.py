frase = input("Digite uma frase: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for x in range(len(frase)):
    if frase[x] == "a":
        a += 1
    if frase[x] == "e":
        e += 1
    if frase[x] == "i":
        i += 1
    if frase[x] == "o":
        o += 1
    if frase[x] == "u":
        u += 1
total = a + e + i + o + u
print(f"A quantidade de vogais em sua frase é: {total}")
