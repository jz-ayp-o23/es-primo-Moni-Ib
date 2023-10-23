"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones

#Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
divisor = 2

while divisor < entrada:
    if entrada % divisor == 0 and divisor != entrada:
        print(f"El número {entrada} no es primo")
        divisor = entrada  
    divisor += 1
else:
    print(f"El número {entrada} sí es primo")




