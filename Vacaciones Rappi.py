print("*******************")
print("Compañía Rappi S.A.")
print("******************* \n")

print("Programa de cálculo de Vacaciones de empleados \n")

nombre = input("Ingresa tu nombre: ")
dependencia = int(input("\n Ingresa el número de tu clave: "))
antiguedad = int(input("\n Ingresa los años de antigüedad con Rappi S.A.: "))

if dependencia == 1:
    if antiguedad <= 1:
        print("\n", nombre, " posees actualmente 6 días de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("\n", nombre, " posees actualmente 14 días de vacaciones.")
    elif antiguedad >= 7:
        print("\n", nombre, " posees actualmente 20 días de vacaciones.")
    else:
        print("No ingresaste un dato válido.")

elif dependencia == 2:
    if antiguedad <= 1:
        print("\n", nombre, " posees actualmente 7 días de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("\n", nombre, " posees actualmente 15 días de vacaciones.")
    elif antiguedad >= 7:
        print("\n", nombre, " posees actualmente 22 días de vacaciones.")
    else:
        print("No ingresaste un dato válido.")

elif dependencia == 3:
    if antiguedad <= 1:
        print("\n", nombre, " posees actualmente 10 días de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("\n", nombre, " posees actualmente 20 días de vacaciones.")
    elif antiguedad >= 7:
        print("\n", nombre, " posees actualmente 30 días de vacaciones.")
    else:
        print("No ingresaste un dato válido.")
else:
    print("\n La Clave no existe.")    
    

