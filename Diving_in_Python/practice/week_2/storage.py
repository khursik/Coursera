import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    

def put(key, value):
    data = get()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get():
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def read_data(key):
    data = get()
    if key in data:
        return data.get(key)
    else:
        return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='KEY')
    parser.add_argument('--val', help='VALUE')
    parser.add_argument('--clear', action='store_true', help='CLEAR')
    args = parser.parse_args()
    if args.clear:
        os.remove(storage_path)
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        
        print(', '.join(list(read_data(args.key))))
    else:
        print('The program is called with invalid parameters.')