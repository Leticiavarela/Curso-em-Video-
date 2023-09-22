n = int(input('Digite um número: '))
a = n - 1 
s = n + 1
print('O antecessor de {} é {}\nO sucessor de {} é {}.'.format(n, a, n, s))
### Nesse caso as variáveis > a e s < podem ser substituídas por (n-1) e (n+1) dentro do comando .format.
### Ficando:
### print('O antecessor de {} é {}\nO sucessor de {} é {}.'.format(n,(n-1),n,(n+1)))
