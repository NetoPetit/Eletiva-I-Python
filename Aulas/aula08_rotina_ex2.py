def media(nota):
    
    if nota >= 7:
        return "Aluno aprovado"
    elif nota >= 4 and nota <7:
        return "Aluno de exame"
    else:
        return "Aluno reprovado"

nota = float(input("Qual a nota do aluno: "))
sit = media(nota)
print(f"{sit}")