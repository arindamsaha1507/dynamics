#!/usr/bin/env python3

from dynamics.system import System

import argparse

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--ode_system', action="store", default="None", help="The ODE system to solve")
    parser.add_argument('-o', '--outfile', action="store", default="timeseries.csv", help="The ODE system to solve")
    args = parser.parse_args()

    S = System(args.ode_system)
    S.solver()
    S.save_timeseries(args.outfile)
