import yaml
import numpy as np
import pandas as pd
import configuration.ode as ode
from numpy import linalg as LA
from scipy.integrate import solve_ivp

class System:

    def __init__(self, arguments):

        with open('configuration/inputs.yml', 'r') as f:
            inputs = yaml.safe_load(f)

        self.family = inputs['family']

        if self.family == 'ode':

            self.params = dict(inputs['parameters'])
            self.ic = dict(inputs['initial_conditions'])
            self.time = inputs['time']

            for key in self.params:
                self.params[key] = self.params[key]['default']

            for key in self.ic:
                self.ic[key] = self.ic[key]['default']

            if arguments.random_ic != 'None':
                vars = arguments.random_ic.split(';')
                for v in vars:
                    self.ic[v] = np.random.random()*(inputs['initial_conditions'][v]['max'] - inputs['initial_conditions'][v]['min']) + inputs['initial_conditions'][v]['min']

            if arguments.random_params != 'None':
                vars = arguments.random_params.split(';')
                for v in vars:
                    self.params[v] = np.random.random()*(inputs['parameters'][v]['max'] - inputs['parameters'][v]['min']) + inputs['parameters'][v]['min']


            self.vars = list(self.ic.keys())
            self.ic = [self.ic[k] for k in self.vars]
            self.timeseries = None

            self.system = inputs['ode_system']


    def solver(self):

        if self.family == 'ode':

            sol = solve_ivp(
                ode.ode, 
                [self.time['ti'], self.time['tf']], 
                self.ic, 
                args=(self.params, self.system), 
                dense_output=True
                )

            ts = np.arange(self.time['ti'], self.time['tf'], self.time['dt'])
            xs = sol.sol(ts)
 
            df = pd.DataFrame()

            df['time'] = ts
            for cc in range(len(self.vars)):
                df[self.vars[cc]] = xs[cc, :]

            self.timeseries = df

    def eigenvalues(self):

        df = pd.DataFrame()

        df['time'] = list(self.timeseries['time'])
        es_real = np.zeros((len(self.timeseries['time']), len(self.vars)))
        es_imag = np.zeros((len(self.timeseries['time']), len(self.vars)))
        
        for ii in range(len(self.timeseries)):

            x = [self.timeseries[v][ii] for v in self.vars]
            e = LA.eig(ode.jacobian(df['time'][ii], x, self.params, self.system))

            es_real[ii] = e[0].real
            es_imag[ii] = e[0].imag

        for cc in range(len(self.vars)):
            df['real_{}'.format(cc)] = es_real[:,cc]
            df['imag_{}'.format(cc)] = es_imag[:,cc]

        self.eigenvalues = df

    def save_timeseries(self, outfile):

        if self.timeseries is not None:

            ts = self.timeseries[int(self.time['tr']*len(self.timeseries)):-1]

            ts.to_csv(outfile, index=False)

    def save_eigenvalues(self, outfile):

        if self.eigenvalues is not None:

            ts = self.eigenvalues[int(self.time['tr']*len(self.timeseries)):-1]

            ts.to_csv(outfile, index=False)
