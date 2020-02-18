import argparse

class Option :
    __parser = argparse.ArgumentParser (
        description="JOPS - Jinn's operation tool"
    )
    __subparser = __parser.add_subparsers (
        title='Command list',
        description='Main command for JOPS',
        dest="command"
    )
    @classmethod
    def get_args(cls) :
        cls.default_option()
        cls.ansible_option()
        cls.install_option()
        # cls.wifi_option()
        return cls.__parser.parse_args()

    @classmethod
    def default_option(cls) :
        default_parser = cls.__parser        
        default_parser.add_argument (
            '-n', '--number', 
            type=int, nargs=1, metavar=('Number'), 
            help='Type number of panes in one window'
        )
        default_parser.add_argument (
            '-p', '--proxy', 
            type=str, nargs=1, metavar=('Host'), 
            help='Type host providing a proxy with user ( user@host )'
        )
        default_parser.add_argument (
            '-s', '--secret', 
            type=str, nargs=1, metavar=('Password'), 
            help='Type password for access'
        )
        default_parser.add_argument (
            '-t', '--target', 
            type=str, nargs='?', 
            default=False,
            metavar=('Target'), 
            help='Type target to manage( target#s:e )'
        )
        default_parser.add_argument (
            '-u', '--user', 
            type=str, nargs=1, metavar=('User'), 
            help='Type user to connect'
        ) 
        default_parser.add_argument (
            '-x', '--execute', 
            type=str, nargs='?',
            default=False,
            const=True,
            metavar=('Command'),
            help='Type command to execute'
        ) 
        # default_parser.add_argument (
        #     '-k', '--kubernetes', 
        #     action='store_true',
        #     help='Make target as Kubernetes pod'
        # )

    @classmethod
    def install_option(cls) :
        cls.__subparser.add_parser(
            'install', help='Install Jops',
            aliases=['i']
        )
    @classmethod
    def ansible_option(cls) :
        ansible_parser = cls.__subparser.add_parser(
            'ansible', help='Using Ansible',
            aliases=['a']
        )
    @classmethod
    def kubernetes_option(cls) :
        kubernetes_parser = cls.__subparser.add_parser(
            'kubernetes', help='Using Kubernetes',
            aliases=['k']
        ) 

    # @classmethod
    # def wifi_option(cls) :
    #     wifi_parser = cls.__subparser.add_parser(
    #         'wifi', help='Handling Wifi',
    #         aliases=['w']
    #     )
    #     wifi_parser.add_argument (
    #         '-c', '--proxy', 
    #         type=str, nargs=1, metavar=('Host'), 
    #         help='Type host providing a proxy'
    #     )