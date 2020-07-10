def divisao (d):

    nota_cem = d//10000
    d = d-d//10000 * 10000
    nota_cinq = d//5000
    d = d-d//5000 * 5000
    nota_vinte = d//2000
    d = d - d//2000 * 2000
    nota_dez = d//1000
    d = d-d//1000 * 1000
    nota_cinco = d//500
    d = d - d//500 * 500
    nota_dois = d//200
    d = d - d//200 * 200
    moeda_um = d//100
    d = d-d//100 * 100
    moeda_cinq = d//50
    d = d - d//50 * 50
    moeda_vinte_cinco = d//25
    d = d - d//25 * 25
    moeda_dez = d//10
    d = d - d//10 * 10
    moeda_cinco = d//5
    d = d - d//5 * 5

    print (str(nota_cem) + " nota(s) de R$ 100,00.")
    print (str(nota_cinq) + " nota(s) de R$ 50,00.")
    print (str(nota_vinte) + " nota(s) de R$ 20,00.")
    print (str(nota_dez) + " nota(s) de R$ 10,00.")
    print (str(nota_cinco) + " nota(s) de R$ 5,00.")
    print (str(nota_dois) + " nota(s) de R$ 2,00.")
    print (str(moeda_um) + " moeda(s) de R$ 1,00.")
    print (str(moeda_cinq) + " moeda(s) de R$ 0,50.")
    print (str(moeda_vinte_cinco) + " moeda(s) de R$ 0,25.")
    print (str(moeda_dez) + " moeda(s) de R$ 0,10.")
    print (str(moeda_cinco) + " moeda(s) de R$ 0,05.")

d = int(input("entre com o valor de d: "))
 
res = divisao (d)



