'''
Defina un programa que determine el mayor valor entre 3 números!!!
'''
def numMayor(num1, num2, num3):
    if num1 == num2 and num2 == num3 and num1 == num3:
        return "Todos los números son iguales."
    else:
        if num1 > num2:
            if num1 > num3:
                return num1
            else:
                return num3
        else:
            if num2 > num3:
                return num2
            else:
                return num3

def leerNum(texto):
    return int(input(texto))

def main():
    num1 = leerNum("Ingrese el primer Valor: ")
    num2 = leerNum("Ingrese el segundo valor: ")
    num3 = leerNum("Ingrese el tercer valor: ")    
    mayor = numMayor(num1, num2, num3)
    print("El mayor número entre los 3 valores ingresados es ", mayor)

main()
        