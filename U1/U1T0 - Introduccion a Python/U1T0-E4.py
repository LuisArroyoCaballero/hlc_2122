# Ejercicio 4:
# Convierta un número decimal en octal usando print() con formato de salida.

# Dado: num = 8

# Resultado: El número octal del número decimal 8 es 10

numero = input("Introduzca un número: ")

cadena = "El número octal del número decimal {number} es {octNumber}".format(number = numero, octNumber = oct(int(numero)))

print(cadena)