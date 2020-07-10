N_linhas = int(input())
h=0
e = 0
i = 1

while i <= N_linhas:
    i = i + 1
    s_i = str(input())
    if s_i.isdigit():
        print (s_i)
    elif s_i[0] == "-" and s_i[1:].isdigit():
        print (s_i)
    elif s_i[0] == "#" and s_i[1:].isalpha():
        h = h + 1
    elif s_i.isalpha():
        print (s_i)
    else:
         e = e + 1

if h == 1:
    print ("1 hashtag foi removida.")
elif h > 1:
    print (str(h) + " hashtags foram removidas.")
if e == 1:
    print ("1 emoticon foi removido.")
elif e > 1:
    print (str(e) + " emoticons foram removidos.")

        
