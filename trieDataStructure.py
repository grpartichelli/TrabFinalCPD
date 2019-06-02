class trieNode:
	def __init__(self,info=None, isID=False):
		self.children = []
		self.isID = isID
		self.info = info
	
	def isID(isID):
		return self.isID

	def getInfo(info):
		return self.info
	
	def addChildren(newChild):
		self.children.append(newChild)
	
	def getChildren(self):
		return self.children()

class trie:

	def __init__(self):
		self.root = trieNode()
		
		
	def insert(self,word,id):
		
		nodoAtual = self.root
		foundEnd = False

		for char in word:
			if foundEnd == False:
				
				for children in nodoAtual:
					if children.getInfo() == char:
						nodoAtual = children
						break
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

	def findID(self,word):
		nodoAtual = self.root
		for char in word:
			for children in nodoAtual:
					if children.getInfo() == char:
						nodoAtual = children
						break
					print("Search Failed")
					return -1
			
		for children in nodoAtual:
			if children.isID() == True:
				return children.info()
			else:
				print("Search Failed")
					return -1



				
				

	
		
				
				
				
				