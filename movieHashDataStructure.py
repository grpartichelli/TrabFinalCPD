class movieHashTable:
	def __init__(self,tableSize):
		self.tableSize = tableSize
		self.table = [None]*tableSize
		
	
	def insertMovie(self,movieInfo):
			i = 0
			hashed =  movieInfo.getId()%self.tableSize
			#Searches for an empty spot to insert
			while True:
				index = ((i*i) + (31*i) + hashed)%self.tableSize
				if self.table[index] == None:
					self.table[index] = movieInfo
					return
				i += 1

	def searchMovie(self,id):
			i = 0
			hashed =  id%self.tableSize
			while True:
				index = ((i*i) + (31*i) + hashed)%self.tableSize
				
				if self.table[index] == None:
					print("Movie not found")
					return -1
				else:
					if self.table[index].getId() == id:
						return self.table[index]
				
				i += 1

	def updateMovie(self,id,rating):
			i = 0
			hashed =  id%self.tableSize
			while True:
				index = ((i*i) + (31*i) + hashed)%self.tableSize

				if self.table[index] == None:
					print("Movie not found")
					return -1
				else:
					if self.table[index].getId() == id:
						self.table[index].addRating(rating)
						self.table[index].increaseNumRating()
						
						return 
				
				i += 1			
	
#Class to store all the info for a movie, including all the ratings				
class movieInfo():
	def __init__(self,id,genres,title):
		self.id = id
		self.genres = genres
		self.title = title
		self.sumRatings = 0
		self.numRatings = 0
	

	def addRating(self,rating):
		self.sumRatings += rating 

	def increaseNumRating(self):
		self.numRatings += 1

	def getAvgRating(self):
		if(self.numRatings == 0):
			return 0
		return self.sumRatings/self.numRatings

	def getId(self):
		return self.id

