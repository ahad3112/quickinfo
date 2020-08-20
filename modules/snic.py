'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * How to activate SNIC env
        * List of all SNIC-ENV variables
    Source:
        * https://www.pdc.kth.se/support/documents/data_management/data_management.html#snic-environmental-variables
'''

# from utilities.colors import Colors
from utilities.formatter import justify, Colors, Style


__line_width = 150

__snic_variables = {
    'name': ' '.join('SNIC'),
    'quickinfo': justify(
        ('To simplify for the users how to find different folders,'
            ' SNIC has provided a number of specific variables'
            ' which indicate in which folders data should be stored.'
            ' On "Beskow" the module "snic_env" is loaded by default but'
            ' in order to access these variables on "Tegner", a module must be loaded'),
        __line_width
    ),
    'var_list_title': 'SNIC Variables',
    'module_activate_title': 'Activate SNIC Module',
    'activate': 'module add snic-env',
    'SNIC_BACKUP': r'Folder for backing up important data. (default : your AFS home directory)',
    'SNIC_NOBACKUP': r'Not backed up folder for large data which resides in /cfs/klemming/nobackup',
    'SNIC_RESOURCE': r'Name of the cluster you are logged into',
    'SNIC_SITE': r'Name of the site, i.e. PDC',
    'SNIC_TMP': r'Scratch folder for storing temporary data which resides in /cfs/klemming/scratch',
    'var_value_title': 'Example of getting variable value',
    'echo_var': 'echo $<variable_name>',
    'info_format': ('{0:=<{1}}\n{3.HEADER}{2[name]:^{1}}{3.RESET}\n{0:=<{1}}'
                    '\n{3.RESET}{2[quickinfo]:<{1}}\n'
                    '\n{3.TITLE}{2[module_activate_title]}'
                    '\n{3.RESET}{2[activate]}\n'
                    '\n{3.TITLE}{2[var_list_title]}{3.RESET}'
                    '\n{3.KEYWORD}SNIC_BACKUP   : {3.RESET}{2[SNIC_BACKUP]:<{1}}'
                    '\n{3.KEYWORD}SNIC_NOBACKUP : {3.RESET}{2[SNIC_NOBACKUP]:<{1}}'
                    '\n{3.KEYWORD}SNIC_RESOURCE : {3.RESET}{2[SNIC_RESOURCE]:<{1}}'
                    '\n{3.KEYWORD}SNIC_SITE     : {3.RESET}{2[SNIC_SITE]:<{1}}'
                    '\n{3.KEYWORD}SNIC_TMP      : {3.RESET}{2[SNIC_TMP]:<{1}}\n'
                    '\n{3.TITLE}{2[var_value_title]}'
                    '\n{3.RESET}{2[echo_var]}\n'
                    )
}


def handler(args):
    print(__snic_variables.get('info_format', 'Not Available').format(
        '=',
        __line_width,
        __snic_variables,
        Style
    ))


def add_snic_cli(subparsers):
    snic_parser = subparsers.add_parser(
        'snic',
        help=r'Quickinfo on "SNIC" at "PDC"',
        description=r'This submodule provides some quick information on "SNIC" at "PDC"',
    )

    snic_parser.set_defaults(handler=handler)
