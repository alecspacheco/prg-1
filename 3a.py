class Paciente:
  def __init__(self, nombre, edad:int, genero, ci:int, celularReferencia:int):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
    self.ci = ci
    self.celularReferencia = celularReferencia
  def leerDatos(self):
    self.nombre = input('Ingrese el nombre del paciente: ')
    self.edad = int(input('Ingrese la edad del paciente: '))
    self.genero = input('Ingrese el genero del paciente: ')
    self.ci = int(input('Ingrese la cedula de identidad del paciente: '))
    self.celularReferencia = int(input('Ingrese el celular de referencia del paciente: '))
  def imprimirDatos(self):
    print(f'Nombre: {self.nombre}, Edad: {self.edad}, Genero: {self.genero}, CI: {self.ci}, Celular de referencia: {self.celularReferencia}')
    
def main():
  p1 = Paciente('','',0,'',0)
  p1.leerDatos()
  p1.imprimirDatos()
main()