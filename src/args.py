import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('message', type=str, help='the message to be printed')
    args = parser.parse_args()
    return args

