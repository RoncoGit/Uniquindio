mensaje = "Hola"
mensaje += " "
mensaje += "Cristian"
print(mensaje)

print("Concatenación:")

mensaje = "hola"
espacio = " "
nombre = "Cristian"
print(mensaje+espacio+nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda:")

mensaje = "Hola Cristian"
buscar_subcadena = mensaje.find("Cristian")
print(buscar_subcadena)

print("Extracción:")

mensaje: "Hola Cristian"
extraer_subcadena = mensaje [1:8]
print(extraer_subcadena)

print("Comparación:")

mensaje_uno = "Hola"
mensaje_dos = "Hol"
print(mensaje_uno == mensaje_dos)
