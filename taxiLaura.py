'''
Laura pide un taxi desde su casa al cine y ha pagado X por la carrera.
Si el taxi cobra Y por recogerla y Z por KM, ¿Cuál es la distancia recorrida?

Z = $500 por KM recorrido
X = $25.000 pagado por Laura
Y = $4.000 Banderazo

'''
def leerInt(texto):
    return int(input(texto))

def recorrido(km, ini, vlrFinal):
    return (vlrFinal - ini) / km

def main():
    Kilometros = 500
    banderazo = 4000
    vlrPagado = leerInt("Ingrese el valor final pagado: ")
    kmRecorrido = recorrido(Kilometros, banderazo, vlrPagado)
    print("La cantidad de Kilómetros recorridos en esta carrera fue de ", kmRecorrido, "Km's. ")
