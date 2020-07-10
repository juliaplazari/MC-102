# Laboratório 9

Em um jogo de Bingo, os participantes recebem cartelas com 24 números distintos dispostos em uma matriz com 5 linhas e 5 colunas, sendo que o elemento central não recebe número. Os números da primeira coluna devem estar no intervalo de 1 a 15, da segunda, de 16 a 30, da terceira, de 31 a 45, da quarta, de 46 a 60 e da quinta, de 61 a 75. Além disto, a palavra BINGO costuma estar escrita no topo das cartelas de maneira a facilitar a identificação das colunas.

Durante o jogo, números são sorteados e anunciados juntamente com o identificador das colunas, como, por exemplo, B-02, I-17 ou G-54. Ao verificar que um número sorteado está em sua cartela, o jogador deve marcá-lo. Ganha prêmios quem completar com números sorteados uma linha, uma coluna ou uma das diagonais.

Sua tarefa será implementar um programa em Python para simular a participação de um jogador com uma única cartela em uma partida de Bingo.

## Descrição da entrada

As primeiras cinco linhas da entrada correspondem aos números da cartela. Para facilitar a leitura, o elemento central será marcado com XX.

12 24 43 49 72

07 23 31 57 62

04 20 XX 51 73

08 21 38 50 61

05 27 40 54 63

A próxima linha conterá a quantidade de números sorteados que deverão ser processados. Em seguida, os números virão um por linha no padrão <letra>-<numero>.

6

N-38

N-40

B-06

N-43

N-31

O-72

## Descrição da saída

Inicialmente, você deverá escrever a cartela com a moldura, o espaçamento e a palavra BINGO representada com nos exemplos da primeira seção. Em seguida, deverá processar os números sorteados. Todo número lido deve ser escrito na saída e, caso tenha sido encontrado na cartela, a cartela deve ser reescrita com XX no lugar do elemento sorteado. Caso uma linha, coluna ou diagonal tenha sido completada, a palavra BINGO é emitida e processamento termina, mesmo que existam mais números na entrada.

