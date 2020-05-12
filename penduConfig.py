#!/usr/bin/python3
#coding: utf-8
scoreFile = "penduScores.py"

wordList = ["feuillages",
    "ceinturon",
    "chevalier",
    "cachalot",
    "autobus",
    "casablanca",
    "boustifaille",
    "arpenter",
    "etagere",
    "couleuvre",
    "hyperespace",
    "annulation",
    "carabine",
    "beatitude",
    "discernement",
]

hangingStages = list()
hangingStages.append("  ________\n  |      |\n  |      O\n  |    --|--\n  |     / \\\n__|__")
hangingStages.append("  ________\n  |      |\n  |      O\n  |    --|--\n  |\n__|__")
hangingStages.append("  ________\n  |      |\n  |      O\n  |      |\n  |\n__|__")
hangingStages.append("  ________\n  |      |\n  |      O\n  |\n  |\n__|__")
hangingStages.append("  ________\n  |      |\n  |\n  |\n  |\n__|__")
hangingStages.append("  ________\n  |\n  |\n  |\n  |\n__|__")
hangingStages.append("\n  |\n  |\n  |\n  |\n__|__")
hangingStages.append("\n\n\n\n\n_____")
hangingStages.append("\n\n\n\n\n")
hangingStages.reverse()