#!/usr/bin/env python
# coding: utf-8

# In[62]:


from pathlib import Path
import argparse


# In[ ]:


import numpy as np


# In[ ]:


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int)
parser.add_argument('-s', '--seed', default=None, type=int)
parser.add_argument('-o', '--outdir', default='.')
parser.add_argument('in_fa', metavar='<in.fasta>')
args = parser.parse_args()


# In[ ]:


if args.seed is not None:
    np.random.seed(args.seed)


# In[55]:


def shuffle_seq(seq):
    seq_arr = np.array(list(seq))
    np.random.shuffle(seq_arr)
    return ''.join(list(seq_arr))


# In[69]:


def write_shuffle(seq, seq_id, n, out):
    basepath = Path(out).joinpath(f'{seq_id}.permuted')
    basepath.mkdir(exist_ok=True)
    for i in range(0, n):
        with open(str(basepath.joinpath(f'{seq_id}.permuted.{i}.fa')), 'w') as f:
            f.write(f'>{seq_id}\n')
            f.write(shuffle_seq(seq))


# In[70]:


with open(args.in_fa) as f:
    current_filepath = None
    current_id = None
    current_sequence = ''
    for line in f:
        if line[0] == '>':
            if current_id is not None:
                write_shuffle(current_sequence, current_id, args.number, args.outdir)
                
            current_sequence = ''
            current_id = line[1:].strip().split(' ')[0]
        else:
            current_sequence += line.strip()
    
    write_shuffle(current_sequence, current_id, args.number, args.outdir)

