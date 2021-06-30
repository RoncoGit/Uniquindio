print("*************************")
print("* CÁLCULO MENSUALIDADES *")
print("*************************")

print("\n Escoge el programa a ofrecer:")
print("""1. A1
2. A1 - A2
3. A1 - B2.1
4. A1 - C1
5. A1 - C1 CON VERSANT \n""")

programa = int(input("Ingresa la opción requerida: "))


if programa == 1:
    abono = int(input("Ingresa el valor de tu abono inicial: $"))
    dto = int(input("\n Ingrese el porcentaje de descuento de esta transaccion: "))
    if dto > 0:
        vlrpro = int(1156257 - (1156257 * (dto / 100)))
        mensualidad = int(281000 - ((abono / vlrpro) * 281000))
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")
    else:
        mensualidad = int((abono / vlrpro) * 281000)
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")
elif programa == 2:
     abono = int(input("Ingresa el valor de tu abono inicial: $"))
    dto = int(input("\n Ingrese el porcentaje de descuento de esta transaccion: "))
    if dto > 0:
        vlrpro = int(1156257 - (1156257 * (dto / 100)))
        mensualidad = int(281000 - ((abono / vlrpro) * 281000))
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")
    else:
        mensualidad = int((abono / vlrpro) * 281000)
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")
elif programa == 2:
     abono = int(input("Ingresa el valor de tu abono inicial: $"))
    dto = int(input("\n Ingrese el porcentaje de descuento de esta transaccion: "))
    if dto > 0:
        vlrpro = int(1156257 - (1156257 * (dto / 100)))
        mensualidad = int(281000 - ((abono / vlrpro) * 281000))
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")
    else:
        mensualidad = int((abono / vlrpro) * 281000)
        print("con un abono de ", "$",abono, "el valor de tu mensualidad es de ", "$",mensualidad,".")        
