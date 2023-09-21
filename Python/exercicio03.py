## Programa que soma o valor entre 2 númerose e imprime o resutado.

## n1 = input('Digite um valor: ')
## Para saber qual a classe do numero ou mensagem, digitar print(type(conteúdo da variavel)).
## Exemplo: print(type(n1))

## Para que o resultado de uma classe seja exibida é preciso atribuir ela após o sinal de = da variavel.
##  Exempo: n1 = int(input('Digite um valor: '))  

## Para que dois valores inteiros sejam somados é necessário informar a classe antes do comando, caso contrário o terminal exibirá a junção deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
s = n1 + n2
print('O resultado entre {} e {} é: {}.'.format(n1, n2,s))