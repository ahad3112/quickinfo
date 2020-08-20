'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
        * ....

    Source:
        https://www.pdc.kth.se/support/documents/data_management/data_management.html
'''

import os

from utilities.colors import Colors
from utilities.formatting import justify

__line_width = 120
__username = os.popen('whoami').read().strip()

__file_systems = {
    'afs': {
        'name': ' '.join('AFS'),
        'location': r'/afs/pdc.kth.se',
        'home': f'/afs/pdc.kth.se/home/{__username[0]}/{__username}',
        'web': r'https://www.pdc.kth.se/support/documents/data_management/afs.html',
        'quickinfo': justify(
            ('The Andrew File System (AFS) is a distributed file system'
             ' which uses a set of trusted servers to present a homogeneous, '
             ' location-transparent file name space to all the client workstations.'),
            __line_width
        ),
        'info_format': ('{3.HEADER}{0:{1}}\n{2[name]:^{1}}\n{0:{1}}'
                        '\n{3.Reset}{2[quickinfo]:<{1}}\n'
                        '\n{3.Red}LOCATION : {3.Reset}{2[location]:<{1}}'
                        '\n{3.Red}HOME     : {3.Reset}{2[home]:<{1}}'
                        '\n{3.Red}WEB      : {3.Reset}{2[web]:<{1}}\n')
    },
    'lustre': {
        'name': ' '.join('LUSTRE'),
        'location': r'/cfs/klemming',
        'home': f'/cfs/klemming/home/{__username[0]}/{__username}',
        'nobackup': f'/cfs/klemming/nobackup/{__username[0]}/{__username}',
        'scratch': f'/cfs/klemming/scratch/{__username[0]}/{__username}',
        'web': r'https://www.pdc.kth.se/support/documents/data_management/lustre.html',
        'quickinfo': justify(
            ('The Lustre system is a parallel file system'
             ' optimized for handling data from many clients at the same time.'),
            __line_width
        ),
        'info_format': ('{3.HEADER}{0:{1}}\n{2[name]:^{1}}\n{0:{1}}'
                        '\n{3.Reset}{2[quickinfo]:<{1}}\n'
                        '\n{3.Red}LOCATION : {3.Reset}{2[location]:<{1}}'
                        '\n{3.Red}HOME     : {3.Reset}{2[home]:<{1}}'
                        '\n{3.Red}NOBACKUP : {3.Reset}{2[nobackup]:<{1}}'
                        '\n{3.Red}SCRATCH  : {3.Reset}{2[scratch]:<{1}}'
                        '\n{3.Red}WEB      : {3.Reset}{2[web]:<{1}}\n')
    }
}


def handler(args):
    # Displaying filesystems
    for filesystem in args.filesystems:
        filesystem = __file_systems.get(filesystem, 'None')
        if filesystem:
            print(filesystem.get('info_format', 'Not Available').format(
                '-' * __line_width,
                __line_width - 11,
                filesystem, Colors
            ))


def add_filesystems_cli(subparsers):
    fs_parser = subparsers.add_parser(
        'fs',
        help=r'Some usefule information on "filesystem" at PDC',
        description=r'This submodule provides usefull information on "PDC" filesystem',
    )

    fs_parser.set_defaults(handler=handler)

    fs_parser.add_argument(
        '--filesystems',
        choices=['afs', 'lustre'],
        nargs='+',
        help='Choose the filesystem. (default ["afs", "lustre"])',
        default=['afs', 'lustre']
    )
