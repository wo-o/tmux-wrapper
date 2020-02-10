import argparse

from core.tmux import Tmux
from core.target import Target
from core.kerberos import Kerberos

class AnsibleOption :

    @classmethod
    def handler(cls, args) :
        target_list = cls.get_target_list(args)
        # cls.execute_tmux_with_ssh(args, target_list)

    @classmethod
    def get_target_list(cls, args) :
        if args.method : 
            target_list = Target.select_parse_method()
        else :
            target_list = Target.parse_by_default(args.target[0])
        return target_list

    @classmethod
    def execute_tmux_with_ssh(cls, args, target_list) :
        Tmux(args, target_list=target_list).generate_tmux()


