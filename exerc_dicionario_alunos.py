alunos_notas = {"Paulo" : [10, 8], "Pedro" : [5, 8], "João" : [10,10]}

for nome, notas in alunos_notas.items():
    media = sum(notas) / len(notas)
    print(f"{nome} tem média {media:.2f}")