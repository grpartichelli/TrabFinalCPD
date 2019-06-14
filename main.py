# -*- coding: utf-8 -*-
from entradaFuncs import * 
from trieDataStructure import *
from movieHashDataStructure import *
from userHashDataStructure import *
from stringHashDataStructure import *

# some_file.py
import sys
sys.path.append(sys.path[0]+'\\importedLibs')
from prettytable import PrettyTable


import re
import time


def main():
    t0 = time.time()
    trieTree, moviesTable,usersTable, genresTable,tagsTable = entrada()
    t1 = time.time()

    total = t1-t0
    print(total)
    print("Modo Console: ")
    flush_input()
    while(True):
        command =False
        word = input()

        if word[:5] == "movie":
            command = True
            prefix = word[5:].strip()
            movieFunction(prefix,trieTree,moviesTable)
        
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
        

        if word == "quit":
            break
        
        if not command:
            print("Esse comando não existe.")



    
    print("Programa Terminado com Sucesso.")
    
#TODO REMOVE SORTED
def movieFunction(prefix, trieTree,moviesTable):
    
    idList = sorted(trieTree.findAll(prefix))
    t = PrettyTable(['movieID', 'Title', 'Genres', 'AvgRating', 'Cout'])
    
    for movieId in idList:
        movie= moviesTable.searchMovie(movieId)
        t.add_row([movieId, movie.title," | ".join(movie.genres), round(movie.getAvgRating(),6),movie.numRatings])
        
    print(t)

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

if __name__ == '__main__':
    main()

