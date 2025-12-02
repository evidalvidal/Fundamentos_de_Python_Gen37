#Programa para pedir contraseña al usuario

#Pediremos que el usuario ingrese datos personales que solamente serán visibles al momento en que ponga la contraseña de manera adecuada

print("Bienvenido, a continuación ingrese los siguientes datos:")

#Decretamos las dos variables que se utilizaran como contraseñas
Contra_uno = input("Ingrese una contraseña que comience con un número: ")

i = 0
# Ocupamos un índice en cero

while i == 0:

    if Contra_uno[i].isdigit() :
        Contra_dos = input("Confirme la contraseña: ")

        if Contra_dos == Contra_uno :
            print("¡Acceso concedido!")
  
        break #Salimos del bucle si la contraseña es la misma
   
    else: 
        print("La contraseña debe de comenzar con un número")
        Contra_uno = input("Indique una contraseña que comience con un número: ")

input()






