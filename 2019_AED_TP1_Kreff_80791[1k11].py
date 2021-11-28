# 2019_AED_TP1_Kreff_80791[1k11]_Apellido_Legajo[Curso]

# pequeño menu
print("Tienda de Indumentaria")
print("Para seleccionar un tipo de prenda eliga un nuemero entre 0 y 6")
print("0=Remeras, 1=Camisas, 2=Pantalones, 3=Faldas, 4=Vestidos, 5=Abrigos, 6=Calzado.")
print("Si La Prenda participadel programa SuperPuntos Escriba 'si' ")
print()
# Primera Prenda
print("Prenda N°1")
prenda1 = int(input("Ingrese Numero De Tipo De Prenda: "))
if prenda1 == 0:
    prenda1 = "Remera"
elif prenda1 == 1:
    prenda1 = "Camisa"
elif prenda1 == 2:
    prenda1 = "Pantalon"
elif prenda1 == 3:
    prenda1 = "Falda"
elif prenda1 == 4:
    prenda1 = "Vestido"
elif prenda1 == 5:
    prenda1 = "Abrigo"
elif prenda1 == 6:
    prenda1 = "Calzado"
else:
    print("Valor Ingresado NO Valido")

precio1 = float(input("Ingrese Precio: "))
superpun1 = input("Participa del Programa SupePuntos? : ")
puntos1 = 0
if superpun1 == "si":
    puntos1 = precio1

# Segunda Prenda


print("Prenda N°2")

prenda2 = int(input("Ingrese Numero De Tipo De Prenda: "))
if prenda2 == 0:
    prenda2 = "Remera"
elif prenda2 == 1:
    prenda2 = "Camisa"
elif prenda2 == 2:
    prenda2 = "Pantalon"
elif prenda2 == 3:
    prenda2 = "Falda"
elif prenda2 == 4:
    prenda2 = "Vestido"
elif prenda2 == 5:
    prenda2 = "Abrigo"
elif prenda2 == 6:
    prenda2 = "Calzado"
else:
    print("Valor Ingresado NO Valido")

precio2 = float(input("Ingrese Precio: "))
superpun2 = input("Participa del Programa SupePuntos? : ")
puntos2 = 0
if superpun2 == "si":
    puntos2 = precio2

# Tercera Prenda
print("Prenda N°3")
prenda3 = int(input("Ingrese Numero De Tipo De Prenda N°3: "))
if prenda3 == 0:
    prenda3 = "Remera"
elif prenda3 == 1:
    prenda3 = "Camisa"
elif prenda3 == 2:
    prenda3 = "Pantalon"
elif prenda3 == 3:
    prenda3 = "Falda"
elif prenda3 == 4:
    prenda3 = "Vestido"
elif prenda3 == 5:
    prenda3 = "Abrigo"
elif prenda3 == 6:
    prenda3 = "Calzado"
else:
    print("Valor Ingresado NO Valido")

precio3 = float(input("Ingrese Precio: "))
superpun3 = input("Participa del Programa SupePuntos? : ")
puntos3 = 0
if superpun3 == "si":
    puntos3 = precio3

# TOTAL A PAGAR SIN PROMO
totalsinpromo = precio1 + precio2 + precio3

# SuperPuntos

if superpun1 == superpun2 and superpun1 == superpun3:
    sumapuntos = (puntos1 + puntos2 + puntos3) * 2
else:
    sumapuntos = (puntos1 + puntos2 + puntos3) // 1

# Promos
prom1 = precio1
prom2 = precio2
prom3 = precio3
ahorro = 0

if prenda1 == prenda2 and prenda1 == prenda3:
    men = 0
    if prenda1 < prenda2 and prenda1 < prenda3:
        ahorro = precio1
        prom1 = men
    elif prenda2 < prenda3:
        ahorro = precio2
        prom2 = men

    else:
        ahorro = precio3
        prom3 = men


else:
    if prenda1 == prenda2:
        if precio1 < precio2:
            prom2 = precio2 // 2
            ahorro = prom2
        else:
            prom1 = precio1 // 2
            ahorro = prom1
    elif prenda1 == prenda3:
        if precio1 < precio3:
            prom3 = precio3 // 2
            ahorro = prom3
        else:
            prom1 = precio1 // 2
            ahorro = prom1
    elif prenda2 == prenda3:
        if precio2 < precio3:
            prom3 = precio3 // 2
            ahorro = prom3
        else:
            prom2 = precio2 // 2
            ahorro = prom2

# TOTAL A PAGAR CON PROMO
totalconpromo = prom1 + prom2 + prom3

# FORMA DE PAGO
pago = int(input("Ingrese Forma De Pago(1=Contado y 2=Tarjeta)"))

# Contado
manera = "Error"
total = 0
if pago == 1:
    manera = "Contado (10% descuento)"
    total = totalconpromo * 0.9

# Tarjeta

if pago == 2:
    cuotas = int(input("Ingrese En Cuantas Cuotas: "))
    if cuotas <= 3:
        manera = "Tarjeta 3 o Menos Cuotas (Recargo del 2%)"
        total = totalconpromo + (totalconpromo * 0.02)
    else:
        manera = "Tarjeta Mas de 3 Cuotas (Recargo del 5%)"
        total = totalconpromo + (totalconpromo * 0.05)

# Ticket
print("\033[1;34m" + "-------------------------------------------------------------")
print()
print("Ticket")
print("Tipo Precio SuperPuntos")
print(prenda1, "$", precio1)
print(prenda2, "$", precio2)
print(prenda3, "$", precio3)
print('Total sin promo $', totalsinpromo)
print("Ahorro $", ahorro)
print("Total con promo $", totalconpromo)
print("Forma de pago: ", manera)
print("Monto a pagar $", total)
print("Usted obtiene", sumapuntos, "SuperPuntos")
print()
print("\033[1;34m" + "-------------------------------------------------------------")
