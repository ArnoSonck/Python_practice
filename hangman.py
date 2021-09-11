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
    # [output if condition else output for l in list]
    letters = [i for i in word]
    # letters = [i.upper() if i == "ñ" or i == "Ñ" else unidecode(i.upper()) for i in word]
    letters.pop()
    return letters
    # for i in letters:
    #     if letters[i] != gess[i]:
    #         print(letters[i], end = " ")
    #     else:
    #         print("_", end = " ")
    # print("\n")

def compare(hint,letter,letters):
    global flag
    for i in range(len(letters)):
        # if (letter[0] == letters[i] or letter[0] == hint[i]):
        if (unidecode(letter[0].upper()) == unidecode(letters[i].upper()) or letter[0] == hint[i]):
            # print(letter[0] == hint[i])
            hint[i] = letters[i]
            flag = True
            # print(letter)
        else:
            # print(str(letter[0]))
            # print(str(letters[i]))
            # print(letter[0] == letters[i])
            hint[i] = hint[i]
            # print("_")
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
    # print("Adivina la palabra")
    word = escoge_palabra()
    # word = [AñÑBA] # palabra de prueba
    # print(word)
    letters = separa_letras(word)
    # letters = ["A","B","A","B","A"] # palabra de prueba
    hint = ["_" for i in letters]
    # print(hint)
    # print(letters)
    while hint != letters:
        print(hint, "\n")
        letter = input("Introduzca una letra: ")
        # letter = letter.upper()
        # letter = ['A']
        # print(letter)
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