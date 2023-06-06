
#! /usr/bin/env python3

import sys, re
from argparse import ArgumentParser
from collections import Counter

# argument parser
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# input sequence
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# change sequence to upper case to support case such as atcg
args.seq = args.seq.upper()

# ACGT so DNA
if re.search('^[ACGT]+$', args.seq):
    print ('The sequence is DNA')
# ACGU so RNA
elif re.search('^[ACGU]+$', args.seq):
    print ('The sequence is RNA')
# no T or U so RNA or DNA
elif re.search('^[ACG]+$', args.seq):
    print ('The sequence can be DNA or RNA')
# all other cases
else:
    print ('The sequence is not DNA nor RNA')
    raise ValueError('unsupported value')

sequence = args.seq
seq_len = len(sequence)
counter = Counter(sequence)

seq_freq = [ (char, round(char_count / seq_len, 2)) for char, char_count in counter.most_common()]
print(seq_freq)

