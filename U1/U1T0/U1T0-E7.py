# Ejercicio 7:
# Acepte tres cadenas cualquiera de una llamada input(). 
# Escriba un programa para tomar tres nombres como entrada de un usuario con una única llamada a función input().

cadena = ""

for i in range(3):
    cadena = cadena+input("Introduzca un nombre: ")+" "
    
print(cadena)