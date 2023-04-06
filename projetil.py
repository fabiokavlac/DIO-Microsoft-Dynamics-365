g = -10  # Aceleração da gravidade

# Solicita ao usuário a velocidade inicial, posição inicial e instante de tempo
v0 = float(input("Digite a velocidade inicial em m/s: "))
y0 = float(input("Digite a posição inicial em m: "))
t = float(input("Digite o instante de tempo em s: "))

# Calcula a posição final usando a fórmula dada
y = y0 + v0*t + (g*(t**2))/2

# Imprime a posição final
print(f"A posição final do projétil é {y:.2f} m.")

"""
Velocidade inicial em m/s = 300
Posição inicial em m = 300
Instante de tempo em s = 10
A posição final do projétil é 2800.00 m.
"""