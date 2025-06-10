print("Verifique se um número é triângular.")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = num1 * num2 * num3

if num1.is_integer() and num2.is_integer() and num3.is_integer():
    print(f"O número {resultado} É triângular, os três números consecutivos {num1} x {num2} x {num3} são inteiros!")
else :
    print(f"O número {resultado} NÃO é triângular, os três números consecutivos {num1} x {num2} x {num3} NÃO são inteiros!")