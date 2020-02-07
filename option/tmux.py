import argparse
import os

from colorama import Fore, Back, Style, init
init(autoreset=True)

from core.tmux import Tmux
from core.target import Target
from core.kerberos import Kerberos

class TmuxOption :

    @classmethod
    def handler(cls, args) :
        target_list = cls.get_target_list(args)
        if args.execute : 
            command = input(f'{Fore.GREEN}\n Type command to execute\n $ {Fore.RESET}')
            for target in target_list:
                print(f'{Fore.GREEN}\n{"="*20} {target}')
                os.system(f'ssh root@{target} ' + command)
                print(f'{Fore.GREEN}{"="*50}\n')
        else : cls.execute_tmux_with_ssh(args, target_list)

    @classmethod
    def get_target_list(cls, args) :
        if args.method : 
            target_list = Target.select_parse_method()
        else :
            target_list = Target.parse_by_default(args.target[0])
        return target_list

    @classmethod
    def execute_tmux_with_ssh(cls, args, target_list) :
        user = args.user if args.user else ['root']
        proxy = args.proxy if args.proxy else [None]
        pane_number = args.number if args.number else [9]
        Tmux(user=user[0], proxy=proxy[0], pane_number=pane_number[0], target_list=target_list).generate_tmux()


