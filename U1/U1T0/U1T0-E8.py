# Ejercicio 8:
# Calcula la multiplicación y la suma de dos números. 
# Dados dos números enteros, devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.

n1 = input("Introduzca un primer número: ")
n2 = input("Introduzca un segundo número: ")

suma = int(n1) + int(n2)
multiplicacion = int(n1) * int(n2)

if multiplicacion > 1000:
    print(multiplicacion)
else:
    print(suma)