#!/usr/bin/env python

"""Convenience functions for saving data into ANSYS material properties file"""

import sys
import time
import numpy as np

preamble = "! This file was saved by "+sys.argv[0]+" on "+time.ctime()
preamble += "\n! Author: Grygoriy Kravchenko"

def constr_KINH(mat_hand, reft_hand, temp_arr, ex_arr, alpx_arr, nuxy_arr,
                eps_pl_arr, sig_arr):
    """Construct string for output as a kinematic hardening in ANSYS
    refer TB,KINH documentation

    Args:
        mat_hand (string): material number handler
        reft_hand (string): reference temperature handler
    """

    sys.stdout.write('\n{0}=arg1'.format(mat_hand))
    sys.stdout.write('\n{0}=arg2'.format(reft_hand))

    sys.stdout.write('\nmptemp,')
    for temp, ex, alpx, nuxy in zip(temp_arr, ex_arr, alpx_arr, nuxy_arr):


        #sys.stdout.write('\nmpdata,{0},{1:8.1e}'.format(mat_hand, ex)

if __name__ == "__main__":
    sys.stdout.write(preamble)
    sys.stdout.write('\nexiting...\n')
    # generate random properties
    count = 3 # number of temperature points
    temp_arr = np.random.random((count,))*300 + 300
    ex_arr = np.random.random((count,))*10 + 140
    alpx_arr = np.random.random((count,))*10e-6 + 17e-6
    nuxy_arr = np.random.random((count,))*0.1 + 0.34

