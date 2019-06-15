from trieDataStructure import *
from movieHashDataStructure import *
from userHashDataStructure import *
from stringHashDataStructure import *
import csv

def entrada():  
    
    #Creates the Hash Table for Movies There are 27278 movies. 27278*1.6 ~= 45000
    moviesTable = movieHashTable(tableSize =45000)
    
    #Creates the Hash Table for Users
    usersTable = userHashTable(tableSize= 30000000)
    
    #Creates the Hash Table for Genres. There are 21 genres. 21*1.9 ~= 40
    genresTable = stringHashTable(tableSize = 40 )
   
    #Creates the Hash Table for Tags. There are 38644 tags. 38644*1.6 ~= 61.830
    tagsTable = stringHashTable(tableSize = 61830 )
    #Creates Trie Three:
    trieTree = trie()
    clr_screen()
    print("Loading Movies...")
    #Reads movie.csv file
    with open('movie.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        #Separates the data
        for line in reader:
            movieId = int(line[0])
            movieTitle = line[1]
            if  line[2] != "(no genres listed)":
                movieGenres = line[2].split("|")
            else:
                movieGenres = []
            #Inserts movie on hash table
            for genre in movieGenres:
                genresTable.insertList(genre.lower(),movieId)

            movieData= movieInfo(movieId,movieGenres,movieTitle)
            moviesTable.insertMovie(movieData)
            trieTree.insert(movieTitle,movieId)
  
    clr_screen()
    print("Loading Ratings...") 
    #Reading rating.csv file.
    #f =  open('minirating.csv', 'r', encoding="utf8") 
    f =  open('ratingOpt.csv', 'r', encoding="utf8") 
    next(f)
    for line in f:
        line = line.split(",")
        userId = int(line[0])

        movieId = int(line[1])
        rating = float(line[2])
        newReview = review(userId,rating,movieId)
        #Inserts users reviews to the hashtable
        usersTable.insertReview(newReview)
        #Updates hash tables to have every rating
        moviesTable.updateMovie(movieId,rating)
    

    
    csvFile.close()
    clr_screen()
    print("Loading Tags...")
    #Reads through the rating file
    with open('tagOpt.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for line in reader:
            movieId = int(line[1])
            movieTag = line[2]
            #Creates a hash table that takes tags as id.
            tagsTable.insertList(movieTag.lower(),movieId)

            
    csvFile.close()
    
    return trieTree, moviesTable,usersTable, genresTable,tagsTable

import os
def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




        
            
    


    