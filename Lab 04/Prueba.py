contador = 0
suma = 0
minimo = 0
maximo = 0
primeroNumero = True
while True:
    numero = input("ingrese un número: ")
    if (numero== "salir"):
        break
    contador = contador + 1
    suma = suma + int (numero)
    if (primeroNumero):
        minimo = int(numero)
        maximo= int(numero)
        primerNumero = False
    else:
        if (int(numero) > maximo):
            maximo = int(numero)
        if (int(numero) < minimo):
            minimo = int(numero)
print("contador:", contador)
print("suma", suma)
print("promedio:", suma/contador)
print("Mínimo:", minimo)
print("Máximo", maximo)
