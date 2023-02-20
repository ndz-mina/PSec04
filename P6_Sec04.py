import json

add = input('¿Agregará información? (Sí/No):\n')
add = add.lower()

if add == 'sí' or add == 'si' or add == 'no':

    if add == 'no':
        data = {}

        with open('text.json', 'r') as file:
            data = json.load(file)
            if data != {}:
                print(data)
            else:
                print('Archivo vacío.')

    else:
        add_info = add

        while add_info == 'sí' or add_info == 'si':

            ID = input('Ingrese número de C.I.: ')
            Name = input('Ingrese primer nombre: '); Name = Name.capitalize()
            Fullname = input('Ingrese primer apellido: '); Fullname = Fullname.capitalize()
            Note = input('Ingrese nota: ')

            new_student = {"Estudiantes": {"C.I.": [{ID: {"Nombre": Name, "Apellido": Fullname, "Nota": Note}}]}}

            if ID.isnumeric() and Name.isalpha() and Fullname.isalpha():

                data = {}
                with open('text.json', 'r') as file:
                    data = dict(json.load(file))
                    data = data.update(new_student)
                    data["C.I."].append(new_student)
                
                with open('text.json', 'w') as file:
                    json.dump(data, file, indent=4, sort_keys=True)

            else:
                raise TypeError
            
            add_info = input('¿Agregará más información? (Sí/No):\n')
            add_info = add_info.lower()

else:
    raise ValueError
