import os
import re
import uuid

class Tmux:

    def __init__(self, args, ssh=False, kubernetes=False):
        self.session_id = uuid.uuid4().hex[:18].upper()
        os.system(f'tmux new-session -d -s {self.session_id}')
        
        self.pane_number = args.number[0] if args.number else 9
        self.ssh = ssh
        self.window_number = 0

    def exectue_ssh(self, target):
        os.system(
            f' tmux splitw -t {self.session_id}:{self.window_number} -h ' +
            f' {self.ssh.get_ssh_command(target)} '
        )

    def make_panel(self, target):
        self.exectue_ssh(target)
        os.system(f' tmux set-window-option synchronize-panes on ')
        os.system(f' tmux select-layout tiled ')
    
    def wrap_up(self):
        for num in range(self.window_number+1) :
            os.system(f' tmux select-window -t {self.session_id}:{num} ')
            os.system(f' tmux kill-pane -t {self.session_id}:{num}.0 ')
            os.system(' tmux select-layout tiled ')
        os.system(f' tmux attach-session -t {self.session_id}:0 ')

    def generate_tmux(self, target, index):
        if index and ((index % self.pane_number) == 0) :
            self.window_number+=1
            os.system(f'tmux new-window -t {self.session_id}')
        self.make_panel(target)