import os
import uuid

class Kerberos:
    __id=''

    @staticmethod
    def destroy_kerberos() :
        return os.system('kdestroy')
    
    @staticmethod
    def check_kerberos() : # if already typed kinit, klist might return 0 
        return os.system('klist > /dev/null')
    
    @classmethod
    def init_kerberos(cls) : # kinit with the id in /tmp 
        session_id = uuid.uuid4().hex[:18].upper()
        os.system(f'tmux new -d -s {session_id}')
        os.system(f'tmux send-keys -t {session_id} "kinit {cls.__id}" ENTER')
        os.system(f'tmux kill-session -t {session_id}')
        os.system(f'kinit --keychain {cls.__id}') # --keychain save your id in your PC, if you are using MACOS

    @classmethod
    def set_kerberos(cls) :
        while not cls.__id :
            cls.__id = input('Type kerberos id : ')
        print()
        os.system(f'echo {cls.__id} > ./.kerberos_id')
    
    @classmethod
    def use_kerberos(cls) :

        # if already typed kinit then return
        print(HEADER+'Check kerberos\n'+END)
        if not cls.check_kerberos(): 
            return 

        # if there is kerberos id in /tmp
        try:
            with open('./.kerberos_id','r') as f :
                cls.__id = f.readline()
                print(OKGREEN + '\nFound id : ' + cls.__id + END)
                print(WARNING + 'If the id is wrong, please remove kerberos_id\n' + END)

        # if there is no kerberos id in ~/.midgard
        except: 
            print(WARNING + 'There is no kerberos id information\n' + END)
            cls.set_kerberos()

        cls.init_kerberos()
