import argparse
import os

from d1_publish_package.publish import set_package_public
from d1_publish_package.utils import get_config

def cli():
    """
    The command line interface for the package.
    """
    parser = argparse.ArgumentParser(description='Publish a DataONE package.')
    parser.add_argument('package_id', type=str, help='The package persistent identifier (PID).')
    args = parser.parse_args()
    set_package_public(args.package_id)
