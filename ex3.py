
from math import sqrt, atan, degrees
import matplotlib.pyplot as plt
import numpy as np


def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None # não há raízes reais
    
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)

    return x1, x2

print('Código por Luan Diniz Mazaro Rodovalho\n')
print('Terceira questão: dada uma seção conica descubra, os autovalores, os autovetores, identifique essa cônica, identifique o ângulo de rotação e a equação transformada em coordenadas x1 y1')
while True:
    print('Dada a seção conica Ax2 + Bxy + Cy 2 = F insira: ')
    A = float(input('A: '))
    B = float(input('B: '))
    C = float(input('C: '))
    F = float(input('F: '))

    matriz = [[A,B/2],[B/2,C]]

    #encontrando os autovetores eu autovalores
    lamb = bhaskara(1, -matriz[0][0]-matriz[1][1], (matriz[0][0]*matriz[1][1])-(matriz[1][0]*matriz[0][1]))
    print(f'Autovalores:\nλ1 = {lamb[0]}\nλ2 = {lamb[1]}')
    matriz1 = [[matriz[0][0]-lamb[0], matriz[0][1]],[matriz[1][0], matriz[1][1]-lamb[0]]]
    matriz2 = [[matriz[0][0]-lamb[1], matriz[0][1]],[matriz[1][0], matriz[1][1]-lamb[1]]]
    y1 = y2 =0 
    v1 = [(-matriz1[0][1]*1)/matriz1[0][0], 1]   
    v2 = [(-matriz2[0][1]*1)/matriz2[0][0], 1]  
    print('Autovetores:\nv1:')
    print(f'{(-matriz1[0][1]*1)/matriz1[0][0]}, 1') 
    print('v2:')
    print(f'{(-matriz2[0][1]*1)/matriz2[0][0]}, 1') 

    #identificação da conica
    D = [[lamb[0],0],[0,lamb[1]]]
    print(f'D:\n|{D[0][0]:.2f}  {D[0][1]:.2f}|\n|{D[1][0]:.2f}  {D[1][1]:.2f}|\n')
    if lamb[0] == 0:
        print(f'Parábola degeneráda dada pela equação:\n{lamb[1]}y²={F}')

    else:
        if lamb[1]>0:
            print(f'Elipse dada pela equação:\n{lamb[0]}x²+{lamb[1]}y²={F}')

        elif lamb[1]<0:
            print(f'Hipérbole dada pela equação:\n{lamb[0]}x²{lamb[1]}y²={F}')
        elif lamb[1]==lamb[0]:
            print(f'Hipérbole dada pela equação:\n{lamb[0]}x²+{lamb[1]}y²={F}')

        else:
            print(f'Parábola degenerada dada pela equação:\n{lamb[0]}x²={F}')

    #normalizando os autovetores
    u1 = sqrt((v1[0]**2)+(v1[1]**2))
    v1[0] = v1[0]*(1/u1)
    v1[1] = v1[1]*(1/u1)
    u2 = sqrt((v2[0]**2)+(v2[1]**2))
    v2[0] = v2[0]*(1/u2)
    v2[1] = v2[1]*(1/u2)

    
    print(f'Autovetores Normalizados:\n|{v1[0]:.2f}    {v2[0]:.2f}|    =   |cosθ   -senθ|\n|{v1[1]:.2f}     {v2[1]:.2f}|        |senθ    cosθ|')
    arcotg = atan(v1[1]/v1[0])
    print(f'\nÂngulo de rotação = {degrees(arcotg):.2f}°')

    x = np.linspace(-2, 2, 1000) # valores de x no intervalo de -2 a 2
    y = np.sqrt((F - lamb[0]*x**2) / lamb[1]) # calcular valores de y para cada valor de x
    plt.plot(x, y, label='Equação')
    plt.plot(x, -y, label='Equação')
    plt.show()
    resp = input('Deseja realizar outra operação? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
    