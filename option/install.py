import os
import sys

from common.variable import PYTHON, CONSOLE_ROW, CONSOLE_COLUMN, BASE_DIR, HOME_DIR
from colorama import Fore, Back, Style, init
init(autoreset=True)

class InstallOption :

    @classmethod
    def handler(cls, args):
        cls.check_brew_installed()
        cls.check_tmux_installed()
        cls.set_tmux_config()
        cls.install_python_package()

    @staticmethod
    def check_brew_installed():
        print(f'{Fore.BLUE}\nCheck if Brew installed: ', end="")
        if not os.system('brew help > /dev/null 2>&1'): print(f'{Fore.GREEN}O')
        else : 
            print(f'{Fore.RED}X')
            print(f'{Back.RED}\nPlease install brew{Back.RESET}')
            sys.exit(0)

    @staticmethod
    def check_tmux_installed():
        print(f'{Fore.BLUE}Check if TMUX installed: ', end="")
        if not os.system('tmux ls > /dev/null 2>&1'): print(f'{Fore.GREEN}O')
        else : 
            print(f'{Fore.RED}X')
            print(f'{Back.RED}\nPlease install tmux{Back.RESET}')
            sys.exit(0)

    @staticmethod
    def set_tmux_config():
        print(f'{Fore.BLUE}\nSet TMUX config')
        print(f'{Fore.BLUE}{"="*CONSOLE_COLUMN}')

        if os.system(f'mv ~/.tmux.conf ~/.tmux.conf.bak > /dev/null 2>&1'):
            print(f'{Back.YELLOW}Please check {HOME_DIR}/.tmux.conf{Back.RESET}')
        else: print(f'{Fore.BLUE}Backup : {Fore.GREEN}{HOME_DIR}/.tmux.conf -> {HOME_DIR}/.tmux.conf.bak')

        if os.system(f'cp {BASE_DIR}/config/tmux.conf {HOME_DIR}/.tmux.conf > /dev/null 2>&1'): 
            print(f'{Back.RED}Please check {BASE_DIR}/config/tmux.conf{Back.RESET}')
            sys.exit(0)
        else: print(f'{Fore.BLUE}Copy   : {Fore.GREEN}{BASE_DIR}/config/tmux.conf -> {HOME_DIR}/.tmux.conf')

        print(f'{Fore.BLUE}{"="*CONSOLE_COLUMN}')

    @staticmethod
    def install_python_package():
        print(f'{Fore.BLUE}\nInstall Python package')
        print(f'{Fore.BLUE}{"="*CONSOLE_COLUMN}')
        ret = os.system(f'{PYTHON} -m pip install -r {BASE_DIR}/requirements.txt')
        print(f'{Fore.BLUE}{"="*CONSOLE_COLUMN}')
        if ret:
            print(f'{Back.RED}\nError occured while installing python package{Back.RESET}')
            sys.exit(0)
