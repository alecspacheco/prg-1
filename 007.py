class Rectangulo:
  def __init__(self, ancho:float, alto:float):
    self.ancho = ancho
    self.alto = alto
  def leer(self):
    self.ancho = float(input("Ingrese el ancho: "))
    self.alto = float(input("Ingrese el alto: "))
  def mostrar(self):
    print("Ancho: ", self.ancho)
    print("Alto: ", self.alto)
  def perimetro(self):
    print(f"El perímetro es: {2 * (self.ancho + self.alto)}")
  def area(self):
    print(f"El área es: {self.ancho * self.alto}")
    
def main():
  rectangulo = Rectangulo(0, 0)
  rectangulo.leer()
  rectangulo.mostrar()
  rectangulo.perimetro()
  rectangulo.area()
  
main()