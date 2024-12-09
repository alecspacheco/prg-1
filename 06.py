
import os
def crearArchivo():
  archivo = open("personas.txt", "w")
  archivo.close()
  archivo = open("varones.txt", "w")
  archivo.close()
  archivo = open("mujeres.txt", "w")
  archivo.close()

def guardarRegistro(ci, apellido, nombre, sexo):
  archivo = open("personas.txt", "a")
  archivo.write(f"{ci},{apellido},{nombre},{sexo}\n")
  archivo.close()
  
def mostrar():
  archivo = open("personas.txt", "r")
  for linea in archivo:
    print(linea)
  archivo.close()
  
def separar():
  archivo = open("personas.txt", "r")
  varones = open("varones.txt", "w")
  varones.close()
  mujeres = open("mujeres.txt", "w")
  mujeres.close()
  for linea in archivo:
    datos = linea.split(",")
    if datos[3].strip() == "M":
      with open("varones.txt", "a") as varones:
        varones.write(linea)
    elif datos[3].strip() == "F":
      with open("mujeres.txt", "a") as mujeres:
        mujeres.write(linea)
  archivo.close()
  
def main():
  if not os.path.exists("personas.txt"):
    crearArchivo()
  while True:
    print("1. Guardar registro")
    print("2. Mostrar registros")
    print("3. Salir")
    opcion = int(input("Opción: "))
    if opcion == 1:
      ci = input("Ingrese CI: ")
      apellido = input("Ingrese Apellido: ")
      nombre = input("Ingrese Nombre: ")
      sexo = input("Ingrese Sexo (M/F): ")
      guardarRegistro(ci, apellido, nombre, sexo)
    elif opcion == 2:
      mostrar()
      separar()
    else:
      break
main()