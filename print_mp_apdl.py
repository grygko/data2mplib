# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# APDL example

# <rawcell>

# /prep7
# MPTEMP,1,0,500               ! Define temperature-dependent EX,
# MPDATA,EX,1,,14.665E6,12.423e6           
# MPDATA,PRXY,1,,0.3
#                                 ! MPDATA, Lab, MAT, STLOC, C1, C2, C3, C4, C5, C6
#                                 ! MPTEMP, STLOC, T1, T2, T3, T4, T5, T6
#                                 ! TB, Lab, MAT, NTEMP, NPTS, TBOPT, EOSOPT, FuncName
# 
# TB,PLASTIC,1,2,5,KINH        ! Activate TB,PLASTIC data table
# TBTEMP,0.0                   ! Temperature = 0.0
# TBPT,,0,29.33E3          ! Plastic strain, stress at temperature = 0
# TBPT,,1.59E-3,50E3
# TBPT,,3.25E-3,55E3
# TBPT,,5.91E-3,60E3
# TBPT,,1.06E-2,65E3
# TBTEMP,500                   ! Temperature = 500
# TBPT,,0,27.33E3          ! Plastic strain, stress at temperature = 500
# TBPT,,2.02E-3,37E3
# TBPT,,3.76E-3,40.3E3
# TBPT,,6.48E-3,43.7E3
# TBPT,,1.12E-2,47E3

# <codecell>

import sys
import numpy as np

# <codecell>

def print_mptemp(temp_list, command='MPTEMP', max_entries=6, max_ntemp=100,
                 fmt='{:.2f}'):
    """Print temperatures in accordance to MPTEMP command to stdout
    
    Args:
        temp_list (list): 1D list with temperature values
        command (string): APDL command
        max_entries (int): max number of the property entries on on line
        max_ntemp (int): max number of temperatures
        fmt (str): string formatter. How to pass it XXX
    """
    
    temp_list = temp_list[:max_ntemp] # cut off exceeding temperatures
    
    for val, ix in zip(temp_list, range(len(temp_list))):
        if ix % max_entries == 0:
            sys.stdout.write('\n{0},{1}, {2:.2f}'.format(command, ix+1, val))
        else:
             sys.stdout.write(', {0:.2f}'.format(val))
                
                        
def print_mpdata(data_list, lab, command='MPDATA', max_entries=6, 
                 max_ndata=100, fmt='{:.3E}'):
    """Print linear temperature-dependant material property to stdout
    
    Args:
        data_list (list): 1D data list
        lab (string): valid ANSYS APDL property label
        command (string): APDL command
        max_entries (int): max number of the property entries on on line
        fmt (str): string formatter. How to pass it XXX

    The function prints in ANSYS APDL format convenient for e.g., saving to files
    """
    
    data_list = data_list[:max_ndata] # cut off exceeding data elements
    
    for val, ix in zip(data_list, range(len(data_list))):
        if ix % max_entries == 0:
            sys.stdout.write('\n{0},{1},{2}, {3:.3E}'.
                             format(command, lab, ix+1, val))
        else:
             sys.stdout.write(', {0:.3E}'.format(val))
                
def print_tb(lab, mat, tbopt, temp_list, tbpt_list, max_npts=100,
             max_ntemp=20, temp_fmt='{:.2f}', data_fmt='{:.3E}'):
    """
    Args:
        lab (string): material model label e.g. PLASTIC
        tbopt (string): material model option
        temp_list (list): list of temperatures. Must correspond to first
            dimension of tbpt_list
        tbpt_list (list): ntemp x N x 2 list containing data points. 
            Will be cut-off for ntemp > max_npts
        max_ntemp (int): max number of temperature points
        max_npts (int): max number of data points

    For description of arguments and structure of the printout see description
    of TB and TBPT commands in ANSYS APDL documentaion
    
    Example:
        TB, Lab, MAT, NTEMP, NPTS, TBOPT
        
        TB,PLASTIC,1,2,3,KINH
        TBTEMP,0.0               ! Temperature = 0.0
        TBPT,,0,29.33E3          ! Plastic strain, stress at temperature = 0
    """
    temp_list = np.asarray(temp_list, dtype=float)
    tbpt_list = np.asarray(tbpt_list, dtype=float)
    temp_list = temp_list[:max_ntemp] # cut-off exceeding elements
    tbpt_list = tbpt_list[:max_ntemp, :, :max_npts]
    ntemp = len(temp_list)
    npts = len(tbpt_list)
    
    sys.stdout.write('\nTB,{0},{1},{2},{3},{4}'.
                     format(lab, mat, ntemp, npts, tbopt))

    for temp, tix in zip(temp_list, range(len(temp_list))):
        sys.stdout.write('\nTBTEMP,{0:.2f}'.format(temp))
        
        for x1, x2 in zip(tbpt_list[tix][0], tbpt_list[tix][1]):
            sys.stdout.write('\nTBPT,, {0:10.3E}, {1:12.5E}'.format(x1, x2))

# <codecell>

temp = np.linspace(300, 400, 10)
ex = temp*1e3
tb_pt = np.arange(60).reshape(10,2,3)

print_mptemp(temp)
print_mpdata(ex, 'EX')
print_tb('PLASTIC', 1, 'KINH', temp, tb_pt)

# <codecell>

fmt='{:10.3E}'
print('a = {0:.2f} b = '+fmt.format(100000, 200000))

# <codecell>

a = np.arange(36).reshape(3,2,6)
print a, '\n'*2, a[:1,:,:4], '\n'*2, a[0][:,:4]

# <codecell>

l = list(a)
l = a.tolist()
l

# <codecell>

for l in a:
    for m,n in zip(l[0],l[1]):
        print m,n,'\n'

