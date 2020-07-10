# Laboratório 3

Nesta tarefa, vamos praticar comandos repetitivos fazendo desenhos com caracteres ASCII. As formas irão variar de acordo com as dimensões estabelecidas e o caractere especificado para contorno. Observe os exemplos.

**Quadrado:** Deve ser desenhado o contorno de um quadrado, a partir da medida, em termos de número de caracteres, do lado deste quadradado.
- lado = 3:

***
* *
***

- lado = 7:
&&&&&&&
&     &
&     &
&     &
&     &
&     &
&&&&&&&

**Retângulo:* Deve ser escrito o contorno de um retângulo a partir da medida em número de caracteres da largura e altura deste retângulo.
- largura = 10, altura = 5:
&&&
& &
& &
& &
& &
& &
&&&

-largura = 5, altura = 5:
XXXXX
X   X
X   X
X   X
XXXXX

**Paralelogramo:** Deve ser escrito o contorno de um paralelogramo a partir da medida em número de caracteres da largura e altura deste paralelogramo. Observe que a inclinação da lateral do paralelogramo é de 1 caractere à direita por linha.
- largura = 4, altura = 3:
****
 *  *
  ****
  
- largura = 8, altura = 4:
########
 #      #
  #      #
   ########

**Losango:** Deve ser escrito o contorno de um losango a partir da medida em número de caracteres do lado deste losango.
- lado = 3:
 *
 * *
*   *
 * *
  * 
  
- lado = 6:
   @
    @ @
   @   @
  @     @
 @       @
@         @
 @       @
  @     @
   @   @
    @ @
     @
  
  
**Cruz:** Desenha uma cruz formada pela junção de 5 contornos de quadrados de mesmo tamanho de lado.     
- lado = 3:
   ***
   * *
*********
* ** ** *
*********
   * *
   ***
   
- lado = 5:
    XXXXX
     X   X
     X   X
     X   X
XXXXXXXXXXXXXXX
X   XX   XX   X
X   XX   XX   X
X   XX   XX   X
XXXXXXXXXXXXXXX
     X   X
     X   X
     X   X
     XXXXX

## Descrição da entrada:

Para todos os objetos será indicado:

<tipo_do_objeto>

<caractere> 

As letras que identificarão os tipos dos objetos serão as seguintes:

- Q: Quadrado
- R: Retângulo
- P: Paralelogramo
- L: Losango
- C: Cruz

Para os objetos Quadrado, Losango e Cruz deverá ser lida a medida do lado.

<medida_do_lado>

Para os objetos Retângulo e Paralelogramo deverão ser lidas as medidas da largura e da altura.

<medida_da_largura>

<medida_da_altura>

O valor para as dimensões deverá ser um número maior ou igual a 3.

Exemplo:

P

:

4

5

## Descrição da saída:
Caso a entrada tenha dados de acordo com a especificação, um desenho como os descritos na primeira seção deverá ser exibido. Para o exemplo de entrada fornecido, a saída será:

::::
 :  :
  :  :
   :  :
    ::::
    
**Importante:** Não acrescente caracteres em branco ao final das linhas!

Caso o tipo_do_objeto lido não corresponda a um dos elencados acima, deve ser emitida a mensagem Objeto incorreto.

Caso algum número lido seja menor do que 3, deve ser emitida a mensagem Dimensao incorreta. (propositalmente sem acentuação). Caso o tipo do objeto seja inválido, não é necessário ler ou verificar a validade das dimensões.




