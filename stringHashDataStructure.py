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
            if self.table[index] == None:
                lst = [number]
                self.table[index] = (string,lst)
                return

            if self.table[index][0] == string:
                 self.table[index][1].append(number)
                 return

            i +=1
            

    def searchList(self,string):
        hashe = str_func_hash(string,self.tableSize)
        i=0
        while True:
            index = ((i*i) + 31*i + hashed)%self.tableSize
            if self.table[index] == None:
                print("Search Failed")
                return -1
            if self.table[index][0] == string:
                return table[index][1]
            i += 1


def str_func_hash(s,tableSize):
    hashe = 0
    for c in s:
        hashe = (31*hashe + ord(c))%tableSize
    return hashe
