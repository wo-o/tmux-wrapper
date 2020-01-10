import os
import re
import uuid
from common.font import *
from common.decorator import function_decorator


class Tmux:

    def __init__(self, user, proxy):
        self.user = user
        self.proxy = proxy
        self.session_id = uuid.uuid4().hex[:18].upper()
        os.system('tmux new-session -d -s ' + self.session_id)

    def connect_using_ssh(self):
        pass
        
    def make_panel(self, target):
        os.system('tmux set-window-option synchronize-panes off')
        os.system(f'tmux splitw -t {self.session_id} -h ssh -o StrictHostKeyChecking=no root@{target}')
        os.system('tmux select-layout tiled')
    
    def wrap_up(self):
        os.system('tmux set-window-option synchronize-panes on')
        os.system('tmux kill-pane -t 0')
        os.system('tmux select-layout tiled')
        os.system('tmux attach-session -t ' + self.session_id)
    
    def use_tmux(self):
        for t in self.target :
            self.make_panel(t)
        self.wrap_up()


class Stmux(Tmux):

    def __init__(self, user):
        self.user = user.strip()

    def make_panel(self, hostname):
        os.system('tmux set-window-option synchronize-panes off')
        os.system(f'tmux splitw -h ssh -o StrictHostKeyChecking=no -t {proxy} ssh -o StrictHostKeyChecking=no root@{hostname}')
        os.system('tmux select-layout tiled') 
