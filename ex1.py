print('Código por Luan Diniz Mazaro Rodovalho\n')
print('Primeira Questão:\nColoque duas bases "B" e "C" e um vetor e receba a Matriz P e os Vetores vB e vC. ')
while True:
    print('Considerando a Base B = (v1,v2):')
    B = [[0,0], [0,0]]
    C = [[0,0], [0,0]]
    for i in range (0,2):
        for j in range (0,2):
            if i == 0:
                if j == 0:
                    B[i][j] = float(input(f'Digite o número v1x: '))
                else:
                    B[i][j] = float(input(f'Digite o númerov1y: '))
            else:
                if j == 0:
                    B[i][j] = float(input(f'Digite o número v2x: '))
                else:
                    B[i][j] = float(input(f'Digite o número v2y: '))

    print('Considerando a Base C = (w1,w2):')
    for i in range (0,2):
        for j in range (0,2):
            if i == 0:
                if j == 0:
                    C[i][j] = float(input(f'Digite o número w1x: '))
                else:
                    C[i][j] = float(input(f'Digite o número w1y: '))
            else:
                if j == 0:
                    C[i][j] = float(input(f'Digite o número w2x: '))
                else:
                    C[i][j] = float(input(f'Digite o número w2y: '))

    B_reserva = ((B[0][0],B[0][1]), (B[1][0], B[1][1]))  
    C_reserva = ((C[0][0],C[0][1]), (C[1][0], C[1][1])) 
    
    if ((B[0][0]==B[1][0] and B[0][1]==B[1][1]) or  (C[0][0]==C[1][0] and C[0][1]==C[1][1])):
        print('Os vetores que formam as bases devem ser diferentes')
    else:
        print('Considerando um vetor v = (x,y) na base C, adicione:') 
        x= float(input('x: '))
        y= float(input('y: '))

        detb = (B[0][0]*B[1][1])-(B[1][0]*B[0][1])
        if detb == 0:
            print('Determinante igual a 0, a matriz B não possui inversa')
        k=B[0][0]
        B[0][0] = B[1][1]
        B[1][1] = k
        B[1][0] = -B[1][0]
        B[0][1] = -B[0][1]
        B[0][0] = B[0][0]*(1/detb)
        B[1][0] = B[1][0]*(1/detb)
        B[0][1] = B[0][1]*(1/detb)
        B[1][1] = B[1][1]*(1/detb)

        P = [B[0][0]*C[0][0]+ B[1][0]*C[0][1], B[0][0]*C[1][0]+ B[1][0]*C[1][1], B[0][1]*C[0][0]+ B[1][1]*C[0][1], B[0][1]*C[1][0]+ B[1][1]*C[1][1]]

        VB = [P[0]*x + P[1]*y, P[2]*x + P[3]*y]

        print(f'P:| {P[0]}  {P[1]}  |\n |  {P[2]}  {P[3]} |')

        print(f'vB = ({VB[0]:.2f},{VB[1]:.2f})')
        print(f'vC = ({x:.2f},{y:.2f})')
    continuar = input('Deseja realizar outro teste?[S/N]: ').upper().strip()
    if continuar[0] == 'N':
        break
    
