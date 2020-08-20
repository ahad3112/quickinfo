'''
    Author:
        * Muhammed Abdullah Al Ahad <ahad3112@yahoo.com, maaahad@gmail.com, maaahad@kth.se>


    Description:
    Based on clusters:
        * List of login nodes
        * list of transfer nodes
        * List of nodes with gpu along with gpu info

    Source:
        * https://www.pdc.kth.se/support/documents/data_management/data_management.html#nodes-for-file-operations
'''

def handler(args):
    print(f'This method deals with Clusters module: {args}')

def add_clusters_cli(subparsers):
    cluster_parser = subparsers.add_parser(
        'cluster',
        help=r'information on "PDC" clusters.',
        description=r'This module provides some useful information on "PDC" clusters ("Beskow" or "Tegner")'
    )
    cluster_parser.set_defaults(handler=handler)

    cluster_parser.add_argument('name', choices=['tegner', 'beskow'],help="name of the cluster")

