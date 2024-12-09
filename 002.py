
class Persona:
  def __init__(self, nombre, edad:int):
    self.nombre = nombre
    self.edad = edad
    
  def leer(self):
    self.nombre = input("Ingrese su nombre: ")
    self.edad = int(input("Ingrese su edad: "))
    
  def mostrar(self):
    print(f"Nombre: {self.nombre}")
    print(f"Edad: {self.edad}")
    
  def saludar(self):
    print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")
def main():
  persona = Persona(" ", 0)
  persona.leer()
  persona.mostrar()
  persona.saludar()
main()