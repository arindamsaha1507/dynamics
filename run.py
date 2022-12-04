from dynamics.system import System

import argparse

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--ode_system', action="store", default="fhn", help="The ODE system to solve")
    args = parser.parse_args()

    S = System(args.ode_system)
    S.solver()
    S.save_timeseries()
