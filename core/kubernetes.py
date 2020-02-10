import os
from common.dialogue import Dialogue as Dialog

class SSH:

    def __init__(self, args):
        self.command = self.get_command() if args.execute else ''
        self.proxy = f' ssh -t {args.proxy} -o StrictHostKeyChecking=no ' if args.proxy else ''
        self.secret = f' sshpass -p {args.secret} ' if args.secret else ''
        self.user = args.user[0] if args.user else 'root'

    def execute_ssh(self, target) :
        return (
            f' {self.proxy} ' +
            f' {self.secret} ' +
            f' ssh -o StrictHostKeyChecking=no ' +
            f' {self.user}@{target} ' +
            f' {self.command} '
        )

    @classmethod 
    def get_command(cls):
        return Dialog.get_command()