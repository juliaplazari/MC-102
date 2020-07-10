
N = int(input()) #numero de cartelas
total = [] #lista gigante
bingo = 0
oi = 0

for i in range (1,N+1):
    lista_i = []
    linha_i_1 = [str(x) for x in input().split()]
    linha_i_2 = [str(x) for x in input().split()]
    linha_i_3 = [str(x) for x in input().split()]
    linha_i_4 = [str(x) for x in input().split()]
    linha_i_5 = [str(x) for x in input().split()] 
    lista_i.append(linha_i_1)
    lista_i.append(linha_i_2)
    lista_i.append(linha_i_3)
    lista_i.append(linha_i_4)
    lista_i.append(linha_i_5)
    total.append(lista_i)

print ("+----------------+ "*(N-1),end="")
print ("+----------------+")
print ("| B  I  N  G  O  | "*(N-1),end="")
print ("| B  I  N  G  O  |")
print ("+================+ "*(N-1),end="")
print ("+================+")
       
for i in range (0,N):
    print("|"," ".join(str(x) for x in total[i][0]), "|",end="")
    if i != (N-1):
        print(" ",end="")
print("\n",end="")
for i in range (0,N):
    print("|"," ".join(str(x) for x in total[i][1]), "|",end="")
    if i != (N-1):
        print(" ",end="")
print("\n",end="")
for i in range (0,N):
    print("|"," ".join(str(x) for x in total[i][2]), "|",end="")
    if i != (N-1):
        print(" ",end="")
print("\n",end="")
for i in range (0,N):
    print("|"," ".join(str(x) for x in total[i][3]), "|",end="")
    if i != (N-1):
        print(" ",end="")
print("\n",end="")
for i in range (0,N):
    print("|"," ".join(str(x) for x in total[i][4]), "|",end="")
    if i != (N-1):
        print(" ",end="")
print("\n",end="")
print("+----------------+ "*(N-1),end="")
print("+----------------+")

S = int(input()) #qtd de numeros sorteados
for a in range (0,S):
    if bingo != 0:
        break
    sorteio = input()
    sorteio.split()
    num = str(sorteio[2]+sorteio[3])
    print(sorteio)
    oi = 0
    
    for a in range(len(total)):
        for b in range(5):
            for x in range(5):
                if total[a][b][x] == num:
                    total[a][b][x] = "XX"
                    oi = 1

            if total[a][b][0]==total[a][b][1]==total[a][b][2]==total[a][b][3]==total[a][b][4]:
                bingo += 1
            elif total[a][0][b]==total[a][1][b]==total[a][2][b]==total[a][3][b]==total[a][4][b]:
                bingo += 1
            elif total[a][0][0]==total[a][1][1]==total[a][2][2]==total[a][3][3]==total[a][4][4]:
                bingo += 1    
            elif total[a][0][4]==total[a][1][3]==total[a][2][2]==total[a][3][1]==total[a][4][0]:
                bingo += 1

    if oi == 1:
        print ("+----------------+ "*(N-1),end="")
        print ("+----------------+")
        print ("| B  I  N  G  O  | "*(N-1),end="")
        print ("| B  I  N  G  O  |")
        print ("+================+ "*(N-1),end="")
        print ("+================+")

        for i in range (0,N):
            print("|"," ".join(str(x) for x in total[i][0]), "|",end="")
            if i != (N-1):
                print(" ",end="")
        print("\n",end="")
        for i in range (0,N):
            print("|"," ".join(str(x) for x in total[i][1]), "|",end="")
            if i != (N-1):
                print(" ",end="")
        print("\n",end="")
        for i in range (0,N):
            print("|"," ".join(str(x) for x in total[i][2]), "|",end="")
            if i != (N-1):
                print(" ",end="")
        print("\n",end="")
        for i in range (0,N):
            print("|"," ".join(str(x) for x in total[i][3]), "|",end="")
            if i != (N-1):
                print(" ",end="")
        print("\n",end="")
        for i in range (0,N):
            print("|"," ".join(str(x) for x in total[i][4]), "|",end="")
            if i != (N-1):
                print(" ",end="")
        print("\n",end="")
        print("+----------------+ "*(N-1),end="")
        print("+----------------+")

    if bingo != 0:
        print("BINGO!")
    if bingo != 0:
        break

     
           


