#
#
#
#
#
#
#
#

import os

def movie_file():
    filename = input("Please input a file name: ")
    while not os.path.exists(filename):
        filename = input("Not a valid file, please enter a file name: ")
    return filename




def maximum_profit(filename):

    try:
        file_object = open(filename, "r")
        print( "File opened for reading" )
        for line in file_object:
            print(line, end = " ")
            date, title, budget, revenue = line.split(",")
            budget = int(budget)
            revenue = int(revenue)



    except FileNotFoundError:
        print( "File does not exist" )




movies = movie_file()
maximum_profit(movies)
