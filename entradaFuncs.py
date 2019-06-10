from trieDataStructure import *
from movieHashDataStructure import *
import csv



def entrada():  
    
    
    #Reads movie.csv file
    #There are 27278 movies. 27278*1.6 ~= 45000
    #Creates the Hash Table
    moviesTable = hashTable(tableSize =45000)
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
  
  
    
    with open('minirating.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for line in reader:
            userId = int(line[0])
            movieId = int(line[1])
            rating = float(line[2])
            #Updates hash tables to have every rating
            moviesTable.updateMovie(movieId,rating)
           

    


    csvFile.close()
    

    with open('tag.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for line in reader:
            userId = int(line[0])
            movieId = int(line[1])
            movieTag = line[2]
            
    csvFile.close()








        
            
    


    