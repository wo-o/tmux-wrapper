import os
import re
import time
import inquirer
import requests
import json
import sys

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

        target_list = list()
        for i in range (start, end+1):
            target_list.append(prefix + str(i).zfill(len(suffix)))

        return target_list

    @staticmethod
    def parse_by_seperator(seperator_symbol, seperator):
        targets = Dialog.get_targets_for_seperator(seperator)
        return targets.split(seperator_symbol)

    @classmethod
    def parse_by_file(cls):
        file_name = Dialog.get_file_name()
        try:
            f = open(file_name, 'r')
            target_list = f.read().split('\n')
            f.close()
            target_list = list(filter(lambda x:x!='',target_list))
            return target_list
        except FileNotFoundError:
            Dialog.get_file_failed()
            sys.exit(0)
    
    @classmethod
    def select_parse_method(cls):
        try :
            method = Dialog.get_method_to_parse()
            if method == 'Comma'  : return cls.parse_by_seperator(' ', 'Comma')
            if method == 'File'   : return cls.parse_by_file()
            if method == 'Range'  : return cls.parse_by_range()
            if method == 'Space'  : return cls.parse_by_seperator(' ', 'Space')
        except TypeError: sys.exit(0)

