#!/usr/bin/env python

'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>

    Usage:
        $ quickinfo.py -h

    Description:
        Write some documentation about common specific questions on that cluster.
        Examples:
            * where the filesystems are and how to reach
            * it SNIC variables
            * submit how to
            * Link to support documentation etc...
            * compiler settings
            * SLURM example
            *
'''

import argparse


from modules.filesystems import add_filesystems_cli
from modules.snic import add_snic_cli
from modules.jobsubmit import add_jobsubmit_cli
from modules.softwares import add_softwares_cli
from modules.clusters import add_clusters_cli


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This script answers for some common questions on cluster.',
    )

    subparsers = parser.add_subparsers(
        title=f'Available submodules',
        description='Submodules allows to get info regarding snic, filesystems, job submission',
        required=False,
    )

    add_filesystems_cli(subparsers)
    add_snic_cli(subparsers)
    add_jobsubmit_cli(subparsers)
    add_softwares_cli(subparsers)
    add_clusters_cli(subparsers)

    args = parser.parse_args()

    # handling users input
    try:
        args.handler(args)
    except AttributeError:
        raise RuntimeError('Implementation Error : No handler found!!!')

    # if args.handler:
    #     args.handler(args)
