import os
from common.dialogue import Dialogue as Dialog

class Command:

    def __init__(self, args):
        self.command = args.execute
        if self.command is True: 
            self.command = Dialog.get_command()
        
    def get_command(self) :
        return self.command