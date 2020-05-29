#!/usr/bin/python3

from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('dir')
parser.add_argument('-c', '--command')
parser.add_argument('-p', '--pattern')
parser.add_argument('-o', '--output', default = None)
parser.add_argument('--output-type-o', action='store_true', default = False)
args = parser.parse_args()


for f in list(Path(args.dir).glob('**/' + args.pattern)):
    cmd = args.command + ' ' + str(f)

    if args.output is not None:
        f_out = '.'.join(str(f).split('.')[:-1] + [args.output])
        if args.output_type_o:
            cmd = args.command + ' -o ' + f_out + ' ' + str(f)
        else:
            cmd = args.command + ' ' + str(f) + ' > ' + f_out

    print(cmd)
    subprocess.run([cmd], shell = True)

