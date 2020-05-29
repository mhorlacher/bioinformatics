#!/usr/bin/python3

from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('target')
parser.add_argument('-p', '--pattern')
args = parser.parse_args()


for f in list(Path(args.source).glob('**/' + args.pattern)):
    f_relative_to_source = f.relative_to(Path(args.source))
    f_relative_to_target = Path(args.target, f_relative_to_source)
    (f_relative_to_target.parent).mkdir(parents = True, exist_ok = True)

    print('Copying', f_relative_to_target.parent)
    shutil.copy(str(f), str(f_relative_to_target.parent))

