import inquirer
from colorama import Fore, Back, Style, init
init(autoreset=True)
# Fore: BLACK, RED, BLUE, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, BLUE, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

class Dialogue :

    @staticmethod
    def get_target() :
        target = None
        while not target :
            target = input(f'{Fore.BLUE} Type target : ')
        print()
        return target

    @staticmethod
    def get_range(start) :
        end = -1
        while start > end :
            end = int(input(f'{Fore.BLUE} Select range. Type greater than or equal to {start} : '))
        print()
        return end

    @staticmethod
    def get_targets_for_seperator(seperator) :
        targets = list()
        while not targets :
            print(f'{Fore.BLUE} Type targets seperated by {seperator}')
            targets = input(f'{Fore.BLUE} $ {Fore.RESET}')
        print()
        return targets

    @staticmethod
    def get_file_name() :
        file_name = None
        while not file_name :
            file_name = input(f'{Fore.BLUE} Type file with path : {Fore.RESET}')
        print()
        return file_name

    @staticmethod
    def get_file_failed() :
        print(f'{Fore.RED} Cannot find the file\n')
    
    @staticmethod
    def start_textarea() :
        print(f'{Fore.BLUE} Type bulk of target\n{"="*30}\n')

    @staticmethod
    def end_textarea() :
        print(f'{Fore.BLUE}\n{"="*30}')

    @staticmethod
    def get_textarea_failed() :
        print(f'{Fore.RED} Cannot get targets\n')


    @staticmethod
    def start_ssh(target) :
        print(f'{Fore.BLUE}\n{"="*100} {Fore.CYAN}{target}\n')

    @staticmethod
    def end_ssh() :
        print(f'{Fore.BLUE}\n{"="*120}\n')

    @staticmethod
    def get_command() :
        command = None
        print(f'{Fore.BLUE}\n Type command to execute')
        while not command :
            command = input(f'{Fore.BLUE} $ {Fore.RESET}')
        return command

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
                message = f'{Fore.BLUE}Choose method to get targets',
                choices = choices
            ),
        ]

        method = None
        while not method :
            method = inquirer.prompt(selector)['method']
        return method

