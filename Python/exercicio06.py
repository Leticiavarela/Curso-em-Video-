n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('O dobro de {} é {}.\nO triplo de {} é {}\nA raiz quadrada de {} é {:.3f}.'.format(n, d, n, t, n, r))
### Para que a execução fique mais organizada é importante colocar cada informação em uma linha.
### Para números flutuantes com resultados grandes adicionar limites de casas após o ponto usando :.a quantidade de casas f dentro das chaves.
### Para o código ficar mais limpo, as variáveis podem ser substituidas usando diretamente a função .format com as operações a serem executadas.