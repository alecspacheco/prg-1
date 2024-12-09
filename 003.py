
class Empleado:
  def __init__(self, ci, nombre, salario:float, cargo):
    self.ci = ci
    self.nombre = nombre
    self.salario = salario
    self.cargo = cargo
  def leer(self):
    self.ci = int(input("Introduce tu CI: "))
    self.nombre = input("Introduce tu nombre: ")
    self.salario = float(input("Introduce tu salario: "))
    self.cargo = input("Introduce tu cargo: ")
    
  def mostrar(self):
    print("CI: ", self.ci)
    print("Nombre: ", self.nombre)
    print("Salario: ", self.salario)
    print("Cargo: ", self.cargo)
  def calcularSalario(self, aumento):
    self.salario = self.salario + (self.salario * aumento / 100)
    print("Salario con aumento: ", self.salario)
    
def main():
  empleado1 = Empleado(0, "", 0, "")
  empleado1.leer()
  empleado1.calcularSalario(int(input("Introduce el aumento en porcentaje: ")))
  empleado1.mostrar()
  
main()