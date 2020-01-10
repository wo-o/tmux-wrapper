import argparse

from core.tmux import Tmux
from core.target import Target
from core.kerberos import Kerberos

class TmuxOption :

    @classmethod
    def handler(cls, args) :
        taget_list = cls.get_target_list(args)

    @classmethod
    def get_target_list(cls, args) :
        if args.method : 
            target = Target.select_parse_method()
        else :
            target = Target.parse_by_default(args.target[0])

    @classmethod
    def execute_tmux_with_ssh(cls, args, target_list) :
        user = args.user if args.user else 'root'
        proxy = args.proxy if args.proxy else None
        tmux = Tmux()


