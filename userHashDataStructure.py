    
class userHashTable:
    def __init__(self,tableSize):
        self.tableSize = tableSize
        self.table = [None]*tableSize
        
    
    def insertReview(self,review):
        
        i = 0
        hashed =  review.getUserId()%self.tableSize
        while True:
            index = ((i*i) + (157*i) + hashed)%self.tableSize
            

            if self.table[index] == None:
                self.table[index] = userInfo(review.getUserId(),review.getMovieId(),review.getRating())

                return
            
            if self.table[index].getUserId() == review.getUserId():
                
                self.table[index].addMovieRates((review.getMovieId(),review.getRating()))
                return
            

            i += 1



    
    def searchUser(self,userId):
        i = 0
        hashed =  userId%self.tableSize
        while True:
            index = ((i*i) + (157*i) + hashed)%self.tableSize
            
            if self.table[index] == None:
                print("User not found")
                return -1
            
            if self.table[index].getUserId() == userId:
                return self.table[index]
                
            i += 1




class review():

    def __init__(self,userId,rating,movieId):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating

    def getUserId(self):
        return self.userId
    
    def getRating(self):
        return self.rating
    
    def getMovieId(self):
        return self.movieId


class userInfo:
    
    def __init__(self,userId,movieId,rating):
        self.movieRates = []
        self.userId = userId
        self.movieRates.append((movieId,rating))
        
    
    def getUserId(self):
        return self.userId

    def addMovieRates(self,movieTuple):
    
        self.movieRates.append(movieTuple)
    
    
