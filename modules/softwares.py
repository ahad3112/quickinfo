'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....
'''


def handler(args):
    print(f'This method deals with Softwares module: {args}')


def add_softwares_cli(subparsers):
    sp = subparsers.add_parser(
        'softwares',
        help=r'"Softwares" related information at "PDC"',
        description=r'This module contains some useful information about "Softwares" at "PDC"'
    )

    sp.set_defaults(handler=handler)
