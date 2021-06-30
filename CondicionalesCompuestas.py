print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cuál es tu nombre?:")

mat = int(input(nombre + "¡Cuál es tu calificación en matemáticas?:"))
qui = int(input(nombre + "¡Cuál es tu calificación en Química?:"))
fis = int(input(nombre + "¡Cuál es tu calificación en Física?:"))

promedio = (mat + qui + fis) / 3

if promedio >= 6 :
    print(nombre, "Felicidades, Aprobaste con una calificación de ", round(promedio,2))

else:
    print(nombre, "lastimosamente no aprobaste. Tu nota fue de ", round(promedio,2))
print("Fin.")
    
