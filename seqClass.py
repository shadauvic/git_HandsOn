#! /usr/bin/env python3

import sys, re
from argparse import ArgumentParser

# argument parser
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# input sequence
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
# input motif for search
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# change sequence to upper case to support case such as atcg
args.seq = args.seq.upper()

if args.motif:
    # change motif to upper case
    args.motif = args.motif.upper()
    print(f"Motif search enabled: looking for motif '{args.motif}' in sequence '{args.seq}'", end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
else:
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
