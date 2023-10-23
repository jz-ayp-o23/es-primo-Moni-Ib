entrada = int(input("Introduzca un número: "))

# Proceso
residuo = 0
divisor = 1

while entrada > 1:
    divisor += 1
    if entrada % divisor == 0 and divisor not in entrada:
         print(f"El número {entrada} no es primo")
    else: 
        print(f"El número {entrada} sí es primo")