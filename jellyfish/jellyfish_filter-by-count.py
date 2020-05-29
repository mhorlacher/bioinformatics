#!/usr/bin/python3

from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('jellyfish_dump_fa')
parser.add_argument('-t', '--threshold', help = "retain all kmers with counts >= threshold")
args = parser.parse_args()

with open(args.jellyfish_dump_fa) as f:
    for line in f:
        if int(line.strip()[1:]) >= int(args.threshold):
            print(line.strip())
            print(f.readline().strip())
        else:
            f.readline()
