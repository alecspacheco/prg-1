
class Estudiante:
  def __init__(self, ru, apellidos, nombres, primerParcial:int, segundoParcial:int, tercerParcial:int):
    self.ru = ru
    self.apellidos = apellidos
    self.nombres = nombres
    self.primerParcial = primerParcial
    self.segundoParcial = segundoParcial
    self.tercerParcial = tercerParcial
  def leer(self):
    self.ru = input("Ingrese el registro universitario: ")
    self.apellidos = input("Ingrese los apellidos: ")
    self.nombres = input("Ingrese los nombres: ")
    self.primerParcial = int(input("Ingrese la nota del primer parcial: "))
    self.segundoParcial = int(input("Ingrese la nota del segundo parcial: "))
    self.tercerParcial = int(input("Ingrese la nota del tercer parcial: "))
  def mostrar(self):
    print("Registro universitario: ", self.ru)
    print("Apellidos: ", self.apellidos)
    print("Nombres: ", self.nombres)
    print("Primer parcial: ", self.primerParcial)
    print("Segundo parcial: ", self.segundoParcial)
    print("Tercer parcial: ", self.tercerParcial)
  def notaTotal(self):
    print(f"Nota total: {self.primerParcial + self.segundoParcial + self.tercerParcial}")
  def promedio(self):
    print(f"Promedio: {(self.primerParcial + self.segundoParcial + self.tercerParcial) / 3}")
    
def main():
  estudiante = Estudiante("", "", "", 0, 0, 0)
  estudiante.leer()
  estudiante.mostrar()
  estudiante.notaTotal()
  estudiante.promedio()
  
main()