#MergeSort function for integers
def myIntegerSort(lst):
    
    if len(lst) > 1: 
        index = len(lst)//2 #Divides the list in two parts
        left = lst[:index]    
        right = lst[index:]     
  
        myIntegerSort(left)  # Sorts Left
        myIntegerSort(right) # Sorts Right
  
        i =0
        j = 0
        k = 0
          
        #Merges both sides
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                lst[k] = left[i] 
                i+=1
            else: 
                lst[k] = right[j] 
                j+=1
            k+=1
          
        #If one of the sides is bigger,puts the rest of the elements.
        while i < len(left): 
            lst[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            lst[k] = right[j] 
            j+=1
            k+=1

#Merge sort function for movies. Orders in decreasing order, by rating
def myMovieSort(movieList):

    if len(movieList) > 1: 
        index = len(movieList)//2 #Divides the list in two parts
        left = movieList[:index]    
        right = movieList[index:]     
  
        myMovieSort(left)  # Sorts Left
        myMovieSort(right) # Sorts Right
  
        i =0
        j = 0
        k = 0
          
        #Merges both sides
        while i < len(left) and j < len(right): 
            if left[i].getAvgRating() > right[j].getAvgRating(): 
                movieList[k] = left[i] 
                i+=1
            else: 
                movieList[k] = right[j] 
                j+=1
            k+=1
          
        #If one of the sides is bigger,puts the rest of the elements.
        while i < len(left): 
            movieList[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            movieList[k] = right[j] 
            j+=1
            k+=1

    