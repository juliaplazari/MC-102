# Laboratório 7

O critério de aprovação em MC102 é composto por vários itens com pesos diferentes. Nesta tarefa, vamos fazer um programa em Python para podermos calcular a média e situação final de um(a) aluno(a) com facilidade. O critério deste semestre é um pouco diferente do critério utilizado no semestre passado!

## Elementos componentes da avaliação

**Atividades conceituais:** são os questionários que podem ser respondidos via Moodle. A nota atribuída a cada uma destas atividades é uma nota de participação, calculada de maneira proporcional ao número de questões respondidas pelo(a) aluno(a), independentemente do fato de estarem corretas ou não. A média das atividades conceituais MAC será dada pela média aritmética simples das notas das atividades.

**Tarefas de laboratório:** são os programas desenvolvidos e entregues para correção automática no SuSy. Para compor a média dos laboratórios ML, cada tarefa tem um peso indicado no enunciado do laboratório.

**Provas teóricas:** são as avaliações aplicadas em sala de aula, sem consulta. Para compor a média de provas MP a primeira prova tem peso 2 e a segunda, peso 3.

## Resultado final

Considerando Freq a porcentagem de frequência às aulas, o resultado final será computado seguindo as regras abaixo:

### Caso Freq ≥ 75%:

- Caso MP ≥ 5 e ML ≥ 5:

Será calculada uma média ponderada dos elementos avaliativos:

MElem = 0.6 * MP + 0.3 * ML + 0.1 * MAC

O(A) aluno(a) estará aprovado(a) por nota e frequência com MFinal = max(5, MElem).

- Caso MP < 2.5 ou ML < 2.5:

O(A) aluno(a) estará reprovado(a) por nota com MFinal = min(MP, ML).

- Caso contrário:

O(A) aluno(a) deverá realizar o exame. Sua média final será MFinal = (min(MP, ML) + Exame)/2.

Caso MFinal ≥ 5.0 o(a) aluno(a) estará aprovado(a) por nota e frequência.

Caso contrário, estará reprovado(a) por nota.

### Caso Freq < 75%:

- O(A) aluno(a) estará reprovado(a) por frequência com MFinal = min(MP, ML).


## Descrição da entrada

A primeira linha da entrada conterá n valores nota_aci indicando as notas das atividades conceituais. A segunda linha conterá m tuplas (nota_labi, peso_labi) indicando a nota da tarefa de laboratório e seu respectivo peso para a média das tarefas de laboratório. A terceira linha conterá as notas das duas provas. A quarta linha conterá um valor entre 0 e 100 indicando a porcentagem da frequência às aulas. Caso o(a) aluno(a) precise fazer exame, haverá uma última linha contendo a nota obtida.

<nota_ac1> ... <nota_acn>

(<nota_lab00>, <peso_lab00>) ... (<nota_labm-1>, <peso_labm-1>)

<nota_prova1> <nota_prova2>

<freq>

<nota_exame>

## Descrição da saída

A primeira parte da saída conterá as médias das atividades conceituais, tarefas de laboratório e provas obtidas pelo(a) aluno(a), formatadas para apresentar apenas uma casa decimal (veja a seção Dicas):

Media das atividades conceituais: <MAC>

Media das tarefas de laboratorio: <ML>

Media das provas: <MP>

Caso o(a) aluno(a) tenha feito exame, a nota deve ser indicada:

Nota no exame: <Exame>

A situação final do(a) aluno(a) deve ser indicada por uma das strings abaixo:

Aprovado(a) por nota e frequencia.

Reprovado(a) por nota.

Reprovado(a) por frequencia.

Por último, a média final deve ser indicada:

Media final: <MFinal>

## Dicas de Python
- Para ler a linha com as notas das atividades conceituais e montar uma lista com elementos do tipo float você pode utilizar:

notas_ac = [float(x) for x in input().split()]

- Para imprimir a primeira nota formatada com uma casa decimal você pode usar:

print("Nota da primeira atividade conceitual:", format(notas_ac[0], ".1f"))

- Para ler a linha com as notas das tarefas de laboratório podemos utilizar uma abordagem semelhante, mas definindo uma função especial que retornará uma tupla com dois elementos, sendo o primeiro um float e o segundo um int.

def tupla_float_int(x) :
    
    x = x[1:-1]       # remove parênteses
    
    x = x.split(",")  # separa em duas strings
    
    f = float(x[0])   # converte primeiro elemento para float
    
    i = int(x[1])     # converte segundo elemento para int
    
    return (f,i)      # retorna tupla

notas_lab = [tupla_float_int(x) for x in input().split()]

- Para imprimir a nota do primeiro lab formatada com uma casa decimal e o peso você pode usar:

print("Nota do Lab00:", format(notas_lab[0][0], ".1f"))

print("Peso do Lab00:", notas_lab[0][1])


