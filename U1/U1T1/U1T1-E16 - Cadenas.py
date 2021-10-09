# Ejercicio 16:
# Eliminación de todos los caracteres que no sean enteros de una cadena

# Dado :
# str1 = 'Tengo 39 años y 10 meses'

# Resultado esperado :
# 3910

str1 = "Tengo 39 años y 10 meses"

for i in str1:
    if not i.isdigit():
        str1 = str1.replace(i, "")
        
print(str1)