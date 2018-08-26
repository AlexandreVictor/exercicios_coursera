"""Receba 3 números inteiros na entrada e imprima 
 - > crescente
    se eles forem dados em ordem crescente. Caso contrário, imprima
 - > não está em ordem crescente"""
vlr_0 = int(input("Insira o número:"))
vlr_1 = int(input("Insira o número:"))
vlr_2 = int(input("Insira o número:"))

if(vlr_0<=vlr_1 and vlr_1<=vlr_2):
    print("Crescente")
else:
    print("Não está em ordem crescente")