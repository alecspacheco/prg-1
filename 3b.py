class Libro:
  def __init__(self, codigo, titulo, autor, editorial, nropaginas:int):
    self.codigo = codigo
    self.titulo = titulo
    self.autor = autor
    self.editorial = editorial
    self.nropaginas = nropaginas
    
  def leerDatos(self):
    self.codigo = input("Ingrese el codigo: ")
    self.titulo = input("Ingrese el titulo: ")
    self.autor = input("Ingrese el autor: ")
    self.editorial = input("Ingrese la editorial: ")
    self.nropaginas = int(input("Ingrese el numero de paginas: "))
  
  def imprimirDatos(self):
    print(f'Codigo: {self.codigo}, Titulo: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Numero de paginas: {self.nropaginas}')
    
def main():
  libro1 = Libro('','','','',0)
  libro1.leerDatos()
  libro1.imprimirDatos()
main()