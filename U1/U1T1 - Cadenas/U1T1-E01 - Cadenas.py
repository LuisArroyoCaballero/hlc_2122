# Ejercicio 1:
# Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena formada por los tres caracteres del medio de una 
# cadena determinada

# Dado :

# Caso 1
# str1 = "ChemTioaDur"
# Resultado
# Tio

# Caso 2

# str2 = "ChQueem"
# Resultado
# Que

cad = input("Introduzca una cadena de letras con un numero de letras impares y mayor que siete: ")
if (len(cad) >= 7 and len(cad) % 2 != 0):
    resultado = cad[int((len(cad)/2)-1):int((len(cad)/2)+2)]
    print(resultado)
else:
    print("Introduzca una cadena con las características requeridas")