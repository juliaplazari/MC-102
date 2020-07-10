# Laboratório 2

A primeira questão da Prova I do primeiro semestre de 2018 foi a seguinte:
Maria e Marcos irão viajar e precisam escolher o destino da viagem. A filha deles, Carla, está muito ansiosa para ir para a praia! O casal percebeu que, para a família poder viajar, as seguintes condições devem ser atendidas:

- Carla não fica em recuperação. Em sua escola, a nota mínima para aprovação em cada matéria é 7!
- Maria e Marcos recebem autorização para tirar férias em dezembro.
- O 13° salário de Maria ou o 13° salário de Marcos são liberados antes do dia 11 de dezembro.
- O valor total da reserva do hotel e das passagens de avião é igual ou inferior a R$ 10.000.

|Nota ciências|Nota Mat.|Nota Port.|Férias Maria|Férias Marcos|13<sup>0</sup> Maria|13<sup>0</sup> Marcos|Valor hotel|Valor Passagem|
:---------: | :------: | :-------: |:---------: | :------: | :-------: |:---------: | :------: | :-------: |
|10|	10|	10	|Sim	|Sim	|01/12|	01/12|	R$ 3.000	|R$ 3.500|	
|9|	9|	9	|Sim	|Não	|05/12	|01/12	|R$ 4.000	|R$ 3.000|	
|8|	8	|8	|Sim	|Sim	|10/12	|11/12	|R$ 2.150	|R$ 7.800|	
|7|	7	|7	|Não|	Sim	|02/12	|09/12	|R$ 3.450	|R$ 6.250|	
|6.9|	7|	8|	Sim	|Sim	|25/12	|03/12	|R$ 2.750	|R$ 4.250|	
|7|	7|	7	|Sim|	Sim|	12/12	|08/12	|R$ 4.500	|R$ 5.500|	
|7.5|	7.4|	7.3|	Não|	Não	|02/12	|08/12	|R$ 5.500	|R$ 4.500|	
|6.9|	10|	10|	Sim|	Sim|	04/12|	05/12	|R$ 1.500	|R$ 3.300|	
|9.1|	9.2|	7.9|	Sim	|Sim|	11/12|	11/12	|R$ 3.200	|R$ 4.800|	
|7	|7	|7.1|	Sim|	Sim|	11/12|	10/12	|R$ 3.208	|R$ 6.792|

Sua tarefa será implementar uma programa em Python que irá ler dados semelhantes aos da tabela e indicar se a família vai ou não viajar. Em caso negativo, uma explicação deve ser exibida.

## Entrada
O seu programa deverá ler os seguintes dados, um elemento por linha:

- três números tipo float referentes às notas da Carla.
- duas strings Sim ou Nao referentes à aprovação das férias de Maria e Marcos.
- dois inteiros correspondentes aos dias em dezembro em que o 13° salário de Maria e o de Marcos foram liberados.
- dois números tipo float indicando os valores do hotel e das passagens.

Veja o exemplo abaixo:

10

9.0

7.5

Sim

Sim

7

11

4000.00

7000.00

## Saída
Seu programa deverá imprimir uma das saídas abaixo:

- SIM!!!
- NAO. As notas da Carla nao foram suficientes.
- NAO. O casal nao esta de ferias.
- NAO. Nenhum 13o salario foi liberado a tempo.
- NAO. O valor total e muito alto.

Para o exemplo apresentado na seção Entrada, a saída será:

NAO. O valor total e muito alto.

Caso a família não possa seguir viagem por mais de uma razão, apenas a primeira condição falsa seguindo a ordem estabelecida no enunciado precisa ser reportada. Por exemplo, se nenhum 13°o foi liberado a tempo e o valor total é muito alto, apenas a string sobre o 13° salário deve ser exibida.

