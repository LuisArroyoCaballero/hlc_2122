# Ejercicio 7:
# Prueba de equilibrio de caracteres de cadena

# Asumiremos que una cadena s1 y s2 está equilibrada si todos los caracteres de s1 están en s2. la posición de los caracteres
# no importa.

# Dado:
# Caso 1:

# s1 = "hD"
# s2 = "ChemaDuran"
# Resultado:

# True
# Caso 2 :

# s1 = "hDf"
# s2 = "ChemaDuran"
# Resultado:

# Falso

s1 = "hDf"
s2 = "ChemaDuran"
comprobador = True

for i in s1:
    if s2.count(i) == 0:
        comprobador = False
        break

print(comprobador)