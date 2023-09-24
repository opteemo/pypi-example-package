import argparse
from example_package_opteemo import hello

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="your name")


def run():
    args = parser.parse_args()
    hello.hello(args.name)
