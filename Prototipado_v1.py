impresoras = [
    ["Ultimaker 1", "LIBRE", ""],
    ["Ultimaker 2", "LIBRE", ""],
    ["Ultimaker 3", "LIBRE", ""],
    ["Ultimaker 4", "LIBRE", ""],
    ["Bambu Lab", "LIBRE", ""],
    ["Creativity", "LIBRE", ""]
]

print("\n=== Sistema de Impresoras 3D D-HIVE ===")
print("1. Ver estado de impresoras")
print("2. Solicitar impresora")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    for i in range(6):
        if impresoras[i][1] == "LIBRE":
            print(impresoras[i][0], ": DISPONIBLE")
        else:
            print(impresoras[i][0], ": OCUPADA por", impresoras[i][1], "(Código:", impresoras[i][2], ")")

elif opcion == "2":
    nombre = input("Ingrese su nombre: ")
    print("\nImpresoras disponibles:")
    libres = []
    for i in range(6):
        if impresoras[i][1] == "LIBRE":
            libres.append(i)
            print(len(libres), ".", impresoras[i][0])

    if len(libres) == 0:
        print("No hay impresoras libres")
    else:
        eleccion = int(input("Seleccione el número de impresora: ")) - 1
        idx = libres[eleccion]
        codigo = str((idx+1)*1111)
        impresoras[idx][1] = nombre
        impresoras[idx][2] = codigo
        print("Asignada", impresoras[idx][0], "a", nombre, "con código", codigo)

else:
    print("Opción no válida.")
