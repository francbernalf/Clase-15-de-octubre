"""
Realice un programa que lea por teclado un número entero positivo, y lo transforme a número binario (transforme el número base 10 a base 2). Por ejemplo: 12 ===> 1100.
"""
n = int(input("Ingrese un valor entero y positivo:"))

if n > 0:
    print (n)
dividendo = n
cociente = 0
resto = 0
valor = " "

while (dividendo != 0):
    cociente = dividendo//2
    resto = dividendo % 2
    dividendo = cociente
    valor += str (resto)
    
print(valor)