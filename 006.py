class Circunferencia:
  def __init__(self, posx:int, posy:int, radio:int):
    self.posx = posx
    self.posy = posy
    self.radio = radio
  def leer(self):
    self.posx = int(input("Ingrese la posición x: "))
    self.posy = int(input("Ingrese la posición y: "))
    self.radio = int(input("Ingrese el radio: "))
  def mostrar(self):
    print("Posición x: ", self.posx)
    print("Posición y: ", self.posy)
    print("Radio: ", self.radio)
  def circunferencia(self):
    print(f"La circunferencia es: {2 * 3.1416 * self.radio}")
  def area(self):
    print(f"El área es: {3.1416 * self.radio ** 2}")
    
def main():
  circulo = Circunferencia(0, 0, 0)
  circulo.leer()
  circulo.mostrar()
  circulo.circunferencia()
  circulo.area()
main()