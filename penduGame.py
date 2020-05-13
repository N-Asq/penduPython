#!/usr/bin/python3
#coding: utf-8
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from penduFunc import *
from penduConfig import *

scoreFile = checkScoreFile(scoreFile)
tag = getTag(scoreFile)
welcomeMessage = "||   {0}, devinez ce mot, ou vous serez pendu !  || ".format(tag).upper()


playAgainOK = True

while playAgainOK:
    word = chooseWord(wordList)
    N_error = 0
    points = len(hangingStages)-1-N_error

    lettersFound = ""

    print("\n"+"="*(len(welcomeMessage)-1))
    print(welcomeMessage)
    print("="*(len(welcomeMessage)-1))

    wordFoundOK = False
    while points > 0 and not wordFoundOK:
        displayAdvancement(hangingStages,N_error,word,lettersFound)
        print("{0} points restants...".format(points))
        letter = getLetter()
        if letter in word:
            lettersFound = str(set(lettersFound+letter))
        else:
            print("\nCette lettre ne fait pas partie du mot, un pas de plus vers la mort.")
            N_error += 1
            points = len(hangingStages)-1-N_error
        wordFoundOK = all(letter in lettersFound for letter in word)

    displayAdvancement(hangingStages,N_error,word,lettersFound)
    if wordFoundOK:
        print("Sauvé ! Vous avez gangé {0} points.".format(points))
    else:
        print("Vous êtes mort. Vous perdez la moitié de vos points.")

    updatePoints(scoreFile,tag,points)

    response = getValidResponse("\nVoulez-vous rejouer ? [O/N] ",["O","Y","N"],"Veuillez entrer une réponse valide.")
    playAgainOK = response.upper() in ["O","Y"]