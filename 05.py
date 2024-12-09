import os
def crearArchivo():
  archivo = open("estudiantes.txt", "w")
  archivo.close()
  
def guardarRegistro(ru, nombre, cursos):
  archivo = open("estudiantes.txt", "a")
  archivo.write(ru + "," + nombre + "," + cursos + "\n")
  archivo.close()

def mostrar():
  archivo = open("estudiantes.txt", "r")
  for linea in archivo:
    datos = linea.strip().split(",")
    print("Nombre: " + datos[1] + ", Cantidad de materias: " + str(len(datos[2].split("-"))))
  archivo.close()
  
def mayorCantidad():
  archivo = open("estudiantes.txt", "r")
  mayor = 0
  for linea in archivo:
    datos = linea.strip().split(",")
    if len(datos[2].split("-")) > mayor:
      mayor = len(datos[2].split(" "))
      nombre = datos[1]
  print("El estudiante con mayor cantidad de materias inscritas es: " + nombre + " con " + str(mayor) + " materias.")
  archivo.close()
  
def main():
  if not os.path.exists("estudiantes.txt"):
    crearArchivo()
  while True:
    print("1. Ingresar registro")
    print("2. Mostrar registros")
    print("3. Estudiante con mayor cantidad de materias inscritas")
    print("4. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
      ru = input("Ingrese el RU: ")
      nombre = input("Ingrese el nombre: ")
      cursos = input("Ingrese los cursos inscritos(separados por guiones): ")
      guardarRegistro(ru, nombre, cursos)
    elif opcion == "2":
      mostrar()
    elif opcion == "3":
      mayorCantidad()
    elif opcion == "4":
      break
    else:
      print("Opción inválida")
  
main()