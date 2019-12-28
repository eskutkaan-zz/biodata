#!/usr/bin/env python3

import os

DIR = 'fastafiles/'

def merge_fasta():
    oh = open('mergedfasta/multiple.fasta', 'w')
    for f in os.listdir(DIR):
        fh = open(os.path.join(DIR, f))
        for line in fh:
            oh.write(line)
        fh.close()
    oh.close()    
