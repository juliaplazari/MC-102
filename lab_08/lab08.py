from forca import lista_palavras, cenas_forca

number = int(input("Escolha um numero entre 0 e 49: "))
i = 0
a = 0
b = 0

if number in set(range (0,50)):
    word = lista_palavras[number]
    palavra = ["_" for i in range (len(word))]
    print("")
    print(cenas_forca[i])
    print("Palavra: ", "  ".join(str(x) for x in palavra),sep="")
    proxima_letra = input("Proxima letra: ")
    incorretas =[]

    while "_" in palavra:
        for x in range(0,len(str(word))):
            if proxima_letra == word[x]:
                palavra[x] = proxima_letra
        if proxima_letra in incorretas:
            print ("Voce jah escolheu esta letra.")
        if proxima_letra not in str(word) and proxima_letra not in incorretas:
            incorretas.append(proxima_letra)
            a = 1
            i += 1
        

        print("")
        print(cenas_forca[i])
        print("Palavra: ", "  ".join(str(x) for x in palavra),sep="")
        if a == 1:
            print("Tentativa(s) incorreta(s): "," ".join(str(x) for x in incorretas),sep="")
        
        if "_" not in palavra:
            print ("Palavra encontrada!")
            break
        elif i == 6:
            print ("Palavra oculta:", word)
            break
        else:
            proxima_letra = input("Proxima letra: ")
        if proxima_letra in palavra:
            print ("Voce jah escolheu esta letra.")
       

    
else:
    print("Numero invalido.")
