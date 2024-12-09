
def main():
  with open('palabras_rae.txt', encoding='utf-8') as f:
    palabras = f.read().splitlines()
  texto = input('Ingrese una oración: ')
  palabras_texto = texto.split()
  mal_escritas = []
  for palabra in palabras_texto:
    palabra_limpia = palabra.strip(',.!?;:')
    if palabra_limpia.lower() not in palabras:
      mal_escritas.append(palabra_limpia)
  print('Palabras mal escritas:')
  for palabra in mal_escritas:
    print(palabra)
    
main()
