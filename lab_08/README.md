# Laboratório 8

No jogo da forca, o desafio é descobrir uma palavra oculta, tendo como dica o número de letras e podendo palpitar uma letra a cada vez. Para aumentar a emoção, a cada letra que não pertence à palavra, um membro de um boneco palito em uma forca é desenhado. O jogo termina se a palavra foi descoberta ou se o número máximo de tentativas foi atingido e o boneco está completo.

Para implementarmos o jogo, utilizaremos como base uma lista de cinquenta palavras que está armazenada no arquivo [forca.py](https://github.com/juliaplazari/MC-102/blob/master/lab_08/forca.py).

Neste mesmo arquivo, há um vetor cenas_forca com as cenas para cada situação do jogo em termos de palpites incorretos.

## Descrição da entrada e da saída

Nesta tarefa, adotaremos um modelo mais amigável para interação com o usuário e, por isso, a entrada e saída serão descritas na mesma seção.

Inicialmente, o seu programa deverá escrever a mensagem "Escolha um numero entre 0 e 49: ". Caso o número digitado não esteja dentro do intervalo, emitiremos a mensagem "Numero invalido." e o programa será encerrado.

Um número válido servirá para selecionarmos a palavra-desafio na lista.

Quando o usuário digitar uma letra incorreta como, o próximo cenário conterá uma linha extra com o registro das letras incorretas.

Se o usuário repetir uma tentativa, emitiremos a mensagem "Voce jah escolheu esta letra." e reapresentaremos o cenário, sem descontar esta tentativa do número máximo permitido.

O jogo prosseguirá neste esquema. Se o usuário não conseguir completar a palavra, o cenário conterá todas as tentativas incorretas, o boneco completo e a palavra que estava oculta.

Se o usuário conseguir completar, o cenário final conterá o boneco no estágio referente às tentativas incorretas, a palavra completa, as letras das tentativas incorretas e a mensagem "Palavra encontrada!".

## Dicas de Python

- Para utilizar as listas que estão definidas no arquivo forca.py escreva no início do arquivo lab08.py:

from forca import lista_palavras, cenas_forca

- Após o import, para imprimir o desenho referente a n_tentativas_incorretas escreva simplesmente:

print(cenas_forca[n_tentativas_incorretas])

- A palavra que está sendo construída pode ficar armazenada em uma lista de caracteres. Para iniciar uma lista de tamanho n com caracteres "_" escreva:

palavra = ["_" for i in range(n)]

- Para fazer uma leitura emitindo uma mensagem, observe os exemplos abaixo:

letra = input("Proxima letra: ")


