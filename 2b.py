# automovil.txt datos: placa, marca, modelo y color. separados por comas.
import os

def crearArchivo():
  with open('automovil.txt', 'w') as file:
    file.write('')
  print('Archivo creado')

def escribirDatos():
  placa = input('Ingrese la placa del automovil: ')
  marca = input('Ingrese la marca del automovil: ')
  modelo = input('Ingrese el modelo del automovil: ')
  color = input('Ingrese el color del automovil: ')
  with open('automovil.txt', 'a') as file:
    file.write(f'{placa},{marca},{modelo},{color}\n')
  print('Datos agregados')
  
def mostrar():
  with open('automovil.txt', 'r') as file:
    autos = file.readlines()
  for auto in autos:
    placa, marca, modelo, color = auto.split(',')
    print(f'Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Color: {color}')
def main():
  if not os.path.exists('automovil.txt'):
    crearArchivo()
  while True:
    print('1. Agregar automovil')
    print('2. Ver automoviles')
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