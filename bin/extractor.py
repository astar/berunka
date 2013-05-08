#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Extract usefull information from fit files
"""

import os
import sys
import csv
import pytz
import glob
import time
import logging
import tempfile
import argparse
import pyfits as pf
import subprocess
import pandas as pd
import datetime as dt
import dateutil.parser as p
from itertools import islice
import matplotlib.dates as mdates
from IPython import embed


def read_fits(f, line, width, names):
    try:
        logging.debug("Reading file: %s" % f)
        with pf.open(f) as hdu:
            x = hdu[1].data.field('WAVE')
            y = hdu[1].data.field('FLUX')

            hdr = hdu[0].header
            name = hdr['OBJECT']
            if width:
                line = int(line)
                width = int(width)
                y = y[(x > line - width) & (x < line + width)]

            y = list(y)

            if names:    
                y = [name] + y
        logging.debug("Reading file done")
        return y
    except Exception, e:
        raise e
        sys.stderr.write("%s: cannot open file '%s'\n" % (sys.argv[0], f))
        pass

def file_list(thedir):
    return glob.glob(os.path.join(thedir, '*.fits'))
            


def save2csv(data):
    try:
        writer = csv.writer(sys.stdout)
        writer.writerow(data)
        logging.debug("Done writing to file")
    except:
        sys.stderr.write("%s: cannot write to file '%s'\n" % (sys.argv[0], file_name))
        sys.exit(1)
        


def main():

    prg = os.path.basename( sys.argv[0] )
    parser = argparse.ArgumentParser()
    parser.add_argument( '-s', '--source', action='store',
                      default=None, required=True, help='specify input dir')

    parser.add_argument( '-c', '--category', action='store',
                      default=None, required=True, help='specify category')

    parser.add_argument( '-o', '--output', action='store',
                      default=None, help='specify output file')

    parser.add_argument('-D', '--debug', action='store_true',
                      default=False, help='enter in debugging mode')
    parser.add_argument( '-n', '--nrows', action='store',
                      default=None, help='limit number of processed files')

    parser.add_argument( '-l', '--line', action='store',
                      default=6563, help='Specify spectral line position  for range limit')

    parser.add_argument( '-w', '--width', action='store',
                      default=None, help='Specify spectral line range limit')

    parser.add_argument( '-N', '--names', action='store_true',
                      default=False, help='Include names of the star into result')
        
    
    args = parser.parse_args()

    #
    # debug
    #
    if args.debug:
        d_level = logging.DEBUG
    else:
        d_level = None
    logging.basicConfig(level=d_level,
                        format='%(asctime)s %(process)d %(levelname)s %(funcName)s(): %(message)s',
                        filemode='a')
    #
    # output
    #
    if args.output:
        logging.debug("Writing to file: %s" % args.output)
        sys.stdout = open(args.output, 'w')

    if args.nrows:
        args.nrows = int(args.nrows)


    files = file_list(args.source)[:args.nrows]

    for f in files:
        data = [args.category] + read_fits(f, args.line, args.width, args.names) 
        save2csv(data)

    

        
if __name__ == '__main__':
    main()

    
# vim: set cin et ts=4 sw=4 ft=python :
