import os
import re
import uuid

class Tmux:

    def __init__(self, user, proxy, target_list, pane_number):
        self.user = user
        self.proxy = proxy
        self.pane_number = pane_number
        self.window_number = 0
        self.target_list = target_list
        self.session_id = uuid.uuid4().hex[:18].upper()

    def make_panel(self, target):
        if self.proxy :
            os.system(f'tmux splitw -t {self.session_id}:{self.window_number} -h ssh -t {self.proxy} -o StrictHostKeyChecking=no ssh -o StrictHostKeyChecking=no {self.user}@{target}')
        else :
            os.system(f'tmux splitw -t {self.session_id}:{self.window_number} -h ssh -o StrictHostKeyChecking=no {self.user}@{target}')
        os.system('tmux set-window-option synchronize-panes on')
        os.system(f'tmux select-layout tiled')
    
    def wrap_up(self):
        for num in range(self.window_number+1) :
            os.system(f'tmux select-window -t {self.session_id}:{num}')
            os.system(f'tmux kill-pane -t {self.session_id}:{num}.0')
            os.system('tmux select-layout tiled')
        os.system(f'tmux attach-session -t {self.session_id}:0')

    def generate_tmux(self):
        self.window_number = 0
        os.system(f'tmux new-session -d -s {self.session_id}')
        for index, target in enumerate(self.target_list) :
            if index and ((index % self.pane_number) == 0) :
                self.window_number+=1
                os.system(f'tmux new-window -t {self.session_id}')
            self.make_panel(target)
        self.wrap_up()