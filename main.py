# -*- coding: utf-8 -*-
from entradaFuncs import * 
from trieDataStructure import *
import re
import time


def main():
	t0 = time.time()
	entrada()
	t1 = time.time()

	total = t1-t0
	print(total)
	print("Modo Console: ")
	while(False):
		command =False
		word = input()

		if word[:5] == "movie":
			command = True
			prefix = word[5:].strip()
			print("TODO: MOVIE")
		
		if word[:4] == "user":
			command = True
			userId = word[4:].strip()
			print("TODO: USER")
			
				
		if word[:3] == "top":
			command = True
			firstspace = word.find(" ")
			n = word[3:firstspace]
			tag = word[firstspace:].strip()
			print("TODO: TOP")
		
		if word[:4] == "tags":
			command = True
			tags = re.split('\'(.*?)\'', word[4:])
			for tag in tags:
				if tag == "" or tag == " ":
					tags.remove(tag)
			print("TODO: TAGS")
		

		if word == "":
			break
		
		if not command:
			print("Esse comando não existe.")



	
	print("Programa Terminado com Sucesso.")
	
if __name__ == '__main__':
	main()

