#!/usr/bin/env python3

from dynamics.system import System

import argparse

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--random_params', action="store", default="None", help="Randomizes parameters")
    parser.add_argument('--random_ic', action="store", default="None", help="Randomizes initial conditions")

    parser.add_argument('-o', '--outfile', action="store", default="timeseries.csv", help="The output file where timeseries is stored")
    parser.add_argument('-e', '--evfile', action="store", default="eigenvalues.csv", help="The output file where eigenvalues is stored")

    args = parser.parse_args()

    S = System(args)
    S.solver()
    S.save_timeseries(args.outfile)
    S.save_eigenvalues(args.evfile)
