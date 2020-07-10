#condições
    #nota minima 7 em todas as matérias
    #Maria E Marcos conseguem férias
    #o 13 salario de um dos dois é liberado antes do dia 11
    # Hotel + passagem < 10.000



science = float(input( ))
math = float(input( ))
port = float(input( ))

ferias_Maria = input(str( ))
ferias_Marcos = input(str( ))

money_Maria = int(input( ))
money_Marcos = int(input( ))

passagem = float(input())
hotel = float(input())
dinheiro = passagem + hotel

if (science > 7 and math > 7 and port > 7 and ferias_Maria == "Sim" and ferias_Marcos == "Sim" and (money_Maria < 11 or money_Marcos < 11) and dinheiro <= 10000.00):
        print ("SIM!!!")
elif (science < 7) or (math < 7) or (port < 7):
    print("NAO. As notas da Carla nao foram suficientes.")
elif (ferias_Maria == "Nao" or ferias_Marcos == "Nao"):
    print ("NAO. O casal nao esta de ferias.")
elif (money_Maria >= 11 and money_Marcos >= 11):
    print ("NAO. Nenhum 13o salario foi liberado a tempo.")
elif dinheiro > 10000:
    print ("NAO. O valor total e muito alto.")
else:
        print ("SIM!!!")
    


    
