import os

def crearArchivo():
  archivo = open("mercaderia.txt", "w")
  archivo.close()

def guardarRegistro():
  archivo = open("mercaderia.txt", "a")
  articulo = input("Ingrese el articulo: ")
  descripcion = input("Ingrese la descripcion: ")
  precio = input("Ingrese el precio: ")
  cantidad = input("Ingrese la cantidad: ")
  archivo.write(articulo + "," + descripcion + "," + precio + "," + cantidad + "\n")
  archivo.close()
  
def mostrar():
  archivo = open("mercaderia.txt", "r")
  for linea in archivo:
    print(linea)
  archivo.close()
  
def ListarPrecios():
  archivo = open("mercaderia.txt", "r")
  precio = int(input("Ingrese el precio maximo a mostrar: "))
  for linea in archivo:
    datos = linea.split(",")
    if int(datos[2]) < precio:
      print(linea)
  archivo.close()
  
def eliminar():
  archivo = open("mercaderia.txt", "r")
  nombre = input("Ingrese el nombre del articulo a eliminar: ")
  lineas = archivo.readlines()
  archivo.close()
  archivo = open("mercaderia.txt", "w")
  for linea in lineas:
    datos = linea.split(",")
    if datos[0] != nombre:
      archivo.write(linea)
  archivo.close()
  
def main():
  if not os.path.exists("mercaderia.txt"):
    crearArchivo()
  while True:
    print("1. Guardar registro")
    print("2. Mostrar registros")
    print("3. Listar precios")
    print("4. Eliminar registro")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
      guardarRegistro()
    elif opcion == 2:
      mostrar()
    elif opcion == 3:
      ListarPrecios()
    elif opcion == 4:
      eliminar()
    elif opcion == 5:
      break
    else:
      print("Opcion incorrecta")
      
main()