usuarios = {
    "estudiante1@ayed.com":"111222",
    "estudiante2@ayed.com":"333444",
    "estudiante3@ayed.com":"555666"
}

intentos = 3
while intentos >= 1:
    print("ingrese mail y contraseña")
    loginmail = input("Mail: ")
    loginpass = input("Contraseña: ")
    if loginmail in usuarios.keys() and loginpass == usuarios[loginmail]:
        print("Usuario y contraseña correctos")
        intentos = -1
    else:
        print("Usuario o contraseña incorrectos")
        intentos -= 1
        print("le quedan ",intentos," intentos")
if intentos == 0:
    print("Agoto los 3 intentos, el programa se cerrara.")

menu_1 = "c"
menu_2 = "c"
menu_3 = "c"
menu_4 = "c"
while menu_1 == "c":
    menu_principal = ""
    while menu_principal < "0" or menu_principal > "4": # Vuelve al menu principal siempre que el usuario marca una opcion no valida
        print("1- Gestionar mi perfil")
        print("2- Gestionar candidatos")
        print("3- Macheo")
        print("4- Reporte estadistico")
        print("0- Salir")
        menu_principal = input("Elige una opcion: ")
        if menu_principal < "0" or menu_principal > "4":
            print("Elige una opcion valida,", menu_principal, "no es una opcion valida")
    # El usuario marco una opcion valida, continua:

    if menu_principal == "1":
        menu_1 = ""
        while menu_1 < "a" or menu_principal > "c":
            print("--Gestionar mi perfil--")
            print("a- Editar mis datos Personales")
            print("b- Eliminar mi perfil")
            print("c- Volver")
            menu_1 = input("Elige una opcion: ")
            if menu_1 < "a" or menu_principal > "c":
                print("Elige una opcion valida,", menu_1, "no es una opcion valida")
        if menu_1 == "a":
            print("Edicion de datos personales")
            # codigo para Edicion de datos personales
        elif menu_1 == "b":
            # Codigo para eliminar perfil
            print("perfir eliminado")
        elif menu_1 == "c":
            volver = False
            # codigo para volver al menu principal

    if menu_principal == "2":
        menu_2 = ""
        while menu_2 < "a" or menu_principal > "c":
            print("--Gestionar candidatos--")
            print("a- Ver candidatos")
            print("b- Reportar un candidato")
            print("c- Volver")
            menu_2 = input("Elige una opcion: ")
            if menu_2 < "a" or menu_principal > "c":
                print("Elige una opcion valida,", menu_2, "no es una opcion valida")
        if menu_2 == "a":
            print("Ver candidatos")
            # codigo para ver candidatos
        elif menu_2 == "b":
            # Codigo para reportar un candidato
            print("Reportar un candidato")
        elif menu_2 == "c":
            volver = False
            # codigo para volver al menu principal

    elif menu_principal == "2":
        print("2")
    elif menu_principal == "3":
        print("3")
    elif menu_principal == "4":
        print("4")
    elif menu_principal == "0":
        print("0")


estudiante1_nombre = "estudiante1"
estudiante1_email = "estudiante1@ayed.com"
estudiante1_pass = "111222"
estudiante1_fecha_nac = "2006-01-01" #string en el formato YYYY-MM-DD
estudiante1_bio = "estudiante"
estudiante1_hobbie = "hobbie"

estudiante2_nombre = "estudiante2"
estudiante2_email = "estudiante2@ayed.com"
estudiante2_pass = "333444"
estudiante2_fecha_nac = "2006-01-02" #string en el formato YYYY-MM-DD
estudiante2_bio = "estudiante"
estudiante2_hobbie = "hobbie"

estudiante3_nombre = "estudiante3"
estudiante3_email = "estudiante3@ayed.com"
estudiante3_pass = "555666"
estudiante3_fecha_nac = "2006-01-03" #string en el formato YYYY-MM-DD
estudiante3_bio = "estudiante"
estudiante3_hobbie = "hobbie"