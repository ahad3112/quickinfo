'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * How to activate SNIC variables
        * List all SNIC variables with
    Source:
        * https://www.pdc.kth.se/support/documents/data_management/data_management.html#snic-environmental-variables
'''


__snic_variables = {
    'SNIC_BACKUP': 'Folder for backing up important data. (default : your AFS home directory)',
}


def handler(args):
    print(f'This method deal with snic module: {args}')


def add_snic_cli(subparsers):
    snic_parser = subparsers.add_parser(
        'snic',
        help=r'information center for "SNIC"',
        description=r'This submodule provides all information on "SNIC"',
    )

    snic_parser.set_defaults(handler=handler)
