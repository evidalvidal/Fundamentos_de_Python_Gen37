# Vamos a calcular la diferencia entre dos años distintos

print("Calculadora de la diferencia entre años")

print("Para calcular adecuadamente, ingrese los años en el formato adecuado")


prim_a = int(input("Indica el año actual: "))
seg_a = int(input("Indica el año de tu elección: "))

while prim_a == seg_a :
    print("Error, introduce dos años distintos")
    prim_a = int(input("Indica el año actual: "))
    seg_a = int(input("Indica el segundo año: "))
    
    if prim_a > seg_a :
      print(f"Han pasado {prim_a-seg_a} años desde {seg_a}")

    elif prim_a < seg_a :
      print(f"Faltan {seg_a-prim_a} años para llegar al {seg_a}")
    
print("Gracias por ocupar esta calculadora, ¡hasta la próxima!")

input()

