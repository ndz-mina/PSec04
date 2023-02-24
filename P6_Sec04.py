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

            Name = input('Ingresar nombre: ')
            Description = input('Ingresar descripción del producto:\n')
            Price = input('Ingresar precio: ')

            if Price.isnumeric() and Name.isalpha():

                Price = eval(Price); Name = Name.capitalize(); Description = Description.capitalize()
                data = {}

                with open('text.json', 'r') as file:
                    data = json.load(file)

                    if data == {}:
                        new_data = {"Ferreteria": [{"Nombre": Name, "Descripcion": Description, "Precio": Price}]}

                        with open('text.json', 'w') as file:
                            json.dump(new_data, file, indent=4, sort_keys=True)

                    else:
                        data["Ferreteria"].append({
                            "Nombre": Name,
                            "Descripcion": Description,
                            "Precio": Price
                        })

                        with open('text.json', 'w') as file:
                            json.dump(data, file, indent=4)

            else:
                raise TypeError
            
            add_info = input('¿Agregará más información? (Sí/No):\n')
            add_info = add_info.lower()

else:
    raise ValueError
