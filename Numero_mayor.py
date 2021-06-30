print("*****************************************************************************")
print("* Programa que determina ¿Qué número es el más grande de los tres números?. *")
print("***************************************************************************** \n")

num1 = int(input("Por favor introduce el primer número:"))
num2 = int(input("Por favor introduce el segundo número:"))
num3 = int(input("Por favor introduce el tercer número:"))

if  num1 > num2 and num1 > num3 :
    print("El número ", num1, "es el número mas grande de los tres.")
else:
    if num2 > num1 and num2 > num3 :
        print("El número ", num2, "es el número mas grande de los tres.")
    else:
        print("El número ", num3, "es el número mas grande de los tres.")
    
