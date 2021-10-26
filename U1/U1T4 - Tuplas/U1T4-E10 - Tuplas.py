# Ejercicio 10
# Compruebe si todos los elementos de la siguiente tupla son iguales

# tupla = (45, 45, 45, 45)
# Resultado:

# True

tupla = (45, 45, 45, 45)
igual = True

# a, b, c, d = tupla

# print(a==b==c==d)

for i in tupla:
    if i != tupla[0]:
        igual = False
        break
    
print(igual)
print(all(i == tupla[0] for i in tupla))