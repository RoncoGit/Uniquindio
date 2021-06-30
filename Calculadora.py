print("Calculadora con una sola variable \n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("""1. Suma
2. Resta
3. Multiplicación
4. División
5. División Entera
6. Exponente
7. Módulo o resto
""")

numero = int(input("Introduce la opción deseada:"))

if numero == 1 :
    print("Elegiste Suma \n")
    numero = int(input("Introduce el primer número:"))
    numero += int(input("Introduce el segundo número:"))
    print(" \n El resultado de la suma es:", numero)
elif numero == 2 :
    print("Elegiste Resta \n")
    numero = int(input("Introduce el primer número:"))
    numero -= int(input("Introduce el segundo número:"))
    print(" \n El resultado de la resta es:", numero)
elif numero == 3 :
    print("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer número:"))
    numero *= int(input("Introduce el segundo número:"))
    print(" \n El resultado de la Multiplicación es:", numero)
elif numero == 4 :
    print("Elegiste División \n")
    numero = int(input("Introduce el primer número:"))
    numero /= int(input("Introduce el segundo número:"))
    print(" \n El resultado de la división es:", round(numero, 2))
elif numero == 5 :
    print("Elegiste División Entera \n")
    numero = int(input("Introduce el primer número:"))
    numero //= int(input("Introduce el segundo número:"))
    print(" \n El resultado de la división entera es:", numero)
elif numero == 6 :
    print("Elegiste Exponencia \n")
    numero = int(input("Introduce el primer número:"))
    numero **= int(input("Introduce el segundo número:"))
    print(" \n El resultado de la exponencia es:", numero)
elif numero == 7 :
    print("Elegiste Módulo - Resto \n")
    numero = int(input("Introduce el primer número:"))
    numero %= int(input("Introduce el segundo número:"))
    print(" \n El resultado del módulo es:", numero)    
else:
    print("No ingresaste una opción válida.")
    
