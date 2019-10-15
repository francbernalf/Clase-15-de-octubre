"""
Realice un programa que lea por teclado un número entero positivo N. Debe asegurarse de que el número ingresado sea positivo. Luego muestre los primeros N números primos.
"""
n = -1 
while n < 0:
    n = int(input('Ingrese un valor entero y positivo N:'))
suma1 = 0
i = 2
while suma1 < n:
    suma2 = 0
    for a in range (2, i):
        if i%a == 0:
            suma2 += 1
    if suma2 == 0:
        suma1 += 1
        print (i)
    i += 1
    
print (suma1)