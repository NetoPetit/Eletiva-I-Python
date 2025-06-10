print("Converta um horário composto por hora, minutos e segundos, em apenas segundos.")
hora = int(input("Digite a hora: "))
mi = int(input("Digite os minutos: "))
seg = int(input("Digite os segundos: "))

if hora >= 0 and hora <= 23 and mi >= 0 and mi <= 59 and seg >= 0 and seg <= 59 :
    conversao = (hora * 60 ** 2) + (mi * 60) + seg
    print(f"O horário {hora}:{mi}:{seg} convertido para segundos, são: {conversao} segundos.")
else: 
    print("Horário inválido \nFIM")