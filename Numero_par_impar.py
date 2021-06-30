print("*******************************************************")
print("* Programa que determina si un número es par o impar. *")
print("******************************************************* \n")

num = int(input("Por favor introduce un número entero:"))
resultado = (num % 2)

if  resultado == 0 :
    print("El número ", num, "es par.")

else:
    print("El número ", num, "es impar.")
    
