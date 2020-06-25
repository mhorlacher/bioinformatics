#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3


# In[ ]:


import argparse
from pathlib import Path
import subprocess


# In[ ]:


parser = argparse.ArgumentParser()
parser.add_argument('--dry', action='store_true', default=False, help='Print command but do not execute.')
parser.add_argument('bam', metavar='<in.bam>')
args = parser.parse_args()


# In[ ]:


out_R1 = args.bam.strip('.bam') + '.R1.fastq'
out_R2 = args.bam.strip('.bam') + '.R2.fastq'


# In[ ]:


cmd = f'samtools fastq -1 {out_R1} -2 {out_R2} {args.bam}'


# In[ ]:


print(cmd)
subprocess.run([cmd], shell=True)

