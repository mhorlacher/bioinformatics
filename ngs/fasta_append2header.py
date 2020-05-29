#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fasta')
parser.add_argument('-s', '--string', help = 'string to append to FASTA header')
args = parser.parse_args()

with open(args.fasta) as f:
    for line in f:
        if line[0] == '>':
            new_header = line.strip() + ' ' + args.string
            print(new_header)
        else:
            print(line.strip())
