# Tendencias e Innovacion en Tecnologia Agricola (TEA)
minutos = input(" minutosjugados? ")
valorPorMinuto = input(" valorporminuto?" )

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de las minutos juagadas
total = int(minutos) * float(valorPorMinuto)
print (total)
