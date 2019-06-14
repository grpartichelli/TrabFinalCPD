from trieDataStructure import *
from movieHashDataStructure import *
from userHashDataStructure import *
from stringHashDataStructure import *
import csv



def entrada():  
    
    
    print("START")
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
                genresTable.insertList(genre,movieId)

            movieData= movieInfo(movieId,movieGenres,movieTitle)
            moviesTable.insertMovie(movieData)
            trieTree.insert(movieTitle,movieId)
  
    print("MOVIES")
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
    

    print("RATINGS")
    

    csvFile.close()
    

    with open('tagOpt.csv', 'r', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for line in reader:
            movieId = int(line[1])
            movieTag = line[2]
            tagsTable.insertList(movieTag,movieId)

            
    csvFile.close()
    print("TAGS")
    return trieTree, moviesTable,usersTable, genresTable,tagsTable







        
            
    


    