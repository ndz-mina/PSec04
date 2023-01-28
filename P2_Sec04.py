#Romina_Mendoza-22438480
#Francisco_Gorrin-19606845

print('Ésta calculadora hace operaciones de suma, resta y multiplicación:')

var1 = int(input('Ingrese un número: '))
var2 = input('Ingrese una operación a realizar (+, -, *): ')
var3 = int(input('Ingrese un número: '))

if var2 == '+':
    var4 = var1 + var3
    print('El resultado es: ',var4)
    
elif var2 == '-':
    var4 = var1 - var3
    print('El resultado es: ',var4)

elif var2 == '*':
    var4 = var1 * var3
    print('El resultado es: ',var4)

else : 
    print('Ésta operación no puede ser realizada.')