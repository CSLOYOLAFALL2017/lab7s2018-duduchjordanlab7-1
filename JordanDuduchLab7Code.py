# Tim Jordan & Tim Duduch
# CS151.02
# Franceschi
#
#
#

import os
import sys


def movie_file():
    filename = input("Please input a file name: ")
    while not os.path.exists(filename):
        filename = input("Not a valid file, please enter a file name: ")
    return filename




def maximum_profit(filename):

    try:
        filename = open(filename, "r")
        profit = 0
        bestmovie = ""

        for line in filename:

            date, title, budget, revenue = line.split(",")
            budget = float(budget)
            revenue = float(revenue)
            totalRevenue = revenue - budget
            if totalRevenue > profit:
                profit = totalRevenue
                bestmovie = title
        print("The movie with the highest profit was:", bestmovie, "who's profit was $%.2f" % profit)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    return


def outputFile(newFile, openFile):
    newOutput = open(openFile, "w")

    try:
        newFile = open(newFile, "r")
        for line in newFile:
            date, title, budget, revenue = line.split(",")
            budget = float(budget)
            revenue = float(revenue)
            totalRevenue = revenue - budget
            print("Date Released:", date, file = newOutput)
            print("Title:", title, file = newOutput)
            print("Total Revenue: $%2f" % revenue, file = newOutput)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    return

def main():
    print("This program is designed to output the movie with the highest profit.")
    newFile = movie_file()
    openFile = input ("Please enter a file to output to:")

    maximum_profit(newFile)

    outputFile(newFile, openFile)

    return


main()
