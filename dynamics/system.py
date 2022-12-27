import yaml
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import configuration.ode as ode
from numpy import linalg as LA

class System:

    def __init__(self, ode_system):

        with open('configuration/inputs.yml', 'r') as f:
            inputs = yaml.safe_load(f)

        self.params = inputs['parameters']
        self.ic = inputs['initial_conditions']
        self.time = inputs['time']

        self.vars = list(self.ic.keys())
        self.ic = [self.ic[k] for k in self.vars]
        self.timeseries = None

        if ode_system == 'None':
            self.system = inputs['ode_system']
        else:
            self.system = ode_system


    def solver(self):
                
        t = self.time['ti']
        x = np.array(self.ic)

        ts = np.zeros(int((self.time['tf']-self.time['ti'])/self.time['dt'])+1)
        xs = np.zeros((int((self.time['tf']-self.time['ti'])/self.time['dt'])+1, len(x)))
        es_real = np.zeros((int((self.time['tf']-self.time['ti'])/self.time['dt'])+1, len(x)))
        es_imag = np.zeros((int((self.time['tf']-self.time['ti'])/self.time['dt'])+1, len(x)))
        cc = 0

        while t < self.time['tf']:

            k1 = self.time['dt'] * ode.ode(x, t, self.params, self.system)
            k2 = self.time['dt'] * ode.ode(x + k1/2, t + self.time['dt']/2, self.params, self.system)
            k3 = self.time['dt'] * ode.ode(x + k2/2, t + self.time['dt']/2, self.params, self.system)
            k4 = self.time['dt'] * ode.ode(x + k3, t + self.time['dt'], self.params, self.system)
            k = (k1+2*k2+2*k3+k4)/6

            ts[cc] = t
            xs[cc] = x

            e = LA.eig(ode.jacobian(x, t, self.params, self.system))

            es_real[cc] = e[0].real
            es_imag[cc] = e[0].imag

            cc += 1

            x = x + k
            t = t + self.time['dt']

        df = pd.DataFrame()
        de = pd.DataFrame()

        df['time'] = ts
        de['time'] = ts
        for cc in range(len(self.vars)):
            df[self.vars[cc]] = xs[:,cc]
            de['real_{}'.format(cc)] = es_real[:,cc]
            de['imag_{}'.format(cc)] = es_imag[:,cc]

        self.timeseries = df
        self.eigenvalues = de

    def save_timeseries(self, outfile):
        if self.timeseries is not None:

            ts = self.timeseries[int(self.time['tr']*len(self.timeseries)):-1]

            ts.to_csv(outfile, index=False)

    def save_eigenvalues(self, outfile):
        if self.eigenvalues is not None:

            ts = self.eigenvalues[int(self.time['tr']*len(self.timeseries)):-1]

            ts.to_csv(outfile, index=False)