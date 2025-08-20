import random
from choose_gender import init_choose

def main():
    print("choose language: \n 1 - Русский \n 2 - English")
    lang = int(input(">> "))
    init_choose(lang)

if __name__ == "__main__":
    main()
