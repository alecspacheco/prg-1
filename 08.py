import csv

def main():
  with open('titanic.csv', 'r') as file:
    lector = csv.DictReader(file)
    conteo_f = 0
    conteo_v = 0
    conteo_sobre = 0
    conteo_menores = 0
    conteo_sobre_f = 0
    conteo_sobre_m = 0    
    for col in lector:
      if col['Sex'] == 'female':
        conteo_f += 1
        if col['Survived'] == '1':
          conteo_sobre_f += 1
      elif col['Sex'] == 'male':
        conteo_v += 1
        if col['Survived'] == '1':
          conteo_sobre_m += 1
      
      if col['Survived'] == '1':
        conteo_sobre += 1
      
      if col['Age'] and float(col['Age']) < 18:
        conteo_menores += 1
    
    print(f"Cantidad de mujeres que viajaron: {conteo_f}")
    print(f"Cantidad de hombres que viajaron: {conteo_v}")
    print(f"Cantidad de sobrevivientes: {conteo_sobre}")
    print(f"Cantidad de menores de 18 años: {conteo_menores}")
    print(f"Cantidad de mujeres que sobrevivieron: {conteo_sobre_f}")
    print(f"Cantidad de hombres que sobrevivieron: {conteo_sobre_m}")
main()