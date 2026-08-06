Existem algumas formas de selecionar elementos nos scripts de frontend

*getElementById("id");#
*getElementByClass("class");.
*querySelector('.css');
*querySelector(".css")

O javascript é baseada na engine V8, sendo uma linguagem interpretada pelos navegadores e se quiser rodar ele fora da web é preciso do node.js que é um ambiente de execução de JavaScript gratuito e de código aberto e multiplataforma.

O let não pode ser redeclarado dentro de funçoes, diferente do var que pode existir tanto no escopo global e no escopo local dentro de funções.

A sintaxe básica de uma lista é:

*let alunos = ["Carlos","Alberto"]

E os dados da lista ficam dentro de colchetes [] e separa cada item com vírgulas

Para acessar a lista é preciso usar o conceito de index;

*alunos[0]

*alunos[1]

Os principais métodos e listas são:

1. Para adicionar ou remover itens<br>

*push() = Adiciona um item no final do elemento

*pop() = Remove o ultimo elemento

*shift() = Remove o primeiro elemento da lista

*unshift() = Adiciona um elemento no começo da lista

*splice() =  Pode adicionar ou remover elementos em qualquer posição da lista

*length() = Conta quantos itens tem dentro da lista

2. Para transformar ou Filtrar<br>

*map():Cria uma nova lista aplicando uma função a cada item

*filter(): Cria uma nova lista apenas com os itens que passam em um teste

*reduce(): Reduz uma lista a um único valor

*find(): retorna o primeiro item que satisfaz uma condição

*findIndex(): retorna o indice desse primeiro item

*includes(): Verifica se a lista contém um determinado valor (True ou False)