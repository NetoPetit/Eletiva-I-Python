print("Calculadora de IMC")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("\n|||RESULTADO|||\n")
if imc < 18.5 :
    print(f"Seu imc é {imc:.2f} e você está abaixo do peso.")
elif imc >= 18.5 and imc < 25 :
    print(f"Seu imc é {imc:.2f} e você está com peso normal.")
elif imc >= 25 and imc < 30 :
    print(f"Seu imc é {imc:.2f} e você está acima do peso.")
else :
    print(f"Seu imc é {imc:.2f} e você está obeso.")