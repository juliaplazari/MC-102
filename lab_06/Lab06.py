n = int(input())
i = 1
dic = {}
pts = 0
win = 0
saldo = 0
gols = 0

while i <= (n*(n-1)):
    entrada = input()
    dados = entrada.split ()

    if str(dados[0]) not in dic:
        dic[str(dados[0])] = [pts,win,saldo,gols]
    if str(dados[3]) not in dic:
        dic [str(dados[3])] = [pts,win,saldo,gols]

    if dados[1] > dados[4]:
        dic[str(dados[0])][0] += 3
        dic[str(dados[0])][1] += 1
        dic[str(dados[0])][2] += int(dados[1])-int(dados[4])
        dic[str(dados[0])][3] += int(dados[1])
        dic[str(dados[3])][2] += int(dados[4])-int(dados[1])
        dic[str(dados[3])][3] += int(dados[4])
    if dados[4] > dados[1]:
        dic[str(dados[3])][0] += 3
        dic[str(dados[3])][1] += 1
        dic[str(dados[0])][2] += int(dados[1])-int(dados[4])
        dic[str(dados[0])][3] += int(dados[1])
        dic[str(dados[3])][2] += int(dados[4])-int(dados[1])
        dic[str(dados[3])][3] += int(dados[4])
    if dados[1] == dados[4]:
        dic[str(dados[0])][0] += 1
        dic[str(dados[3])][0] += 1
        dic[str(dados[0])][2] += int(dados[1])-int(dados[4])
        dic[str(dados[0])][3] += int(dados[1])
        dic[str(dados[3])][2] += int(dados[4])-int(dados[1])
        dic[str(dados[3])][3] += int(dados[4])
        
    i += 1

a = 0
b = 0
c = 0
d = 0


for t in sorted(dic):
        if dic[t][0] > a:
            a = dic[t][0]
            b = dic[t][1]
            c = dic[t][2]
            d = dic[t][3]
            vencedor = t
        elif dic[t][0] == a:
            if dic[t][1] > b:
                b = dic[t][1]
                c = dic[t][2]
                d = dic[t][3]
                vencedor = t
            elif dic[t][1] == b:
                if dic[t][2] > c:
                    c = dic[t][2]
                    d = dic[t][3]
                    vencedor = t
                elif dic[t][2] == c:
                    if dic[t][3] > d:
                        d = dic[t][3]
                        vencedor = t

                        
for t in sorted(dic):
    print(t, " ".join(str(x) for x in dic[t]))
print ("Vencedor:", vencedor)
