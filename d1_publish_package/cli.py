import argparse
import os

from d1_client.mnclient_2_0 import MemberNodeClient_2_0
from d1_publish_package.publish import set_package_public
from .utils import get_config, get_token

def cli():
    """
    The command line interface for the package publisher.
    """
    config = get_config()
    token = get_token()
    mnurl = config['mnurl']
    # Initialize the mn client
    options: dict = {
        "headers": {"Authorization": "Bearer " + token},
        "timeout_sec": 9999,
        }
    client: MemberNodeClient_2_0 = MemberNodeClient_2_0(mnurl, **options)

    parser = argparse.ArgumentParser(description='Publish a DataONE package.')
    parser.add_argument('package_ids', type=str, nargs='+', help='The package persistent identifiers (PIDs).')
    args = parser.parse_args()
    for package_id in args.package_ids:
        print(f'Publishing package: {package_id}')
        set_package_public(package_id, client)
    client._session.close()
