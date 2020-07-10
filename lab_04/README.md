# Laboratório 4

Uma famosa olimpíada do conhecimento decidiu distribuir medalhas de ouro, prata e bronze aos seus participantes de acordo com faixas de notas. Esta medida não agradou a todos, pois é provável que a divisão de medalhas por tipo não seja uniforme. 
Além disso, corre-se o risco de não haver distribuição de um dado tipo de medalha...

Sua tarefa será escrever um programa em Python para ler as notas de corte, as notas dos participantes e calcular o número de medalhas a serem entregues. 
Você também deverá apresentar a maior nota obtida. **O uso de listas é opcional para a implementação da solução desta tarefa!**

## Descrição da entrada

Todas as notas serão consideradas no intervalo de 0 a 10, com uma casa decimal de precisão.

A primeira linha da entrada conterá a nota de corte para obtenção da medalha de ouro. Por exemplo, se a primeira linha contiver 9.0, todos os participantes que tiverem obtido nota no intervalo de 9.0 (inclusive) a 10 receberão medalha de ouro.

A segunda linha conterá a nota de corte para obtenção da medalha de prata. Continuando o exemplo anterior, se a primeira linha contiver 9.0 e a segunda 8.0, todos os participantes que tiverem obtido nota 8.0 (inclusive) a 8.9 (inclusive) receberão medalha de prata.

De maneira semelhante, a terceira linha conterá a nota de corte para a medalha de bronze.

As outras linhas conterão as notas obtidas pelos participantes da olimpíada. O valor -1 sinalizará o final da entrada. Exemplo:

9.0

8.0

7.0

8.5

9.5

9.0

6.9

-1

## Descrição da saída

As três primeiras linhas da saída indicarão o número de medalhas por tipo ou uma indicação que nenhum participante ganhou medalhas daquele tipo. As strings deverão ter o seguinte formato:

Medalha(s) de <tipo_medalha>: XX ou

Nenhum participante recebeu medalha de <tipo_medalha>!

A quarta linha indicará a maior nota lida, com uma string no formato:

Maior nota: <maior_nota>

A saída para a entrada fornecida na seção anterior será:

Medalha(s) de ouro: 2

Medalha(s) de prata: 1

Nenhum participante recebeu medalha de bronze!

Maior nota: 9.5    
