import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", default=None)
parser.add_argument("--val", default=None)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def create_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        new_dict.update({key: [value]})
    return new_dict


def write_dict(exist_dict):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(exist_dict))


def read_dict():
    with open(storage_path, 'r') as f:
        print(f.read())


if args.key:
    if args.val:
        write_dict(create_dict(key=args.key, value=args.val))
        read_dict()
    else:
        print("{}".format(args.key))


