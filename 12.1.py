"""
Realice un programa que lea por teclado un número entero positivo N. Debe asegurarse de que el número ingresado sea positivo. Luego calcule y muestre el factorial de los números desde 1 hasta N.
"""
n = int(input("Ingrese un valor entero y positivo N:"))

s = 0
f = 1
for i in range (1, n+1):
    f*= i
    s+= f
    
print (s)