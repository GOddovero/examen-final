cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower()in vocales:
        contador +=1

print("Número de vocales en la cadena: ", contador)
