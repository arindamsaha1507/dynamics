import yaml
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import configuration.ode as ode

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

        self.system = ode_system


    def solver(self):
                
        t = self.time['ti']
        x = np.array(self.ic)

        ts = np.zeros(int((self.time['tf']-self.time['ti'])/self.time['dt'])+1)
        xs = np.zeros((int((self.time['tf']-self.time['ti'])/self.time['dt'])+1, len(x)))
        cc = 0

        while t < self.time['tf']:

            k1 = self.time['dt'] * ode.ode(x, t, self.params, self.system)
            k2 = self.time['dt'] * ode.ode(x + k1/2, t + self.time['dt']/2, self.params, self.system)
            k3 = self.time['dt'] * ode.ode(x + k2/2, t + self.time['dt']/2, self.params, self.system)
            k4 = self.time['dt'] * ode.ode(x + k3, t + self.time['dt'], self.params, self.system)
            k = (k1+2*k2+2*k3+k4)/6

            ts[cc] = t
            xs[cc] = x
            cc += 1

            x = x + k
            t = t + self.time['dt']

        df = pd.DataFrame()

        df['time'] = ts
        for cc in range(len(self.vars)):
            df[self.vars[cc]] = xs[:,cc]

        self.timeseries = df

    def save_timeseries(self, outfile):
        if self.timeseries is not None:

            ts = self.timeseries[int(self.time['tr']*len(self.timeseries)):-1]

            ts.to_csv(outfile, index=False)
