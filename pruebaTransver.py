from random import randint as rd
import csv
import json
from os import system

# Datos de los trabajadores
Empleados = [
    "Juan Pérez","Maria Garcia","Carlos Lopez","Ana Martines","Pedro Rodriguez","Laura Hernandes","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandes"
]


# Funcion de validacion
def Validacion(rango):
    while True:
        try:
            variable = input("Digite una opcion: ")
            if variable.isdigit() and int(variable) in rango:
                variable = int(variable)
                return variable
        except ValueError:
            print("Digite una opcion valida")

                
# Funcion para randomizar los sueldos
def Randomizar(Info):
    system("cls")
    print("Randomizando sueldos...")

    DatosTrabajadores = []

    for traba in Info:
        Sueldos = rd(300000,2500000)
        Trabajadores = {}
        Trabajadores = {
            "Nombre":traba,
            "Sueldo":Sueldos
        }

        DatosTrabajadores.append(Trabajadores)

    return DatosTrabajadores


# Calificar sueldos 
def Calificar(Datos):
    system("cls")
    print("Calificando sueldos....\n")
    

    print("\nSueldos menores a $800.000")
    for cosas in Datos:
        if cosas["Sueldo"] < 800000:
            print(f"Empleado: {cosas["Nombre"]}  Sueldo: {cosas["Sueldo"]}")

    print("\nSueldos entre $800.000 y $2.000.000")
    for cosas in Datos:
        if cosas["Sueldo"] > 800000 and cosas["Sueldo"] < 2000000:
            print(f"Empleado: {cosas["Nombre"]}  Sueldo: {cosas["Sueldo"]}")

    print("\nSueldos sobre $2.000.000")
    for cosas in Datos:
        if cosas["Sueldo"] > 2000000:
            print(f"Empleado: {cosas["Nombre"]}  Sueldo: {cosas["Sueldo"]}")



# Funcion de estadisticas 
def estadisticas(datos):
    system("cls")
    while True:

        print("""

            Menu de estadisticas
              1. Sueldo mas alto y sueldo mas bajo
              2. Promedio de sueldos
              3. Media geometrica
              4. Volver

                """)
        opc = Validacion(range(1,5))

        if  opc == 1:
            sueldos = []

            for Cosas in datos:
                sueldos.append(Cosas["Sueldo"])

            sueldos.sort()
            print(f"El sueldo mas alto es: {sueldos[9]}")
            print(f"El sueldo mas bajo es: {sueldos[0]}")

        elif opc == 2:
            sueldosINT = 0
            
            for Cosas in datos:
                sueldosINT += Cosas["Sueldo"]
            resultado = sueldosINT/10

            print(f"El promedio de sueldo es: {resultado}")
        
        elif opc == 3:
            sueldosINT = 0
            
            for Cosas in datos:
                sueldosINT += Cosas["Sueldo"]
            resultado = sueldosINT/10
    

            print(f"La media geometrica es: {int(resultado)}")

        else:
            break


# Reporte de sueldos
def Reporte(Datos):
    system("cls")
        

    with open("Datos.csv", 'w') as Archivo:
        Escritor = csv.writer(Archivo)

        Escritor.writerow(["Nombre Empleado","Sueldo base","Descuento de salud","Descuento AFP","Sueldo liquido"])

        for Cosas in Datos:
            SueldoLiquido = Cosas["Sueldo"] - (Cosas["Sueldo"]/(100/7)) - (Cosas["Sueldo"]/(100/12))
            DescuentoSalud = (Cosas["Sueldo"]/(100/93))
            DescuentoAFP = (Cosas["Sueldo"]/(100/88))

            Escritor.writerows(
                [[Cosas["Nombre"], Cosas["Sueldo"], int(DescuentoSalud), int(DescuentoAFP), int(SueldoLiquido)]]
            )


# Main
def main(Empleados,):
    while True:
        print("""
        -----------------
              1. Asignar sueldos aleatorios
              2. Clasificar sueldos
              3. Ver estadisticas
              4. Reporte de sueldos
              5. Salir
            """)
        
        opc = Validacion(range(1,6))

        if opc == 1:
            Datos = Randomizar(Empleados)
        
        elif opc == 2:
            Calificar(Datos)
        
        elif opc == 3:
            estadisticas(Datos)

        elif opc == 4:
            Reporte(Datos)

        else:
            print("Finalizando programa.....")
            print("Creado por: Leandro Pedraza Rodriguez")
            print("Rut: 21.806.616-k")
            break

main(Empleados)
