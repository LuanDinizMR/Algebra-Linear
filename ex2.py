def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None # não há raízes reais
    
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)

    return x1, x2

print('Código por Luan Diniz Mazaro Rodovalho\n')
print('Segunda questão:\nDada uma matriz simétrica 2x2 calcule os autovetores e autovalores:\n')
while True:
    print('Insira uma matriz A simétrica 2x2: ')
    matriz = [[0,0],[0,0]]
    for i in range (0,2):
        for j in range (0,2):
            matriz[i][j]= int(input(f'Valor da posição a{i+1}{j+1}: '))

    trans = [[matriz[0][0],matriz[1][0]],[matriz[0][1], matriz[1][1]]]

    if matriz != trans:
        print('A matriz não é simétrica')
    else:
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
        
    resp = input('Deseja realizar outra operação? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
    
