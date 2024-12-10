# crear un programa que permita al usuario almacenar los datos  de contactos(nombre, celular) Cada contacto, debe ir en una linea cuyos datos deben estar separados por comas

import os
def crearArchivo():
  with open('contactos.txt', 'w') as file:
    file.write('')
  print('Archivo creado')
def guardarRegistro():
  nombre = input('Ingrese el nombre del contacto: ')
  celular = input('Ingrese el celular del contacto: ')
  with open('contactos.txt', 'a') as file:
    file.write(f'{nombre},{celular}\n')
  print('Contacto agregado')
def mostrar():
  with open('contactos.txt', 'r') as file:
    contactos = file.readlines()
  for contacto in contactos:
    nombre, celular = contacto.split(',')
    print(f'Nombre: {nombre}, Celular: {celular}')
    
def main():
  if not os.path.exists('contactos.txt'):
    crearArchivo()
  while True:
    print('1. Agregar contacto')
    print('2. Ver contactos')
    print('3. Salir')
    opcion = input('Ingrese una opcion: ')
    if opcion == '1':
      guardarRegistro()
    elif opcion == '2':
      mostrar()
    elif opcion == '3':
      break
    else:
      print('Opcion invalida')
main()