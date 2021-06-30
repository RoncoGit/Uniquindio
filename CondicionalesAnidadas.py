print("================")
print("Conversor")
print("================ \n")

print("Menú de opciones: \n")

print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

conversor = int(input("¿Cuál es tu opción deseada?:"))

if conversor == 1:
    print("Conversor de Número a palabras. \n")
    num = int(input("¿Cual es el número que deseas convertir?:"))
    if num == 1:
        print("el número es 'uno'")
    elif num == 2:
        print("el número es 'dos'")
    elif num == 3:
        print("el número es 'tres'")
    elif num == 4:
        print("el número es 'cuatro'")
    elif num == 5:
        print("el número es 'cinco'")
    else:
        print("el número máximo de conversion es 5.")
elif conversor == 2:
    print("Conversor de palabras a números. \n")
    tex = input("¿Cual es la palabra que deseas convertir?:")
    tex = tex.lower()
    if tex == "uno" :
        print("el número es '1'")
    elif tex == "dos" :
        print("el número es '2'")
    elif tex == "tres" :
        print("el número es '3'")
    elif tex == "cuatro" :
        print("el número es '4'")
    elif tex == "cinco" :
        print("el número es '5'")
    else:
        print("el número máximo de conversion es cinco.")
else:
    print("Respuesta no válida. Intentalo de nuevo.")

print("Fin.")    
    


 
