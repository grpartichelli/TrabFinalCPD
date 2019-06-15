# -*- coding: utf-8 -*-
from entradaFuncs import * 
from trieDataStructure import *
from movieHashDataStructure import *
from userHashDataStructure import *
from stringHashDataStructure import *
from sortFunctions import *


import re
import time
import sys
sys.path.append(sys.path[0]+'\\importedLibs')
from prettytable import PrettyTable


def main():
    clr_screen()
    t0 = time.time()
    trieTree, moviesTable,usersTable, genresTable,tagsTable = entrada()
    t1 = time.time()

    total = t1-t0
    clr_screen()
    print("Finished Loading. Time:",total)
    
    #Parses the commands and runs the appropriated function
    while(True):
        command =False
        flush_input()
        print("Enter your Command: ")
        word = input()
        clr_screen()
        if word[:5] == "movie":
            command = True
            prefix = word[5:].strip()
            movieFunction(prefix,trieTree,moviesTable)
        
        if word[:4] == "user":
            command = True
            try:
                userId = int(word[4:].strip())
                userFunction(userId,usersTable,moviesTable)
            except:
                print("Incorrect Formating")
                
        if word[:3] == "top":
            command = True
            firstspace = word.find(" ")
            number = word[3:firstspace]
            try:
                number = int(number)
                genre = word[firstspace:].strip()
                genresFunction(genre.lower(),number,genresTable,moviesTable)
            except:
                print("Incorrect Formating")

            
        
        if word[:4] == "tags":
            command = True
            tags = re.split('\'(.*?)\'', word[4:])
            for tag in tags:
                if tag == "" or tag == " ":
                    tags.remove(tag)
           
            tags = [tag.lower() for tag in tags]
            tagsFunction(tags,tagsTable,moviesTable)

           

        if word == "quit":
            break
        
        if not command:
            print("This command doesn't exist. Type \"quit\" to end execution.")

    print("Program Ended Successfully")
    

def movieFunction(prefix, trieTree,moviesTable):
    #Gets a list of movieIds with this prefix
    idList = trieTree.findAll(prefix)
    if idList != -1:

        t = PrettyTable(['movieID', 'Title', 'Genres', 'AvgRating', 'Count'])
       
        myIntegerSort(idList)
        
        for movieId in idList:
            #Searches for movie information on the movie Hash Table
            movie= moviesTable.searchMovie(movieId)
            t.add_row([movieId, movie.title," | ".join(movie.genres), round(movie.getAvgRating(),6),movie.numRatings])
            
        print(t)
    else:
        print("Movie Not Found")

def userFunction(userId,usersTable,moviesTable):
    #Gets a list of (movieId, rating)
    userRatings = usersTable.searchUser(userId)
    if userRatings != -1:
        t = PrettyTable(['User Rating', 'Title', 'AvgRating', 'Count'])
        
        for rating in userRatings:
            #Searches for movie information on the movie Hash Table
            movie= moviesTable.searchMovie(rating[0])
            
            t.add_row([rating[1], movie.title, round(movie.getAvgRating(),6),movie.numRatings])
            
        print(t)
    else:
        print("User Not Found")

def genresFunction(genre,number,genresTable,moviesTable):
    idList = []
    i=0

    movieList = []
    idList = genresTable.searchInfo(genre)
    
    if idList == -1:
        print("No Movies With Genre: "  + genre + " were found.")
        return -1

    #Makes a list of every movie with more than 1000 ratings
    for movieId in idList:
        movie = moviesTable.searchMovie(movieId)
        if movie.numRatings >= 1000:
            movieList.append(movie)
    #Orders the list by rating
    myMovieSort(movieList)

    #Making sure we don't go outside the maximum index
    if len(movieList) < number:
        number = len(movieList) 

    if movieList != []:    
       
        t = PrettyTable(['Title', 'Genres', 'AvgRating', 'Count'])
        #Prints the topN movies
        for i in range(number):
            movie = movieList[i]                           
            t.add_row([movie.title," | ".join(movie.genres), round(movie.getAvgRating(),6),movie.numRatings])
                
        print(t)
    else:
        print("No movie with 1000 or more ratings.")
        


def tagsFunction(tags,tagsTable,moviesTable):
    idList = []
    i=0
    #creates a list with the id of the movies of every tag
    for tag in tags:

        currentIdList = tagsTable.searchInfo(tag)
        if currentIdList == -1:
            print("The Tag: " + tag + " doesn't exist.")
            return -1
        idList += currentIdList
        i = i+1

    correctIds = []
    tagsSize = len(tags)

    if tagsSize != 1:
        #For every movie, checks if there are as many copys of it as tags. Meaning there is one for each tag, so the movie is every tag
        for movieId in idList:
            if idList.count(movieId) == tagsSize:
                #If the movie is every tag, puts it on the correctIds list, and deletes all of its other occurances on the list
                idList =list(filter((movieId).__ne__, idList))
                correctIds.append(movieId)

    else:
        correctIds = idList

    if correctIds != -1 and correctIds != []:        

        t = PrettyTable(['Title', 'Genres', 'AvgRating', 'Count'])
        
        for movieId in correctIds:
            #Searches for movie information on the movie Hash Table
            movie= moviesTable.searchMovie(movieId)
            t.add_row([movie.title," | ".join(movie.genres), round(movie.getAvgRating(),6),movie.numRatings])
            
        print(t)
    else:
        print("No Movie With Tags: "  + ' '.join(tags) + " was found.")
#Clears Keyboard Buffer
def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()

