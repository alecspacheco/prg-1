
import os

def crearArchivo():
  archivo = open("deportistas.txt", "w")
  archivo.close()
  
def guardarRegistro(nombres, apellidos, celular, email, edad, disciplina):
  archivo = open("deportistas.txt", "a")
  archivo.write(nombres + "," + apellidos + "," + celular + "," + email + "," + edad + "," + disciplina + "\n")
  archivo.close()
  
  
def mostrar():
  archivo = open("deportistas.txt", "r")
  for linea in archivo:
    print(linea)
  archivo.close()
  
def modificar():
  nombre = input("Ingrese el nombre del deportista a modificar: ")
  apellido = input("Ingrese el apellido del deportista a modificar: ")
  archivo = open("deportistas.txt", "r")
  lineas = archivo.readlines()
  archivo.close()
  archivo = open("deportistas.txt", "w")
  for linea in lineas:
    if nombre in linea and apellido in linea:
      nuevo_celular = input("Ingrese el nuevo celular: ")
      datos = linea.strip().split(",")
      datos[2] = nuevo_celular
      archivo.write(",".join(datos) + "\n")
    else:
      archivo.write(linea)  
  
def eliminar():
  nombre = input("Ingrese el nombre del deportista a eliminar: ")
  apellido = input("Ingrese el apellido del deportista a eliminar: ")
  archivo = open("deportistas.txt", "r")
  lineas = archivo.readlines()
  archivo.close()
  archivo = open("deportistas.txt", "w")  
  for linea in lineas:
    if nombre in linea and apellido in linea:
      continue
    archivo.write(linea)
  archivo.close()
  
def main():
  if not "deportistas.txt" in os.listdir():
    crearArchivo()
    
  while True:
    print("1. Guardar registro")
    print("2. Mostrar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")
    opcion = int(input())
    
    if opcion == 1:
      guardarRegistro(input("Nombres: "), input("Apellidos: "), input("Celular: "), input("Email: "), input("Edad: "), input("Disciplina: "))
    elif opcion == 2:
      mostrar()
    elif opcion == 3:
      modificar()
    elif opcion == 4:
      eliminar()
    else:
      break
main()