
class Celular:
  def __init__(self, marca, modelo, color, ram, almacenamiento, resCamara, precio:float):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.ram = ram
    self.almacenamiento = almacenamiento
    self.resCamara = resCamara
    self.precio = precio
    
  def leer(self):
    self.marca = input("Marca: ")
    self.modelo = input("Modelo: ")
    self.color = input("Color: ")
    self.ram = input("Memoria RAM: ")
    self.almacenamiento = input("Almacenamiento: ")
    self.resCamara = input("Resolución de cámara: ")
    self.precio = float(input("Precio: "))
  def mostrar(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Color: {self.color}")
    print(f"Memoria RAM: {self.ram}")
    print(f"Almacenamiento: {self.almacenamiento}")
    print(f"Resolución de cámara: {self.resCamara}")
    print(f"Precio: {self.precio}")
  def cambiarPrecio(self, nuevo_precio:float):
    self.precio = nuevo_precio
    
def main():
  celular = Celular("", "", "", "", "", "", 0)
  celular.leer()
  celular.mostrar()
  celular.cambiarPrecio(int(input("Nuevo precio: ")))
  celular.mostrar()
  
main()