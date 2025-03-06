print("Digite as coordenadas X e Y para saber em qual quadrante do plano cartesiano um ponto está localizado.")
coordenadaX = float(input("Digite a coordenada X: "))
coordenadaY = float(input("Digite a coordenada Y: "))

if coordenadaX > 0 and coordenadaY > 0 :
    print(f"O ponto ({coordenadaX}, {coordenadaY}) está no 1º quadrante, pois as duas coordenadas são positivas.")
elif coordenadaX < 0 and coordenadaY > 0 :
    print(f"O ponto ({coordenadaX}, {coordenadaY}) está no 2º quadrante, pois a coordenada X é negativa e a coordenada Y é positiva.")
elif coordenadaX < 0 and coordenadaY < 0 :
    print(f"O ponto ({coordenadaX}, {coordenadaY}) está no 3º quadrante, pois as duas coordenadas são negativas.")
elif coordenadaX > 0 and coordenadaY < 0 :
    print(f"O ponto ({coordenadaX}, {coordenadaY}) está no 4º quadrante, pois a coordenada X é positiva e a coordenada Y é negativa")
else :
    print("Coordenadas inválidas. \nFIM")