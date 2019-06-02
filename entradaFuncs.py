def entrada():	
	
	f = open("minirating.csv", encoding="utf8")
	f2 = open("movie.csv", encoding="utf8")
	f3 = open("tag.csv", encoding="utf8")
	dataRating = []
	dataMovies = [] 
	dataTags = []

    #Skips the first line
	next(f)
	next(f2)
	next(f3)
	#Reads the rest of the file
	for line in f:
		line = line.split(",")
		dataRating.append([int(line[0]), int(line[1]), float(line[2])])
		
	for line in f2:
		dataTags.append(line)
		
	for line in f3:
		dataMovies.append(line)
	
	return dataRating, dataTags, dataMovies