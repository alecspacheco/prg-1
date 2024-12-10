# crear el archivo libros.txt que guarde la infomracion correspondiente al libro como ser: titulo, autor, año de edicion, y cantidad de paginas. separado por comas. 
# crear el archivo, escribir dagtos en el archivo, mostrar los datos del archivo
import os

def crearArchivo():
  with open('libros.txt', 'w') as file:
    file.write('')
  print('Archivo creado')
  
def escribirDatos():
  titulo = input('Ingrese el titulo del libro: ')
  autor = input('Ingrese el autor del libro: ')
  anio = input('Ingrese el año de edicion del libro: ')
  paginas = input('Ingrese la cantidad de paginas del libro: ')
  with open('libros.txt', 'a') as file:
    file.write(f'{titulo},{autor},{anio},{paginas}\n')
  print('Datos agregados')
  
def mostrar():
  with open('libros.txt', 'r') as file:
    libros = file.readlines()
  for libro in libros:
    titulo, autor, anio, paginas = libro.split(',')
    print(f'Titulo: {titulo}, Autor: {autor}, Año de edicion: {anio}, Paginas: {paginas}')
def main():
  if not os.path.exists('libros.txt'):
    crearArchivo()
  while True:
    print('1. Agregar libro')
    print('2. Ver libros')
    print('3. Salir')
    opcion = input('Ingrese una opcion: ')
    if opcion == '1':
      escribirDatos()
    elif opcion == '2':
      mostrar()
    elif opcion == '3':
      break
    else:
      print('Opcion invalida')
main()