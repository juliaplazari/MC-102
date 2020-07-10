lista = []
linha_1 = [str(x) for x in input().split()]
linha_2 = [str(x) for x in input().split()]
linha_3 = [str(x) for x in input().split()]
linha_4 = [str(x) for x in input().split()]
linha_5 = [str(x) for x in input().split()]
lista.append(linha_1)
lista.append(linha_2)
lista.append(linha_3)
lista.append(linha_4)
lista.append(linha_5)

bingo = 0

print ("""+----------------+
| B  I  N  G  O  |
+================+""")
print("| "," ".join(str(x) for x in linha_1), " |",sep="")
print("| "," ".join(str(x) for x in linha_2), " |",sep="")
print("| "," ".join(str(x) for x in linha_3), " |",sep="")
print("| "," ".join(str(x) for x in linha_4), " |",sep="")
print("| "," ".join(str(x) for x in linha_5), " |",sep="")
print("+----------------+")


N = int(input())
for a in range (0,N):
    if bingo != 0:
        break
    sorteio = input()
    sorteio.split()
    num = str(sorteio[2]+sorteio[3])
    print(sorteio)

    for i in range(5):
        for x in range(5):
            if lista[i][x] == num:
                lista[i][x] = "XX"

                print ("""+----------------+
| B  I  N  G  O  |
+================+""")
                print("| "," ".join(str(x) for x in linha_1), " |",sep="")
                print("| "," ".join(str(x) for x in linha_2), " |",sep="")
                print("| "," ".join(str(x) for x in linha_3), " |",sep="")
                print("| "," ".join(str(x) for x in linha_4), " |",sep="")
                print("| "," ".join(str(x) for x in linha_5), " |",sep="")
                print("+----------------+")
        if lista[i][0]==lista[i][1]==lista[i][2]==lista[i][3]==lista[i][4]:
            print("BINGO!")
            bingo += 1
        elif lista[0][i]==lista[1][i]==lista[2][i]==lista[3][i]==lista[4][i]:
            print("BINGO!")
            bingo += 1
        elif lista[0][0]==lista[1][1]==lista[2][2]==lista[3][3]==lista[4][4]:
            print("BINGO!")
            bingo += 1    
        elif lista[0][4]==lista[1][3]==lista[2][2]==lista[3][1]==lista[4][0]:
            print("BINGO!")
            bingo += 1
        if bingo != 0:
            break
            
            
           

          

            



        
        
            

            




        
