'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....
'''

__submit_jobs_info = {
    'interactive': {
        'Tegner': {

        },
        'Beskow': {

        }
    },
    'queue': {
        'Tegner': {

        },
        'Beskow': {

        }
    }
}


def handler(args):
    print(f'This method deals with submitting jobs at PDC: {args}')


def add_jobsubmit_cli(subparsers):
    js_parser = subparsers.add_parser(
        'js',
        help=r'Quick information on submitting jobs at "PDC"',
        description=r'This submodule provides all information regarding submitting jobs at PDC',
    )

    js_parser.set_defaults(handler=handler)

    # option
    # mutually exclusive group
    group = js_parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--interactive', action="store_true",
                       help='Information on running jobs interactively.')
    group.add_argument('-q', '--queue', action="store_true",
                       help='Information on queueing jobs.')

    # other optional arguments
    js_parser.add_argument('-c', choices=['Tegner', 'Beskow'],
                           nargs='+',
                           help="Specify the cluster to be queried (default : [Tegner, Beskow])",
                           default=['Tegner', 'Beskow'])
