import os
import time
import functools
import subprocess

print = functools.partial(print, flush=True)

class Wifi:
    dev='en0'
    cwifi=''

    @classmethod
    @method_decorator    
    def change_wifi(cls) :
        twifi=''
        cwifi=cls.get_wifi()
        if cwifi not in cls.wifi:
            os.system('networksetup -removepreferredwirelessnetwork '+cls.dev+' '+cwifi)
        for i in cls.wifi:
            os.system('networksetup -removepreferredwirelessnetwork '+cls.dev+' '+i)
            if i!=cwifi:twifi=i

        os.system('networksetup -addpreferredwirelessnetworkatindex '+cls.dev+' '+twifi+' 0 WPA2E')
        os.system('networksetup -setairportpower '+cls.dev+' off')
        os.system('networksetup -setairportpower '+cls.dev+' on')
        print('\n\nConnecting to '+twifi+'\n')
    
        while cwifi!=twifi :
            cwifi=cls.get_wifi()
            #time.sleep(0.5)
            print('.', end='')
        print('Connected')

    @classmethod
    def get_wifi(cls) :
        cwifi=subprocess.check_output("networksetup -getairportnetwork en0 | cut -d ':' -f2",shell=True)
        cwifi=cwifi[:-1].strip().decode()
        return cwifi
    
    @classmethod
    @method_decorator    
    def check_muzi(cls) :
        cwifi=cls.get_wifi()
        if cwifi!='muzi_wlan':cls.change_wifi()
        else : print(OKGREEN+'Already connected to muzi_wlan'+END)
