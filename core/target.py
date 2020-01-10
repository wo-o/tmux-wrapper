import os
import re
import time
import inquirer
import requests
import json
import sys

# from common.font import *
from common.decorator import method_decorator
from common.decorator import function_decorator
from common.dialogue import Dialogue as Dialog

class Target:
    @staticmethod
    def parse_by_default(arg):
        [prefix, suffix] = arg.split('#')
        [start, end] = suffix.split(':')
        length = len(start)

        target = list()
        for i in range(int(start), int(end)+1) :
            target.append(prefix + str(i).zfill(length))
        
        return target
        
    @staticmethod
    def parse_by_range():
        target = Dialog.get_target()

        suffix = re.findall('\d+', target)[-1]
        prefix = target.split(suffix[0])[0]

        start = int(suffix)
        end = Dialog.get_range(int(start))

        target = list()
        for i in range (start, end+1):
            target.append(prefix + str(i).zfill(len(suffix)))

        return target

    @staticmethod
    def parse_by_space():
        @function_decorator
        def set_hostlist():
            hostlist= input('Type hostlist seperated by blank\n=> ')
            if not hostlist: 
                set_hostlist()
            return hostlist
        hostlist = set_hostlist()

        return hostlist.split()

    @staticmethod
    def parse_by_comma():
        @function_decorator
        def set_hostlist():
            hostlist= input('Type hostlist seperated by comma\n=> ')
            if not hostlist: 
                set_hostlist()
            return hostlist
        hostlist = set_hostlist()

        return hostlist.split(',')

    @classmethod
    def parse_by_file(cls):
        @function_decorator
        def set_filename():
            filename = input('Type filename with path : ')
            if not filename: 
                return set_filename()
            return filename
        filename = set_filename()

        try:
            f = open(filename, 'r')
            hostlist = f.read().split('\n')
            f.close()
            hostlist = list(filter(lambda x:x!='',hostlist))
            return hostlist
        except:
            print(FAIL + 'Cannot find the file' + END)
            return cls.set_hostlist_by_file()
    
    @staticmethod
    def print_menu():
        choices = [
            'Range', 
            'Space', 
            'Comma', 
            'File',
            'Domain'
        ]
        selector = [
            inquirer.List(
                'method',
                message = "Choose method to make access list",
                choices = choices
            ),
        ]

        return inquirer.prompt(selector)
    
    @classmethod
    def select_parse_method(cls):
        try :
            selector = None
            while not selector :
                selector = cls.print_menu()['method']
        except TypeError :
            sys.exit(0)

        if selector == 'Range'  : return cls.parse_by_range()
        if selector == 'Space'  : return cls.parse_by_space()
        if selector == 'Comma'  : return cls.parse_by_comma()
        if selector == 'File'   : return cls.parse_by_file()