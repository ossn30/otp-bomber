import sys
import random
import os
try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)

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
