# Laboratório 9

Esta tarefa é uma extensão da [tarefa anterior](https://github.com/juliaplazari/MC-102/tree/master/lab_09), em que será simulada a participação com múltiplas cartelas em um jogo de Bingo. 
A ideia é que você trabalhe agora com listas tridimensionais e veja a importância do uso de funções para estruturar o seu programa.

Os números sorteados durante o jogo deverão ser procurados e marcados, se for o caso, em todas as cartelas em que forem encontrados.

Em caso da formação de um padrão de Bingo em uma das cartelas, a mensagem BINGO! deverá ser emitida e o processamento dos números sorteados deverá ser encerrado.

##Descrição da entrada

A primeira linha conterá o número de cartelas. Em seguida, a entrada conterá cinco linhas para a descrição de cada cartela.

<n_cartelas>

< descrição_cartela0>    

...

< descrição_cartelan-1>

A próxima linha conterá a quantidade de números sorteados que deverão ser processados. Em seguida, os números virão um por linha no padrão <letra>-<numero>.

<m_numeros_sorteados>

<letra0>-<numero0>

...

<letram-1>-<numerom-1>

## Descrição da saída

Inicialmente, você deverá escrever as cartelas com a mesma moldura da tarefa anterior, uma ao lado da outra, como já ilustrado na primeira seção. Deve haver um espaço em branco entre cada cartela e não há espaço em branco após a última cartela.

Em seguida, deverá processar os números sorteados. Todo número lido deve ser escrito na saída e, caso tenha sido encontrado em alguma cartela, todas as cartelas deverão ser reescritas com XX no lugar da(s) ocorrência(s) do elemento sorteado. Caso uma linha, coluna ou diagonal tenha sido completada, a palavra BINGO é emitida e processamento termina, mesmo que existam mais números na entrada.


