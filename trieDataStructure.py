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
				for children in nodoAtual.getChildren():
					if children.getInfo() == char:
						nodoAtual = children
						foundIt = True
						break
				if not foundIt:
					foundEnd = True
					newNode = trieNode(char)
					nodoAtual.addChildren(newNode)	
					nodoAtual = newNode
			else:
				newNode = trieNode(char)
				nodoAtual.addChildren(newNode)	
				nodoAtual = newNode
		
		newNode = trieNode(id,True)
		nodoAtual.addChildren(newNode)

	
	def findAll(self,word):
		
		nodoAtual = self.root
		infoList = []
		#Searches untill end of the word
		for char in word:	
			foundIt = False

			for children in nodoAtual.getChildren():
				if children.getInfo() == char:
					nodoAtual = children
					foundIt = True
					break	
			if not foundIt:
				print("Search Failed")
				return -1	
		
		return self.findAllRecursion(word,nodoAtual)
					

		
	def findAllRecursion(self,word,nodoAtual,infoList=[]):
		
		
		for children in nodoAtual.getChildren():
			if children.isFinal() == True:
				
				infoList.append((children.getInfo(), word))
			else:
				newWord = word + children.getInfo()
				self.findAllRecursion(newWord,children,infoList)

		
		
		return infoList
		
				
				
				
