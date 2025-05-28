vog = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
frase = input("Frase: ")
for i in range(len(frase)):
    if frase[i] in vog:
        vog[frase[i]] = vog[frase[i]] + 1
print(vog)