import argparse

class Option :
    __parser = argparse.ArgumentParser (
        description='JOPS - DevOPS Tool'
    )
    __subparser = __parser.add_subparsers (
        title='Command list',
        description='Main function for JOPS',
        dest="command"
    )
    @classmethod
    def get_args(cls) :
        cls.tmux_option()
        cls.wifi_option()
        cls.ansible_option()
        return cls.__parser.parse_args()

    @classmethod
    def tmux_option(cls) :
        tmux_parser = cls.__subparser.add_parser(
            'tmux', help='Using TMUX',
            aliases=['t']
        )
        tmux_parser.add_argument (
            '-t', '--target', 
            type=str, nargs='+', metavar=('Host'), 
            help='Type host to connect with tmux ( hostname#s:e )'
        )
        tmux_parser.add_argument (
            '-u', '--user', 
            type=str, nargs=1, metavar=('User'), 
            help='Type user to connect'
        )
        tmux_parser.add_argument (
            '-p', '--proxy', 
            type=str, nargs=1, metavar=('Host'), 
            help='Type host providing a proxy with user ( user@host )'
        )
        tmux_parser.add_argument (
            '-n', '--number', 
            type=int, nargs=1, metavar=('Number'), 
            help='Type number of panes in one window'
        )
        tmux_parser.add_argument (
            '-m', '--method', 
            action="store_true",
            help='Choose method to parse'
        )

    @classmethod
    def wifi_option(cls) :
        wifi_parser = cls.__subparser.add_parser(
            'wifi', help='Handling Wifi',
            aliases=['w']
        )
        wifi_parser.add_argument (
            '-c', '--proxy', 
            type=str, nargs=1, metavar=('Host'), 
            help='Type host providing a proxy'
        )

    @classmethod
    def ansible_option(cls) :
        ansible_parser = cls.__subparser.add_parser(
            'ansible', help='Using Ansible',
            aliases=['a']
        )