import os
from common.dialogue import Dialogue as Dialog

class SSH:

    def __init__(self, args):
        self.command = self.get_command_to_execute(args)
        self.proxy = f' ssh -t {args.proxy} -o StrictHostKeyChecking=no ' if args.proxy else ''
        self.secret = f' sshpass -p {args.secret} ' if args.secret else ''
        self.user = args.user[0] if args.user else 'root'

    def get_ssh_command(self, target) :
        return (
            f' {self.proxy} ' +
            f' {self.secret} ' +
            f' ssh -o StrictHostKeyChecking=no ' +
            f' {self.user}@{target} ' +
            f' {self.command} '
        )

    def execute_ssh_command(self, target) :
        Dialog.start_ssh(target)
        os.system (
            f' {self.proxy} ' +
            f' {self.secret} ' +
            f' ssh -o StrictHostKeyChecking=no ' +
            f' {self.user}@{target} ' +
            f' {self.command} '
        )
        Dialog.end_ssh()

    @classmethod 
    def get_command_to_execute(cls, args):
        # if args.execute == True: return Dialog.get_command()
        if args.execute: return args.execute
        else: return ''
       