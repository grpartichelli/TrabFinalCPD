# -*- coding: utf-8 -*-
from entradaFuncs import * 
from trieDataStructure import *


def main():
	
	dataRating, dataMovies , dataTags = entrada()
	
	trieTree = createTrieStructure(dataMovies)
	print(trieTree.findAll("Batman"))
	
	








	print("Returned 0")
	
if __name__ == '__main__':
	main()

