import re

class trieNode:
	def __init__(self,info=None, isID=False):
		self.children = []
		self.isID = isID
		self.info = info
	
	def isFinal(self):
		return self.isID

	def getInfo(self):
		return self.info
	
	def addChildren(self,newChild):
		self.children.append(newChild)
	
	def getChildren(self):
		return self.children

class trie:

	def __init__(self):
		self.root = trieNode()
		
		
	def insert(self,word,id):
		
		nodoAtual = self.root
		foundEnd = False

		for char in word:
			if foundEnd == False:
				foundIt = False
				#Checks if any children already have this char
				for children in nodoAtual.getChildren():
					if children.getInfo() == char:
						#If they do have, then go to the next char
						nodoAtual = children
						foundIt = True
						break
				#If they don't, we found the end of whats already on the tree. Start creating a new path for the rest word.
				if not foundIt:
					foundEnd = True
					newNode = trieNode(char)
					nodoAtual.addChildren(newNode)	
					nodoAtual = newNode
			else:
				newNode = trieNode(char)
				nodoAtual.addChildren(newNode)	
				nodoAtual = newNode
		#Creating new path
		newNode = trieNode(id,True)
		nodoAtual.addChildren(newNode)

	
	def findAll(self,prefix):
		
		nodoAtual = self.root
		
		#Searches untill end of the prefix
		for char in prefix:	
			foundIt = False

			for children in nodoAtual.getChildren():
				if children.getInfo() == char:
					nodoAtual = children
					foundIt = True
					break	
			if not foundIt:
				print("Search Failed")
				return -1	
		
		infoList = []
		#From this node, we will go search for all the other paths.
		return self.findAllRecursion(prefix,nodoAtual,infoList)
					

	
	def findAllRecursion(self,prefix,nodoAtual,infoList):
		
		
		for children in nodoAtual.getChildren():
			if children.isFinal() == True:
				#Once we find an end, we append the id to the list.
				infoList.append((children.getInfo()))
			else:
				#While searching the path, we build the words.
				newWord = prefix + children.getInfo()
				self.findAllRecursion(newWord,children,infoList)

		
		
		return infoList
		
				
				
				
