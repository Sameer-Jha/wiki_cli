#!/usr/bin/env python3
import wikipedia as wiki
from os import system

def search(term):
    system(f'echo "{wiki.summary(term)}" | less')

def term_search(search_term):
    searcher = wiki.search(search_term)
    s_len = len(searcher)
    if(s_len>1):
        for i in range(s_len):
            print(f'{i+1}: {searcher[i]}')

        f_term = int(input(f'select between 1 & {s_len}: ')) - 1
        search(searcher[f_term])
    elif(s_len==1):
        search(searcher[0])
    else:
        print("Sorry result not found")


if __name__ == "__main__":
    search_term = input("What do you want to search : ")
    term_search(search_term)
