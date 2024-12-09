
def crearArchivo():
  archivo = open("miscontactos.txt", "w")
  archivo.close()

def guardarRegistro(nombre, alias, celular):
  archivo = open("miscontactos.txt", "a")
  archivo.write(nombre + "," + alias + "," + celular + "\n")
  archivo.close()
  
def mostrar():
  archivo = open("miscontactos.txt", "r")
  for linea in archivo:
    print(linea)
  archivo.close()
  
def main():
  crearArchivo()
  guardarRegistro(input("Nombre: "), input("Alias: "), input("Celular: "))
  mostrar()  
main()