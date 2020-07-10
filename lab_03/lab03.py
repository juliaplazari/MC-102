o = input(str())
c = input(str())

if (o == "Q") or (o == "L") or (o == "C"):
    mlado = int(input())
    if (mlado<3):
        print ("Dimensao incorreta.")
    else:
        if (o == "Q"):
            print (mlado * c)
            for a in range (1, mlado-1,1):
                print (c," "*(mlado-2),c,sep="")
            print (mlado * c)

        if (o == "C"):
            print (" "*(mlado-1),mlado * c)
            for a in range (1, mlado-1,1):
                print (" "*mlado,c, " "*(mlado-2),c,sep="")
            print (c*mlado*3)
            for a in range (1, mlado-1, 1):
                print (c, " "*(mlado-2),c,c, " "*(mlado-2),c,c, " "*(mlado-2),c,sep="")
            print (c*mlado*3)
            for a in range (1, mlado-1,1):
                print (" "*mlado,c, " "*(mlado-2),c,sep="")
            print (" "*(mlado-1),mlado * c)

        if (o == "L"):
            print ((mlado-1)*" ",c,sep="")
            j = 1
            for a in range (1, mlado,1):
                print ((mlado-a-1)*" ",c," "*j,c,sep="")
                j = j + 2
            for a in range (1, mlado-1,1):
                print ((a)*" ",c," "*(j-4),c,sep="")
                j = j - 2
            print ((mlado-1)*" ",c,sep="")

        
elif (o == "R") or (o == "P"):
    mlargura = int(input())
    maltura = int(input())
    if (mlargura<3) or (maltura<3):
        print ("Dimensao incorreta.")
    else:
        if (o == "R"):
            print (mlargura * c)
            for a in range (1, maltura-1,1):
                print (c, " "*(mlargura - 2),c,sep="")
            print (mlargura * c)

        if (o == "P"):
            print (mlargura * c)
            for a in range (1, maltura-1,1):
                print(" "*(a),c," "*(mlargura - 2),c,sep="")
            print (" "*(maltura-1), mlargura * c,sep="")
    
else:
    print ("Objeto incorreto.")


    
    
        

        
    
    
