#!/usr/bin/env python3
import wikipedia as wiki
from os import system
from os.path import exists
from string import ascii_lowercase
from random import choice
import argparse


def rand_string_gen(len):
    sel_space = ascii_lowercase
    name = ""
    for i in range(len):
        name = name + choice(sel_space)
    return name

def is_online():
    status = system('ping -c 1 -q google.com > /dev/null 2>&1')
    if status == 0:
        return True
    else:
        return False

def search(term):
    if exists("/usr/bin/less"):
        system(f'echo "{wiki.summary(term)}" | less')
    else:
        system(f'echo "{wiki.summary(term)}"')


def full_search(term):
    data_file = temp_reader(term)
    if exists("/usr/bin/less"):
        system(f"less {data_file}")
    else:
        system(f"cat {data_file}")
    system(f"rm -rf {data_file}")


def temp_reader(search_data):
    if exists("/tmp"):
        file = open(f"/tmp/{rand_string_gen(5)}.txt", "w+")
        file.write(wiki.page(search_data).content)
        name = file.name
        file.close()
        return name
    elif exists("~/.wiki_cli"):
        file = open(f"~/.wiki_cli/{rand_string_gen(5)}.txt", "w+")
        file.write(wiki.page(search_data).content)
        name = file.name
        file.close()
        return name
    else:
        system("mkdir ~/.wiki_cli")
        file = open(f"~/.wiki_cli/{rand_string_gen(5)}.txt", "w+")
        file.write(wiki.page(search_data).content)
        name = file.name
        file.close()
        return name


def term_search(search_term, full_flag=False):
    searcher = wiki.search(search_term)
    s_len = len(searcher)
    if full_flag == False:
        if s_len > 1:
            for i in range(s_len):
                print(f"{i+1}: {searcher[i]}")

            print("0: Exit Search")
            f_term = int(input(f"select between 1 & {s_len}: ")) - 1
            if f_term + 1 >= 1 and f_term + 1 <= s_len:
                search(searcher[f_term])
            else:
                print("Exitting search")

        elif s_len == 1:
            search(searcher[0])
        else:
            print("Sorry result not found")

    else:
        if s_len > 1:
            for i in range(s_len):
                print(f"{i+1}: {searcher[i]}")

            print("0: Exit Search")
            f_term = int(input(f"select between 1 & {s_len}: ")) - 1
            if f_term + 1 >= 1 and f_term + 1 <= s_len:
                full_search(searcher[f_term])
            else:
                print("Exitting search")

        elif s_len == 1:
            full_search(searcher[0])
        else:
            print("Sorry result not found")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-s", "--search", type=str, help="pass term for searching wikipedia"
    )
    argparser.add_argument(
        "-F",
        "--full",
        action="store_true",
        help="output all the pagedata from wikipedia",
    )
    argparser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run the tool interactively(CTRL+C to quit)",
    )
    args = argparser.parse_args()

    if(is_online()):
        if args.full and args.search:
            term_search(args.search, True)
        elif args.search:
            term_search(args.search, False)
        else:
            while True:
                search_term = input("What do you want to search : ")
                term_search(search_term)
    else:
        print('System is offline')