from rich import print
from modules.menu import *
from rich.console import Console

#this is gonna be the api we will be pulling from to see the previous spacex launches
# check to see if we can look at future launches in the future
BASE_API_URL = "https://api.spacexdata.com/v5/launches"



def main():
    print_menu()


if __name__ == "__main__":
    main()


