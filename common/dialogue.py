import inquirer

from colorama import Fore, Back, Style, init
from common.variable import PYTHON, CONSOLE_ROW, CONSOLE_COLUMN, BASE_DIR, HOME_DIR
init(autoreset=True)
# Fore: BLACK, RED, BLUE, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, BLUE, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

class Dialogue :

# 
# Divider
# 
    @staticmethod
    def print_divider() :
        print(f'{Fore.BLUE}{"="*CONSOLE_COLUMN}')
# 
# Target: Seperator
# 
    @staticmethod
    def get_target_by_seperator(seperator) :
        target = None
        print(f'{Fore.BLUE} Type targets seperated by {seperator}')
        while not target :
            target = input(f'{Fore.BLUE} => {Fore.RESET}{Fore.CYAN}')
        return target
#
# Target: Range
#
    @staticmethod
    def get_first_target() :
        target = None
        print(f' {Fore.BLUE}Type first target{Fore.RESET} ' +
            f'{Fore.CYAN}(The target should include number)')
        while not target :
            target = input(f'{Fore.BLUE} => {Fore.RESET}{Fore.CYAN}')
        print()
        return target

    @staticmethod
    def fail_to_get_target_number():
        print(f' {Back.RED}There is no number{Back.RESET}{Fore.CYAN}')


    @staticmethod
    def get_last_target_number(start) :
        end = -1
        print(f'{Fore.BLUE} Type last target number {Fore.RESET}' + 
            f'{Fore.CYAN}(Enter greater than or equal to {start})')
        while start > end :
            end = int(input(f'{Fore.BLUE} => #{Fore.RESET}{Fore.CYAN}'))
        return end
# 
# Target: File 
# 
    @staticmethod
    def get_file_name() :
        file_name = None
        print(f'{Fore.BLUE} Type file name with path {Fore.RESET}')
        while not file_name :
            file_name = input(f'{Fore.BLUE} => {Fore.RESET}{Fore.CYAN}')
        print()
        return file_name

    @staticmethod
    def fail_to_get_file_name() :
        print(f' {Back.RED}Cannot find the file{Back.RESET}')
#     
# Target: Textarea
#     
    @staticmethod
    def start_textarea() :
        print(f'{Fore.BLUE} Type bulk of targets {Fore.RESET}' + 
            f'{Fore.CYAN}(Need "-" at the end of the target) {Fore.RESET}')

    @staticmethod
    def get_textarea() :
        return input(f'{Fore.CYAN}')

    @staticmethod
    def get_textarea_failed() :
        print(f'{Fore.RED} Cannot get targets\n')
#
# Target: Method
#
    @staticmethod
    def get_method_to_parse():
        print()
        choices = [
            f'{Fore.CYAN}Comma{Fore.RESET}', 
            f'{Fore.CYAN}Space{Fore.RESET}', 
            f'{Fore.CYAN}File{Fore.RESET}',
            f'{Fore.CYAN}Range{Fore.RESET}', 
            f'{Fore.CYAN}Textarea{Fore.RESET}'
        ]
        selector = [
            inquirer.List(
                'method',
                message = f'{Fore.BLUE}Choose method to get target{Fore.RESET}',
                choices = choices
            ),
        ]

        method = None
        while not method :
            method = inquirer.prompt(selector)['method']
        return method
#
# SSH 
# 
    @staticmethod
    def print_user_prompt(user, target, command): 
        print(f'{Fore.CYAN}[{user}@{target}]# {command}{Fore.RESET}')
#
# Command
#
    @staticmethod
    def get_command() :
        command = None
        print(f'{Fore.BLUE}\n Type command to execute')
        while not command :
            command = input(f'{Fore.BLUE} $ {Fore.RESET}{Fore.CYAN}')
        return command