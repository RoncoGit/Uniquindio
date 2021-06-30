print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, Introduce tu nombre:")

num_uno = int(input(nombre + " Cual es tu calificacion en matematicas:"))
num_dos = int(input(nombre + " Cual es tu calificacion en Quimica:"))
num_tres = int(input(nombre + " Cual es tu calificacion en Fisica:"))

promedio = (num_uno + num_dos + num_tres) / 3

if promedio >= 6 :
    print("Felicidades 'Pasaste tu materia satisfactoriamente' con un promedio de ", promedio)

print("Fin.")
    
