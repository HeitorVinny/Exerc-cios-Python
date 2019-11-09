'''
    programa 8
'''

import math

x1 = int(input("Na coordenada P, qual a posição de X1? "))
y1 = int(input("Na coordenada P, qual a posição de Y1? "))

x2 = int(input("Na coordenada Q, qual a posição de X2? "))
y2 = int(input("Na coordenada Q, qual a posição de Y2? "))

d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("A distância é: {:.1f}".format(d))

