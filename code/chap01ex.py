"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def main(script):
    df = ReadFemResp()
    print(df.shape)
    t = df.pregnum.value_counts().sort_index()
    print(t)
    print("7-95:", t[7:96].sum())
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    # set caseid as index
    df.set_index("caseid", inplace=True)
    for caseid, indics in preg_map.items():
        n = len(indics)
        pregnum = df.pregnum[caseid]
        assert pregnum == n


    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
