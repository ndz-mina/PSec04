#Romina_Mendoza-22438480

print('Respuestas de ejercicios de la práctica 1')

#Ejercicio_01: Remover String vacíos

Lista1 = ['gatos', '', 'perros', 'ratones', '']

Lista1.remove('')       #Método: .remove
Lista1.remove('')       #Método: .remove

print('1) ',Lista1)


#Ejercicio_02: Añadir un elemento 5000, luego del elemento 1000

Lista2 = [1, 2, [200, 400, [1000, 6000], 800], 30, 40]

Lista2[2][2].insert(1,5000)     #Método: .insert

print('2) ',Lista2)


#Ejercicio_03: Crear un string usando el primer, tercer y último elemento
#de un string dado

str = 'Después de la tempestad, viene la calma'

str_2 = str[0] + str[2] + str[-1]

print('3) str_2 = ',str_2)      #Hasta acá llegué yo en clase xD


#Ejercicio_04: Escribir un scrip para convertir la temperatura dada en C° a F

Temperatura_Centigrados = 20

T_F = (Temperatura_Centigrados * (9 / 5)) + 32

print('4) Temperatura_Farhrenheit = ',T_F)


#Ejercicio_05: Mezclar dos diccionarios en uno

dict1 = {'Diez':10, 'Veinte':20, 'Treinta':30}          #Dado
dict2 = {'Treinta':30, 'Cuarenta':40, 'Cincuenta':50}   #Dado

dict1.update(dict2)

print('5) ', dict1)


#Ejercico_06: Imprima el resultado de la clave o key "Historia"
#del diccionario dado:

diccionarioEstudiante = {
    'Clase': {
        'Estudiante': {
            'Nombre': 'Mike',
            'Marcas': {
                'Física': 70,
                'Historia': 80
            }
        }
    }
}

print('6) ', diccionarioEstudiante['Clase']['Estudiante']['Marcas'].get('Historia'))


#Ejercicio_07: Cambiar la fecha de nacimiento de Platón del año 427 A.C. al año 428 A.C.

dict = {'nombre': 'Platón', 'país': 'Antigua Grecia', 'fecha_de_nacimiento': -427,
'maestro': 'Sócrates', 'alumno': 'Aristótales'}

dict['fecha_de_nacimiento'] = -428

print('7) ',dict)