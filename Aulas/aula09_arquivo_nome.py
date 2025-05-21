n = int(input("N: "))

gravar_nome = open("C:\\Users\\si\\Desktop\Matérias\\Eletiva I\\Aulas\\nome.txt", "w")
for i in range(n):
    nome = input("Digite o nome: ")
    gravar_nome.write(str(nome) + "\n")
gravar_nome.close()

gravar_sobrenome = open("C:\\Users\\si\\Desktop\Matérias\\Eletiva I\\Aulas\\sobrenome.txt", "w")
for i in range(n):
    sobrenome = input("Digite o sobrenome: ")
    gravar_sobrenome.write(str(sobrenome) + "\n")
gravar_sobrenome.close()

ler_nome =  open("C:\\Users\\si\\Desktop\Matérias\\Eletiva I\\Aulas\\nome.txt", "r")
ler_sobrenome = open("C:\\Users\\si\\Desktop\Matérias\\Eletiva I\\Aulas\\sobrenome.txt", "r")
gravar_nomeCompleto = open("C:\\Users\\si\\Desktop\Matérias\\Eletiva I\\Aulas\\nomeCompleto.txt", "w")
nome1 = ler_nome.readline()
sobrenome1 = ler_sobrenome.readline()
nomeCompleto1 = gravar_nomeCompleto.write()
while ler_nome:
    nome1 = ler_nome.readline()
    sobrenome1 = ler_sobrenome.readline()
    nomeCompleto1 = gravar_nomeCompleto.write()
ler_nome.close()
ler_sobrenome.close()
gravar_nomeCompleto.close()