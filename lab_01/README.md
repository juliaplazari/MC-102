# Laboratório 1

O objetivo deste exercício é fazer a divisão em notas e moedas de um valor expresso em centavos de real, dando preferência para as notas ou moedas de maior valor. Utilizaremos notas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e moedas de R$ 1,00, R$ 0.50, R$ 0.25, R$ 0.10 e R$ 0.05.

Como exemplo, o valor 12.830 centavos pode ser dividido em uma nota de R$ 100,00, uma nota de R$ 20,00, uma nota de R$ 5,00, uma nota de R$ 2,00, uma moeda de R$ 1,00, uma moeda de R$ 0.25 e uma moeda de R$ 0.05.

## Entrada

O seu programa deverá ler um número inteiro. Este número deverá estar expresso apenas por dígitos, ou seja, sem pontos extras para separar grupos de três dígitos. Os valores serão mútiplos de 5. Observe o exemplo:

34185

## Saída

Para cada tipo de nota ou moeda enumerados anteriormente, será emitida uma linha indicando o número de notas ou moedas necessárias daquele tipo. Note que alguns valores podem ser iguais a zero.

Para o exemplo de entrada acima, a saída será:

3 nota(s) de R$ 100,00.

0 nota(s) de R$ 50,00.

2 nota(s) de R$ 20,00.

0 nota(s) de R$ 10,00.

0 nota(s) de R$ 5,00.

0 nota(s) de R$ 2,00.

1 moeda(s) de R$ 1,00.

1 moeda(s) de R$ 0,50.

1 moeda(s) de R$ 0,25.

1 moeda(s) de R$ 0,10.

0 moeda(s) de R$ 0,05.

## Dicas de Python 3

- Para ler um valor e armazená-lo como inteiro na variável x utilize os comandos input() e int():

x = int(input())

- Para obter o resultado da divisáo inteira de um número por outro utilize o operador //:

res_int = x // 100

- Para obter o resto da divisáo inteira de um número por outro utilize o operador %:

res_int = x % 100
