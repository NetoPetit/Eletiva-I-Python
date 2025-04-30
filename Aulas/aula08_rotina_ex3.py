def bissexto(ano):

    if ano % 4 == 0:
        return True
    else:
        return False
    
ano = int(input("Ano: "))
if bissexto(ano):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")