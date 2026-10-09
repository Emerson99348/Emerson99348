import random

intentos = 6
ahorcado = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======
    """
]

print("JUEGO DEL AHORCADO")

palabras = ["palomas","vaca","perro","gato","tiburon"]
palabra = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra)
print(" ".join(palabra_oculta))

letras_usadas = []
while intentos > 0:
    letra = input("Elige una letra: ").lower()
    if letra in letras_usadas:
        print("Ya utilizaste esa letra.")
        continue
    letras_usadas.append(letra)
#CICLO PRINCIPAL
    letras_usadas = ["a"]
    if letra in palabra:
        print("¡Correcto!")
        print("¡Incorrecto!")
#RECORRE ESPACIO POR ESPACIO LAS LETRAS DE LA PALABRA PARA COMPARAR
        for i, letra_palabra in enumerate(palabra):
            if letra_palabra == letra:
                palabra_oculta[i] = letra
                print(" ".join(palabra_oculta))
                if "_" not in palabra_oculta:
                    print("¡GANASTE!")
                    break
                "_" not in palabra_oculta
#DESPUES DE RECORRER LOS ESPACIOS RESTA LOS INTENTOS DISPONIBLES                
            else:
                intentos -= 1
                print("Letra incorrecta.")
                print("Intentos restantes:", intentos)
                print(ahorcado[6 - intentos])
                ahorcado[6 - 5]
                ahorcado[1]
                if intentos == 0:
                    print("¡PERDISTE!")
                    print("La palabra era:", palabra)

#...