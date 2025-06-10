print("Informe a data do seu aniversário para saber seu signo.")
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês numérico: "))

if dia >= 21 and mes == 3 or dia <= 20 and mes == 4 :
    print(f"Seu aniversário é {dia}/{mes} e seu signo é Áries")
elif dia >= 21 and mes == 4 or dia <= 20 and mes == 5 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Touro")
elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6 : 
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Gêmeos")
elif dia >= 21 and mes == 6 or dia <= 21 and mes == 7 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Câncer")
elif dia >= 22 and mes == 7 or dia <= 22 and mes == 8    :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Leão")
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Virgem")
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Libra")
elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Escorpião")
elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Sagitário")
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Capricórnio")
elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Aquário")
elif dia >= 20 and mes == 2 or dia <= 20 and mes == 3 :
    print(f"Seu aniversário é {dia}/{mes} e seu  signo é Peixes")
else :
    print("Data Inválida \nFim")