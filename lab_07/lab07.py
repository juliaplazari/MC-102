# MAC média aritmética das notas das atividades
# ML cada lab tem um peso
# MP: p1 tem peso 2, p2 tem peso 3

#notas atividades conceituais
ac = [float(x) for x in input().split()]
soma_ac = 0
for i in ac:
   soma_ac += i
m_ac = float(soma_ac/len(ac))

#notas lab
soma_l = 0
peso_l = 0
def tupla_float_int(x) :
    x = x[1:-1]       # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla

notas_lab = [tupla_float_int(x) for x in input().split()]
for i in range (0, len(notas_lab)):
    soma_l += notas_lab[i][0]*notas_lab[i][1]
    peso_l += notas_lab[i][1]
m_l = soma_l/peso_l

#notas provas
p = [float(x) for x in input().split()]
m_p = (p[0]*2 + p[1]*3)/5

#frequencia
freq = int(input())

#contas
m_exame = 0
if freq >= 75:
   if m_p >= 5 and m_l>= 5:
      m_elem = 0.6 * m_p + 0.3 * m_l + 0.1 * m_ac
      m_final = max(5, m_elem)
      resultado = str("Aprovado(a) por nota e frequencia.")
   elif m_p < 2.5 or m_l < 2.5:
      m_final = min(m_p, m_l)
      resultado = str("Reprovado(a) por nota.")
   else:
      m_exame = float(input())
      m_final = (min(m_p, m_l) + m_exame)/2
      if m_final >= 5:
         resultado = str("Aprovado(a) por nota e frequencia.")
      else:
         resultado = str("Reprovado(a) por nota.")
else:
   resultado = str("Reprovado(a) por frequencia.")
   m_final = min(m_p,m_l)
      
#saída
print ("Media das atividades conceituais: %.1f" % m_ac)
print ("Media das tarefas de laboratorio: %.1f" % m_l)
print ("Media das provas:", m_p)
if m_exame != 0:
   print ("Nota no exame:", m_exame)
print (resultado)
print ("Media final: %.1f" % m_final)
        

