#!/usr/bin/python3
#coding: utf-8

def checkScoreFile(scoreFile = "penduScores.py"):
    """
        Regarde si le fichier de scores existe, et le créé dans le cas contraire.

        :param arg1: Fichier de scores à chercher.
        :type arg1: str
        :return: Fichier de scores utilisé pour stocker les scores du joueur.
        :rtype: str
    """
    import pickle
    import os

    if not os.path.exists(scoreFile):
        print("Le fichier de scores n'a pas été trouvé.")
        with open(scoreFile,"bw") as file:
            pickler = pickle.Pickler(file)
            pickler.dump({})
        print("\tCréation et initialisation de {0} terminées.".format(scoreFile))
    else:
        with open(scoreFile,"br") as file:
            unpickler = pickle.Unpickler(file)
            try:
                scores = unpickler.load()
                assert type(scores) == type(dict())
            except EOFError:
                pass
            except AssertionError:
                exit("Le fichier renseigné ({0}) est corrompu ou n'est pas un fichier de scores.\n"
                "Veuillez utiliser un autre fichier.".format(scoreFile))
    return scoreFile

def getTag(scoreFile = "penduScores.py"):
    """
        Demande à l'utilisateur son pseudo, vérifie si ce dernier est dans le fichier de scores,
        le créée si ce n'est pas le cas, et renvoie le pseudo à utiliser.

        :param arg1: Fichier de scores à utiliser.
        :type arg1: str
        :return: Pseudo de l'utilisateur
        :rtype: str
    """
    import pickle

    with open(scoreFile,"br") as file:
        unpickler = pickle.Unpickler(file)
        try:
            scores = unpickler.load()
        except EOFError:
            scores = {}

    tagOK = False
    while not tagOK:
        tag = input("Veuillez saisir votre pseudo pour jouer : ")
        if scores.get(tag) != None:
            print("\tUn joueur ayant ce pseudo est enregistré, avec un score de {0} points.".format(scores.get(tag)))

            response = getValidResponse("\tVoulez-vous charger ce profil ? [O/N] ",["O","Y","N"],"Veuillez saisir une réponse valide.")
            tagOK = response.upper() in ["O","Y"]
        else:
            print("\tAucun profil correspondant à ce pseudo n'a été trouvé.")
            response = getValidResponse("\tVoulez-vous créer ce profil ? [O/N] ",["O","Y","N"],"Veuillez saisir une réponse valide.")
            if response.upper() in ["Y","O"]:
                scores[tag] = 0
                with open(scoreFile,"bw") as file:
                    pickler = pickle.Pickler(file)
                    pickler.dump(scores)
                tagOK = True

    return tag

def chooseWord(wordList):
    """
        Choisis aléatoirement le mot à faire deviner à l'utilisateur dans une liste.
    
        :param arg1: Liste de mots.
        :type arg1: list
        :return: Le mot à faire deviner en minuscules.
        :rtype: str
    """
    import random
    return random.choice(wordList).lower()

def displayAdvancement(hangingStages,N_error,word,lettersFound):
    """
        Affiche l'avancement du pendu et de la découverte du mot.
    
        :param arg1: Etat du pendu.
        :param arg2: Mot à deviner.
        :param arg3: Lettres déjà trouvées.
        :type arg1: str
        :type arg2: str
        :type arg3: str
    """
    if N_error == len(hangingStages)-1:
        wordReveal = " ".join([letter.upper() for letter in word])
    else:
        wordReveal = " ".join([letter.upper() if letter in lettersFound else "_" for letter in word])
    print(("\n\n"+hangingStages[N_error]+"\t\t"+wordReveal+"\n\n"))

def getLetter():
    """
        Demande à l'utilisateur une unique lettre et la convertit en minuscule.
    
        :return: Lettre minuscule choisie par l'utilisateur.
        :rtype: str 
    """
    import string
    letter = getValidResponse("Quelle lettre choisissez-vous ? ",list(string.ascii_letters),"Veuillez renseigner une unique lettre.")
    return letter.lower()

def updatePoints(scoreFile,tag,points):
    """
        Met à jour les points dans le fichier de score. Si points == 0, divise le score par 2. 
    
        :param arg1: Fichier de score à utiliser.
        :param arg2: Pseudo de l'utilisateur.
        :param arg3: Points à ajouter.
        :type arg1: str
        :type arg2: str
        :type arg3: int
    """
    import math
    import pickle

    with open(scoreFile,"br") as file:
        unpickler = pickle.Unpickler(file)
        scores = unpickler.load()

    if scores.get(tag) == None:
        scores[tag] = 0
    if points > 0:
        scores[tag] += points
    else:
        scores[tag] = math.floor(scores[tag]/2)

    with open(scoreFile,"bw") as file:
        pickler = pickle.Pickler(file)
        pickler.dump(scores)

    print("Vous avez maintenant {0} points.".format(scores[tag]))   

def getValidResponse(questionMessage, validChoices = ["Y","N"], errorMessage = "Please type a valid response.", caseSensitive = False):
    """
        Pose à l'utilisateur la même question en boucle, jusqu'à ce que la réponse renseignée fasse partie des choix valides.
    
        :param arg1: Question à poser.
        :param arg2: Liste des réponses valides. Seuls les éléments de type str seront pris en compte.
        :param arg3: Message indiquant une réponse invalide.
        :param arg4: Rendre la réponse sensible à la casse.
        :type arg1: str
        :type arg2: list
        :type arg1: str
        :type arg1: bool
        :return: La réponse valide de l'utilisateur.
        :rtype: str
    """
    responseOK = False
    if not caseSensitive:
        validChoices = [choice.upper() for choice in validChoices]
    while not responseOK:
        try:
            response = input(questionMessage)
            if caseSensitive:
                responseWProperCase = response
            else:
                responseWProperCase = response.upper()
            if responseWProperCase not in validChoices:
                raise(ValueError)
        except ValueError:
            print(errorMessage)
        else:
            responseOK = True
    return response