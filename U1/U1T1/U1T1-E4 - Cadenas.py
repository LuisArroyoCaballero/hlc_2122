# Ejercicio 4:
# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice los caracteres de tal manera que todas las 
# letras minúsculas deben ir primero.

# Dado :
# str1 = ChEmaDUraN

# Resultado:
# hmaraCEDUN

str1 = "ChEmaDUraN"
mayus = ""
minus = ""

for i in str1:
    if (i.isupper()):
        mayus += i
    elif (i.islower()):
        minus += i

print(minus+mayus)