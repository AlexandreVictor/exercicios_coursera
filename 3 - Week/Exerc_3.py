"""Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima
Buzz
se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada."""

vlr = int(input("Insira o número:"))
if(vlr%5==0):
    print("Buzz")
else:
    print(vlr)
