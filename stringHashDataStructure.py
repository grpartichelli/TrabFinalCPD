#Data Structure of HashTables that has an id of a string and a (string,list of ints) as information
class stringHashTable:
    def __init__(self,tableSize):
        self.tableSize = tableSize
        self.table = [None]*tableSize


    def insertList(self,string,number):
        hashed = str_func_hash(string,self.tableSize)
        i=0
        while True:
            index = ((i*i) + 31*i + hashed)%self.tableSize
            #Inserts if not occupied
            if self.table[index] == None:
                self.table[index] = (string,[number])
                return
            #If there is already this string, adds a number to the number list
            if self.table[index][0] == string:
                if number not in self.table[index][1]:
                    self.table[index][1].append(number)
                return

            i +=1
            

    def searchInfo(self,string):
        hashed = str_func_hash(string,self.tableSize)
        i=0
        while True:
            index = ((i*i) + 31*i + hashed)%self.tableSize
            if self.table[index] == None:
                print("Search Failed")
                return -1
            if self.table[index][0] == string:
                return self.table[index][1]
            i += 1

#Hash function using Horner's Method
def str_func_hash(s,tableSize):
    hashe = 0
    for c in s:
        hashe = (31*hashe + ord(c))%tableSize
    return hashe
