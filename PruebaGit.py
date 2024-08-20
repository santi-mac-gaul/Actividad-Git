print("-"*26)
print("Bienvenido a mi programa Profe :D")
print("-"*26)

def agregar_alumno(datos_alumnos):
    nombre = input("ingrese el nombre del alumno: ")
    apellido = input("ingrese el apellido del alumno: ")
    DNi = int(input("ingrese el DNI del alumno (numerico): "))
    fecha_nacimiento = input("ingrese la fecha de nacimiento: ")
    tutor = input("ingrese el nombre del tutor: ")
    notas = (input("ingrese la notas del alumno (numerico y separadas por espacios): "))
    faltas = int(input("ingrese el total de faltas(numerico): "))
    amonestaciones = int(input("ingrese el total de amonestaciones(numerico): "))
    
    nuevo_alumno = {
        "Nombre": nombre, 
        "Apellido": apellido, 
        "DNI": DNi, 
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [float(nota) for nota in notas.split()], 
        "Faltas": faltas,
        "Amonestaciones": amonestaciones,   
    } 
    datos_alumnos[f"alumno{len(datos_alumnos)+ 1}"] = nuevo_alumno




def cambiar_datos(diccionario_alumnos):
    alumno_actualizado = input("Ingrese el nombre del alumno que desea actualizar: ")
    if alumno_actualizado in diccionario_alumnos:
        # Solicitar los nuevos datos del alumno
        nombre = input("Ingrese el nuevo nombre del alumno: ")
        apellido = input("Ingrese el nuevo apellido del alumno: ")
        DNI = int(input("Ingrese el nuevo DNI del alumno (numérico): "))
        fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento: ")
        tutor = input("Ingrese el nuevo nombre del tutor: ")
        notas = [float(nota) for nota in input("Ingrese las nuevas notas del alumno (numérico y separadas por espacios): ").split()]
        faltas = int(input("Ingrese el nuevo total de faltas (numérico): "))
        amonestaciones = int(input("Ingrese el nuevo total de amonestaciones (numérico): "))

        # Actualizar los datos del alumno
        diccionario_alumnos[alumno_actualizado] = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": DNI,
            "Fecha de nacimiento": fecha_nacimiento,
            "Tutor": tutor,
            "Notas": notas,
            "Faltas": faltas,
            "Amonestaciones": amonestaciones
        }
        print(f"Los datos del alumno {alumno_actualizado} han sido actualizados correctamente.")
    else:
        print(f"No se encontró al alumno {alumno_actualizado} en la lista.")
    print (diccionario_alumnos)

Alumnos = {

    "alumno1" : {    
        "Nombre": "Santiago",
        "Apellido": "Mac Gaul",
        "DNI": "46530686",
        "Fecha de nacimiento": "05/01/06",
        "Tutor": "Carolina Figueroa",
        "Notas": ["10","10","10","10"],
        "Faltas": "1",
        "Amonestaciones": "0",
        },
    "alumno2" : {
        "Nombre": "",
        "Apellido": "",
        "DNI": "",
        "Fecha de nacimiento": "",
        "Tutor": "",
        "Notas": "",
        "Faltas": "",
        "Amonestaciones": "",   
    } 
}
while True:
    opcion = ""
    if len(opcion) != 1 or opcion not in "abcd":
        print("Para poder usar el registro de datos elija entre estas opciones:")
        print("a) Mostrar datos de todos los alumnos")
        print("b) Registrar un nuevo alumno")
        print("c) Eliminar un alumno")
        print("d) Actualizar los datos de un alumno")
        print("e) Salir")
        opcion = input("Elija una opcion (a,b,c,d o e): ")
        if opcion == "a":
            print(Alumnos)
        if opcion == "b":
            agregar_alumno(Alumnos)
            print(Alumnos)
        if opcion == "c":
            print(Alumnos)
            alumno_eliminado = input("ingrese la clave del alumno que quiere eliminar: ")
            del(Alumnos[alumno_eliminado])
            print(Alumnos)
        if opcion == "d":
            print(Alumnos)
            alumno_actualizado = input("ingrese la clave del alumno del que quiera actualizar sus datos: ")
            Alumnos[alumno_actualizado] = cambiar_datos(Alumnos)
        if len(opcion) != 1 or opcion not in "abcde":
             print("solo puede elegir entre las opciones (abcd o e): ")
        elif opcion == "e":
            break   