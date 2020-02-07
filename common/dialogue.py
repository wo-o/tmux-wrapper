import inquirer
from colorama import Fore, Back, Style, init
init(autoreset=True)
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

class Dialogue :

    @staticmethod
    def get_target() :
        target = None
        while not target :
            target = input(f'{Fore.GREEN} Type target : ')
        print()
        return target

    @staticmethod
    def get_range(start) :
        end = -1
        while start > end :
            end = int(input(f'{Fore.GREEN} Select range. Type greater than or equal to {start} : '))
        print()
        return end

    @staticmethod
    def get_targets_for_seperator(seperator) :
        targets = list()
        while not targets :
            print(f'{Fore.GREEN} Type targets seperated by {seperator}')
            targets = input(f'{Fore.GREEN} $ {Fore.RESET}')
        print()
        return targets

    @staticmethod
    def get_file_name() :
        file_name = None
        while not file_name :
            file_name = input(f'{Fore.GREEN} Type file with path : ')
        print()
        return file_name

    @staticmethod
    def get_file_failed() :
        print(f'{Fore.RED} Cannot find the file\n')
    
    @staticmethod
    def start_textarea() :
        print(f'{Fore.GREEN} Type bulk of hostname\n{"="*30}\n')

    @staticmethod
    def end_textarea() :
        print(f'{Fore.GREEN}{"="*30}')

    @staticmethod
    def get_textarea_failed() :
        print(f'{Fore.RED} Cannot get targets\n')

    @staticmethod
    def get_method_to_parse():
        print()
        choices = [
            'Comma', 
            'File',
            'Range', 
            'Space', 
            'Textarea'
        ]
        selector = [
            inquirer.List(
                'method',
                message = f'{Fore.GREEN}Choose method to get targets',
                choices = choices
            ),
        ]

        method = None
        while not method :
            method = inquirer.prompt(selector)['method']
        return method

