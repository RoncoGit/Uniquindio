'''
Determine si una persona que ingrese los datos al aplicativo es apta o no para ingresar al Ejercito de colombia.

Datos para ingresar: Genero, Estatura, Edad, Estado Civil.

Condiciones ====> Genero? INDIFERENTE
                  Estatura? H > 165; M >160
                  Edad? H
'''
def leerString(texto):
    return input(texto)

def leerInt(texto):
    return int(input(texto))

def esApto (genero, estatura, edad, estadoCivil):
    if genero == "M":
        if estatura > 160:
            if edad > 20 and edad < 25:
                if estadoCivil == "Soltero":
                    return True
    else:
        if estatura > 165:
            if edad > 18 and edad <= 24:
                if estadoCivil == "Soltero":
                    return True
    return False

def main():
    genero = leerString("Ingrese su Genero (H o M): ")
    estatura = leerInt("Ingrese su estatura en cm's: ")
    edad = leerInt("ingrese su edad: ")
    estadoCivil = leerString("Ingrese su estado civil, así: Soltero (S). Casado (C). Union Libre (U): ")
    esAdmisible = esApto(genero, estatura, edad, estadoCivil)
    if esAdmisible == True:
        print("Usted es un candidato admisible")
    else:
        print("Usted NO es un candidato admisible")

main()