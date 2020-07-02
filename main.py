#!/usr/bin/env python3
import wikipedia as wiki
from os import system
from os.path import exists
import argparse


def search(term):
    if exists("/usr/bin/less"):
        system(f'echo "{wiki.summary(term)}" | less')
    else:
        system(f'echo "{wiki.summary(term)}"')

def full_search(term):
     if exists("/usr/bin/less"):
        system(f'echo "{wiki.page(term).content}" | less')
     else:
        system(f'echo "{wiki.page(term).content}"')
    

def term_search(search_term, full_flag = False):
    searcher = wiki.search(search_term)
    s_len = len(searcher)
    if full_flag == False:
        if(s_len>1):
            for i in range(s_len):
                print(f'{i+1}: {searcher[i]}')

            f_term = int(input(f'select between 1 & {s_len}: ')) - 1
            search(searcher[f_term])

        elif(s_len==1):
            search(searcher[0])
        else:
            print("Sorry result not found")
    
    else:
        if(s_len>1):
            for i in range(s_len):
                print(f'{i+1}: {searcher[i]}')

            f_term = int(input(f'select between 1 & {s_len}: ')) - 1
            full_search(searcher[f_term])

        elif(s_len==1):
            full_search(searcher[0])
        else:
            print("Sorry result not found")




if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-s","--search", type=str ,help="pass term for searching wikipedia")
    argparser.add_argument("-F","--full", action='store_true', help="output all the pagedata from wikipedia")
    argparser.add_argument("-i","--interactive",  action='store_true', help="Run the tool interactively(CTRL+C to quit)")
    args = argparser.parse_args()
    
    if(args.search):
        term_search(args.search)
    else:
        while(True):
            search_term = input("What do you want to search : ")
            term_search(search_term)
