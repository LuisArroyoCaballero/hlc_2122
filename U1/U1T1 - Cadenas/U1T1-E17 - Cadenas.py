# Ejercicio 17:
# Encuentra palabras con alfabetos y números

# Dado :
# str1 = "Chema39 es profesor10 y maker"

# Resultado:
# Chema39 profesor10

str1 = "Chema39 es profesor10 y maker"
resultado = ""

str1 = str1.split(sep=" ")

def isAlphaNumeric(word):
    contNum = 0
    contChar = 0
    for i in word:
        if i.isalpha():
            contChar += 1;
        elif i.isdigit():
            contNum += 1;
        if contChar != 0 and contNum != 0:
            return True
        
    
for i in str1:
    if isAlphaNumeric(i):
        resultado += i+" "
    

print(resultado)
