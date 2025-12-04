# Programa para pedir contraseña al usuario

print("Bienvenido, a continuación ingrese los siguientes datos:")

# Solicitamos la contraseña
while True:
    contra_uno = input("Ingrese una contraseña que comience con un número: ")
    
    if not contra_uno:  # Verifica si la entrada está vacía
        print("La contraseña no puede estar vacía. Intente nuevamente.")
        continue
    
    if contra_uno[0].isdigit():
        contra_dos = input("Confirme la contraseña: ")
        
        if contra_uno == contra_dos:
            print("Su contraseña ha sido creada con éxito. Bienvenido al sitio")
            break
        else:
            print("Las contraseñas no coinciden. Intente nuevamente.")
    else:
        print("Contraseña no válida: debe comenzar con un número.")
        
input("Presione Enter para salir...")