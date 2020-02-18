import os, sys

PYTHON='/usr/local/bin/python3'
CONSOLE_SQUARE = os.popen('stty size', 'r').read().split()
CONSOLE_ROW, CONSOLE_COLUMN = CONSOLE_SQUARE
CONSOLE_ROW = int(CONSOLE_ROW)
CONSOLE_COLUMN = int(CONSOLE_COLUMN)
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
HOME_DIR = os.path.abspath(os.path.dirname('~'))