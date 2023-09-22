## Programa que imprime e mostra seu tipo primitivo e outras informações sobre a mensagem.

usuario = input('Nome de usuario: ')
print(usuario, 'Está capitalizada? ', usuario.istitle())
print(usuario, 'Está em numérico? ', usuario.isnumeric())
print(usuario, 'É alfanumérico? ', usuario.isalnum())
print(usuario, 'É alfabético? ', usuario.isalpha())
print(usuario, 'Está em maiúsculo? ', usuario.isupper())
print(usuario, 'Esta em minusculo? ', usuario.islower())