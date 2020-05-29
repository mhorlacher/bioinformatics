#!/usr/bin/python3

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('fasta')
parser.add_argument('-d', '--directory', default = '.')
args = parser.parse_args()

def make_fname(header):
    identifier = header[1:].split(' ')[0]
    fname_split = args.fasta.split('.')
    new_fname = '.'.join(fname_split[:-1] + [identifier] + [fname_split[-1]])
    return new_fname

with open(args.fasta) as f:
    new_f = None
    for line in f:
        if line[0] == '>':
            new_fname = make_fname(line.strip())
            new_f_path = Path(args.directory)
            if not new_f_path.exists():
                raise NotADirectoryError('Directory "%s" does not exist')
            else:
                if new_f is not None:
                    new_f.close()
                new_f = open(str(new_f_path.joinpath(new_fname)), 'w')
                print(line.strip(), file = new_f)
        else:
            print(line.strip(), file = new_f)
