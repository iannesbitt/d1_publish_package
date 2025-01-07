import argparse

from d1_publish_package.publish import set_package_public

def test():
    """
    Test function for the package.
    """
    parser = argparse.ArgumentParser(description='Test the package.')
    parser.add_argument('test_arg', type=str, help='A test argument.')
    args = parser.parse_args()
    print(f'Test argument: {args.test_arg}')
    print('Test function complete.')
