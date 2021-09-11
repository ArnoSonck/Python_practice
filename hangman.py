import os
import random
from unidecode import unidecode

flag = False # True = letra correcta 

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce","nt","dos"):
        os.system("cls")

def escoge_palabra():
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        words = [lines for lines in f]
        n = random.randint(0, len(words))
    return(words[n])

def separa_letras(word):
    letters = [i for i in word]
    letters.pop()
    return letters

def compare(hint,letter,letters):
    global flag
    for i in range(len(letters)):
        if (unidecode(letter[0].upper()) == unidecode(letters[i].upper()) or letter[0] == hint[i]):
            hint[i] = letters[i]
            flag = True
        else:
            hint[i] = hint[i]
    return(hint)

def ganaste(letters):
    clear()
    print("Felicidades, ganaste el juego")
    print("La palabra escondida era: \n" + str(letters))

def run():
    global flag
    clear()
    print("Bienvenido al juego del ahorcado")
    print("Trata de adivinar la palabra escondida letra por letra \n")
    word = escoge_palabra()
    letters = separa_letras(word)
    hint = ["_" for i in letters]
    while hint != letters:
        print(hint, "\n")
        letter = input("Introduzca una letra: ")
        hint = compare(hint,letter,letters)
        clear()
        if flag == False:
            print("La palabra no contiene la letra " + letter, "\n")
        else:
            print("Si tiene la letra " + letter, "\n")
        flag = False
    clear()
    ganaste(letters)


if __name__ == '__main__':
    run()