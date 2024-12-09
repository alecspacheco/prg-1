
class Automovil:
  def __init__(self, placa, marca, modelo, color):
    self.placa = placa
    self.marca = marca
    self.modelo = modelo
    self.color = color
  def leer(self):
    self.placa = input('Placa: ')
    self.marca = input('Marca: ')
    self.modelo = input('Modelo: ')
    self.color = input('Color: ')
  def mostrar(self):
    print('Placa:', self.placa)
    print('Marca:', self.marca)
    print('Modelo:', self.modelo)
    print('Color:', self.color)

def main():
  auto = Automovil('','','','')
  auto.leer()
  auto.mostrar()
main()