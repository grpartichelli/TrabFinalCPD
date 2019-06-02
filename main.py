# -*- coding: utf-8 -*-
from entradaFuncs import * 
from trieDataStructure import *
import re

def main():
	
	dataRating, dataMovies , dataTags = entrada()
	
	trieTree = trie()
	for line in dataMovies:
		movieID = int(line[:line.find(",")])
		title = re.search('\"(.*?)\"', line)
		title = title.group(1)
		trieTree.insert(title,movieID)
		
		

	








	print("Returned 0")
	
if __name__ == '__main__':
	main()

