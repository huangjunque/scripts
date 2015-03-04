#!/usr/bin/env python
# coding=utf-8
import os, sys
nnnas = len(sys.argv)
if not 3 <=nnnas <=5:
     print 'usage: %s search_text replace_text [infile [outfile]]" %  os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    if nnnas > 3:
        input_file = open(sys.argv[3])
    if nnnas > 4:
        output_file = open(sys.argv[4], 'w')
    for s in input_file:
        output_file.write(s.replace(stext, rtext))
    output.close()
    input.close()
