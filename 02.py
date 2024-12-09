
def crearArchivo():
  archivo = open("compras.txt", "w")
  archivo.close()
  
def guardarRegistro(fecha, proveedor, producto, cantidad, precio):
  archivo = open("compras.txt", "a")
  archivo.write(fecha + "," + proveedor + "," + producto + "," + cantidad + "," + precio + "\n")
  archivo.close()
  
def mostrar():
  archivo = open("compras.txt", "r")
  for linea in archivo:
    print(linea)
  archivo.close()
  
def main():
  crearArchivo()
  guardarRegistro(input("Fecha(año-mes-dia): "), input("Proveedor: "), input("Producto: "), input("Cantidad: "), input("Precio: "))
  mostrar()
main()