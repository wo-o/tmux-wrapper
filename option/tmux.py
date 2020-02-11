import argparse
import os

from colorama import Fore, Back, Style, init
init(autoreset=True)

from core.tmux import Tmux
from core.target import Target
from core.kerberos import Kerberos
from core.ssh import SSH

class TmuxOption :

    @classmethod
    def get_target_list(cls, args) :
        if args.target : 
            target_list = Target.parse_by_default(args.target)
        else :
            target_list = Target.select_parse_method()
        return target_list

    @classmethod
    def handler(cls, args) :
        ssh = SSH(args)
        target_list = cls.get_target_list(args)
        tmux = Tmux(
                    args=args,
                    ssh=ssh,
                )

        for index, target in enumerate(target_list) :
            if args.execute: ssh.execute_ssh_command(target)
            else: tmux.generate_tmux(target, index)
        if not args.execute: tmux.wrap_up()
        



