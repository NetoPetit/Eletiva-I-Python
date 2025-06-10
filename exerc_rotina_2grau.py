import math

def raiz_segundo_grau(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    
    if delta < 0:
        return f"Delta é {delta}, não existem raízes reais, pois o delta é menor que 0."

    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    if delta == 0:
        return f"Delta é igual a {delta}, a equação tem duas raízes reais e iguais, onde x1 = {x1} e x2 = {x2}."
    else:
        return f"Delta é igual a {delta}, a equação tem duas raizes reais diferentes, onde x1 = {x1} e x2 = {x2}."

resultado = raiz_segundo_grau(1, -4, 3)
print(resultado)