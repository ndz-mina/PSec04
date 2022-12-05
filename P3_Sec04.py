#Romina_Mendoza-22438480
#Francisco_Gorrin-19606845

n = 0
while n < 10:
    n += 1          # n = n + 1
    print(n)

N = input('Ingrese un valor numérico: ')
var = N.isnumeric()
if var:
    N = int(N)
    s = 0
    list = [0]
    while s <= (N - 1):
        s += 1
        list.append(s)              #Agregar un elemento al final de la lista
        sumatoria = sum(list)       #Sumar todos los elementos de la lista
    if s == 0:
        print(s)
    else:
        print(sumatoria)
else:
    print('Error. El valor ingresado no es un número entero.')