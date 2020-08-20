'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....
'''


def handler(args):
    print(f'This method deals with submitting jobs at PDC: {args}')


def add_jobsubmit_cli(subparsers):
    js_parser = subparsers.add_parser(
        'js',
        help=r'information on submitting jobs at "PDC"',
        description=r'This submodule provides all information regarding submitting jobs at PDC',
    )

    js_parser.set_defaults(handler=handler)

    # fs_parser.add_argument('filesystem', choices=['afs', 'lustre'])
