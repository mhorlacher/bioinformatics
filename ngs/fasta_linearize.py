#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fasta')
args = parser.parse_args()

with open(args.fasta) as f:
    linear_line = ''
    for line in f:
        if line[0] == '>':
            print(linear_line, end = '')
            print('\n' + line.strip())
            linear_line = ''
        else:
            linear_line += line.strip()
    print(linear_line)
