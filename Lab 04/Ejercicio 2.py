def mostrarmenor(m):
    print('\nEl numero menor es: ',m)

def mostrarmayor(M):
    print('\nEl numero mayor es: ',M)

def pedirdato():
    menor=None
    mayor=None
    while True:
        n=input('Ingrese un numero: ')
        if n=='fin':
            break
        try:
            n = int(n)
        except:
            print('\nError!! Ingrese un numero o la palabra "fin".\nEl programa ha finalizado')
            quit()

        if mayor is None or n>mayor:
            mayor=n
        if menor is None or n<menor:
            menor=n
    mostrarmayor(mayor)
    mostrarmenor(menor)

pedirdato()
