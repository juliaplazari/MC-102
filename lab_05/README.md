# Laboratório 5

#ilovepythoon ;-)

Em textos disponíveis na Internet é muito comum o uso de hashtags e emoticons. Um pesquisador da área de linguística está interessado em medir o quanto o uso destes elementos é importante para a interpretação destes textos. Para isso ele irá entregar os textos originais para um grupo de leitores e os mesmos textos sem emoticons e hashtags para outro grupo. Finalmente, ele irá comparar as impressões dos grupos sobre os textos.

Sua tarefa será escrever a versão inicial de um programa em Python para auxiliar o pesquisador a filtrar os textos. Adotaremos as seguintes regras simplificadas para a classificação dos elementos:

- **Palavras:** sequência de letras (sem acento).

Exemplos: UNICAMP algoritmos programacao

- **Números:** sequência de dígitos precedidos ou não do sinal negativo (-). Não trataremos números reais, complexos ou com pontos indicando a separação em grupos de três dígitos.

Exemplos: 2018 -100000

- **Hashtag:** caractere # seguido de letras.

Exemplos: #python #unicamp #amoviajar

- **Emoticons:** grupo de dois ou mais caracteres que não se enquadram nas descrições anteriores. São compostos principalmente por caracteres de pontuação, mas podem conter letras, números ou serem precedidos por #.

Exemplos: :-) #:-) :D <3

## Descrição da entrada

esta versão inicial, a entrada já virá pré-processada como uma sequência de N+1 linhas, com a primeira linha contendo o número N e as demais os elementos a serem classificados. Veja o exemplo abaixo:

5

#ilovepython

<3

happy

hacking

:-)

Note que uma entrada contendo apenas o número 0 é uma entrada válida.

## Descrição da saída

A saída conterá os elementos que foram classificados como palavras simples ou números seguida de um pequeno relatório do número de hashtags ou emoticons removidos, quando for o caso.

### Hashtags:

- Caso <h> > 1 hashtags tenham sido removidas, a seguinte mensagem deve ser emitida: <h> hashtags foram removidas.
- Caso apenas 1 hashtag tenha sido removida, a mensagem virá no singular: 1 hashtag foi removida.
- Não é necessário emitir mensagem caso nenhuma hashtag tenha sido removida.

## Emoticons:

- Caso <e> > 1 emoticons tenham sido removidos, a seguinte mensagem deve ser emitida: <e> emoticons foram removidos.
- Caso apenas 1 emoticon tenha sido removido, a mensagem virá no singular: 1 emoticon foi removido.
- Não é necessário emitir mensagem caso nenhum emoticon tenha sido removido.

Para a entrada usada como exemplo a saída será:

happy

hacking

1 hashtag foi removida.

2 emoticons foram removidos.







