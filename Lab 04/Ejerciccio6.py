def calcularSalario(horas, tarifa):
    horas_extras = int(horas) - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMANALES * float(tarifa)) + (horas_extras * (float(tarifa)* 1.5))
    else:
        pago = int(horas) * float(tarifa)
    return pago

try: 
    MAX_HORAS_SEMANALES = 40
    horas = input("Ingrese número de horas: ")
    tarifa = input("Ingrese tarifa por hora: ")
    salario = calcularSalario(horas, tarifa)
    print(salario)
except:
    print("Error, debe ingresar un número")
    

