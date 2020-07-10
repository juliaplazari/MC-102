# Laboratório 6

Em um campeonato de futebol, todos os times inscritos se enfrentam duas vezes: uma em seu estádio e outra no estádio adversário. O principal elemento para classificação é a **pontuação** acumulada: cada time recebe três pontos por vitória, um ponto por empate e zero ponto por derrota.

Em caso de empate, o desempate é feito por **número de vitórias**, **saldo de gols** (diferença entre o número de gols pró marcados e os gols sofridos por cada time) e **número de gols pró**. Caso os times permaneçam empatados em todos estes itens, ocupariam a mesma posição no campeonato. Nesta tarefa, no entanto, todos os testes levarão a um **único vencedor**.

## Descrição da entrada

A primeira linha da entrada indicará o número de times do campeonato e as linhas seguintes irão descrever os resultados das partidas. Uma partida será descrita em uma linha pelo nome e o número de gols pró do primeiro time, pelo caractere "x" e pelo nome e o número de gols pró do segundo time.

<numero_de_times>

<time_A> <gols_A> x <time_B> <gols_B>

<time_B> <gols_B> x <time_A> <gols_A>

<time_A> <gols_A> x <time_C> <gols_C>

<time_C> <gols_C> x <time_A> <gols_A> 

...

<time_B> <gols_B> x <time_C> <gols_C>

<time_C> <gols_C> x <time_B> <gols_B>

...     	

Exemplo:

3 

Ibis 0 x Cascavel 3

Cascavel 2 x Ibis 0

Ibis 0 x Dourados 1

Dourados 2 x Ibis 0

Cascavel 3 x Dourados 2

Dourados 3 x Cascavel 1  

## Descrição da saída

A saída conterá os resultados obtidos pelos times, apresentados em ordem alfabética de acordo com o padrão abaixo:

<nome_do_time> <pontuacao> <num_vitorias> <saldo_gols> <num_gols_pro>

A última linha conterá a string Vencedor: seguida do nome do vencedor.

Vencedor: <vencedor>

Para o exemplo da seção anterior, a saída será:

Cascavel 9 3 4 9

Dourados 9 3 4 8

Ibis 0 0 -8 0

Vencedor: Cascavel

## Dicas de Python

- Para separar os dados da partida, você pode utilizar a função split. Faça, por exemplo, o seguinte teste:
linha_entrada = input()

dados_partida = linha_entrada.split()

print("O time da casa", dados_partida[0], "marcou", dados_partida[1], "gols.")

print("O time visitante", dados_partida[3], "marcou", dados_partida[4], "gols.")    

- Para armazenar os dados dos times, você pode usar dicionários. Veja exemplos de algumas ações:

Inicia dicionário vazio: dic_times = {}

Verifica se um time está em um dicionário:
if "Ibis" in dic_times:
       print("Ibis faz parte dos times inscritos.")
 
Atribui dados a um elemento do dicionário. Suponha que a variável dados_time contém os dados que queremos armazenar:
dic_times["Araguaia"] = dados_time

Percorre os elementos de um dicionário em ordem alfabética:
for t in sorted(dic_times):
    print(t, ":", dic_times[t])	  




