def entrada():	
	
	f = open("minirating.csv", encoding="utf8")
	f2 = open("movie.csv", encoding="utf8")
	f3 = open("tag.csv", encoding="utf8")
	dataRating = []
	dataMovies = [] 
	dataTags = []


	for line in f:
		dataRating.append(line)
		
	for line in f2:
		dataTags.append(line)
		
	for line in f3:
		dataMovies.append(line)
		
		
	return dataRating, dataTags, dataMovies