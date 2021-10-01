# Ejercicio 9:
# Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, ignorando todos los demás caracteres.


# Dado :

# str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
# Resultado:

# la suma es 294
# el promedio es 73.5

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
contador = 0
almacenSuma = 0

for i in str1.split(sep = " "):
    if (i.isdigit()):
        almacenSuma += int(i)
        contador += 1
        
print("La suma es "+str(almacenSuma))
print("El promedio es "+str(almacenSuma/contador))