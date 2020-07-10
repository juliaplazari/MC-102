corte_ouro = float(input())
corte_prata = float(input())
corte_bronze = float(input())

o = 0
p = 0
b = 0
i = 1
n = 0
nota_i = float(input())
while nota_i != -1:
    i  = i + 1
    if (nota_i >= corte_ouro):
        o = o + 1
    elif (nota_i >= corte_prata):
        p = p + 1
    elif (nota_i >= corte_bronze):
        b = b + 1
    if (nota_i > n):
        n = nota_i
    nota_i = float(input())

if (o != 0):
    print(str("Medalha(s) de ouro: "),o,sep="")
else:
    print ("Nenhum participante recebeu medalha de ouro!")

if (p != 0):
    print (str("Medalha(s) de prata: "),p,sep="")
else:
    print ("Nenhum participante recebeu medalha de prata!")

if (b != 0):
    print (str("Medalha(s) de bronze: "),b,sep="")
else:
    print ("Nenhum participante recebeu medalha de bronze!")

print ("Maior nota: ",n,sep="")

    

    

        
    
