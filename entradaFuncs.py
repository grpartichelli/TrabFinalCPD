from trieDataStructure import *
from movieHashDataStructure import *
from userHashDataStructure import *

import csv



def entrada():  
    
    
    #Reads movie.csv file
    #There are 27278 movies. 27278*1.6 ~= 45000
    #Creates the Hash Table for Movies
    moviesTable = movieHashTable(tableSize =45000)
    usersTable = userHashTable(tableSize= 30000000)
    #There are users
    #Creates the Hash Table for Users
    #usersTable = hashTable(tableSize =?)
    #Creates Trie Three:
    trieTree = trie()

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
            movieData= movieInfo(movieId,movieGenres,movieTitle)
            moviesTable.insertMovie(movieData)
            trieTree.insert(movieTitle,movieId)
  
    print("MOVIES")
    f =  open('rating.csv', 'r', encoding="utf8") 
       
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
    

    print("RATINGS")
    

    csvFile.close()
    

    with open('tag.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for line in reader:
            userId = int(line[0])
            movieId = int(line[1])
            movieTag = line[2]
            
    csvFile.close()
    print("TAGS")







        
            
    


    