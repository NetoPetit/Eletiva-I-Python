ler_alunos =  open("C:\\Users\\User\\Desktop\\ITE\\Sistemas de Informação\\2º Ano\\Eletiva\\Python\\alunos.txt", "r")
ler_notas = open("C:\\Users\\User\\Desktop\\ITE\\Sistemas de Informação\\2º Ano\\Eletiva\\Python\\notas.txt", "r")
gravar_notaAluno = open("C:\\Users\\User\\Desktop\\ITE\\Sistemas de Informação\\2º Ano\\Eletiva\\Python\\alunos_notas.txt", "w")
aluno = ler_alunos.readline()
nota = ler_notas.readline()
alunoNotas = gravar_notaAluno.write()
for i in range(len(aluno)):
    nome = aluno[i].strip()  # Remover espaços e quebras de linha
    notas_aluno = [float(nota) for nota in nota[i].strip().split(',')]  # Converter as notas para float
    
    # Calculando a média
    media = sum(notas_aluno) / len(notas_aluno)
    
    # Escrevendo o nome do aluno e a média no arquivo de resultado
    alunoNotas.write(f'{nome} {media:.2f}\n')
ler_alunos.close()
ler_notas.close()
gravar_notaAluno.close()