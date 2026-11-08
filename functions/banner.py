import sys
import random
import os
import requests
from colorama import Fore, Style

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

def bann_text():
    os.system("clear")
    logo = """
     ▗▄▖▗▄▄▄▖▗▄▄▖     ▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖ 
    ▐▌ ▐▌ █  ▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌
    ▐▌ ▐▌ █  ▐▛▀▘     ▐▛▀▚▖▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖
    ▝▚▄▞▘ █  ▐▌       ▐▙▄▞▘▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌                         
                                                 """
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print()
