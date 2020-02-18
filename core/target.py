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
        try:
            [prefix, suffix] = arg.split('#')
            [start, end] = suffix.split(':')
        except ValueError:
            return [arg]

        length = len(start)
        target = list()
        for i in range(int(start), int(end)+1) :
            target.append(prefix + str(i).zfill(length))
        
        return target
        
    @staticmethod
    def parse_by_range():
        target = Dialog.get_first_target()

        try:
            suffix = re.findall('\d+', target)[-1]
            prefix = target.split(suffix[0])[0]
        except IndexError:
            Dialog.fail_to_get_target_number()
            sys.exit(0)

        start = int(suffix)
        end = Dialog.get_last_target_number(int(start))

        target_list = list()
        for i in range (start, end+1):
            target_list.append(prefix + str(i).zfill(len(suffix)))

        return target_list

    @staticmethod
    def parse_by_seperator(seperator_symbol, seperator):
        target = Dialog.get_target_by_seperator(seperator)
        return target.split(seperator_symbol)

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
            Dialog.fail_to_get_file_name()
            sys.exit(0)
    
    @classmethod
    def parse_by_textarea(cls):
        Dialog.start_textarea()
        Dialog.print_divider()
        
        target_list = list()
        while True:
            i = Dialog.get_textarea().split(' ')[0].strip()
            if i == '': continue
            if i == '-': break
            target_list.append(i)

        Dialog.print_divider()
        return target_list


    @classmethod
    def select_parse_method(cls):
        try :
            method = Dialog.get_method_to_parse()
            if 'Comma' in method  : return cls.parse_by_seperator(',', 'Comma')
            if 'Space' in method: return cls.parse_by_seperator(' ', 'Space')
            if 'File' in method: return cls.parse_by_file()
            if 'Range' in method: return cls.parse_by_range()
            if 'Textarea' in method : return cls.parse_by_textarea()
        except TypeError: sys.exit(0)

