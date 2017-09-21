#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:51:22 2017

@author: irribarrac
"""

#with open("bls_interesting_3_sigma.dat", 'r' ) as infile:
 #   with open("EPICIDS.txt", "w") as outfile:
 #       a = infile.readline()
#       for line in infile:
#            line = line.split()
 #           bigname = '{0}\n'.format(line[0])
  #          bigname2 = bigname.replace("ktwo", "")
#            newline = bigname2.replace("-c04_llc.fits", "")
#            print "wrinting into file this:", newline
#            outfile.write(newline)
#infile.close()
#outfile.close()
from scipy.signal import medfilt
from scipy.ndimage.filters import gaussian_filter
import numpy as np
import argparse
import pyfits
import urllib
import os

# Read user input:
parser = argparse.ArgumentParser()
parser.add_argument('-epicid',default=None)
parser.add_argument('-campaign',default=None)

args = parser.parse_args()
idfile = open(args.epicid,'r')
campaign = args.campaign
for EPICID in idfile:
    EPICID = EPICID.replace("\n", "")
    print EPICID, campaign
    