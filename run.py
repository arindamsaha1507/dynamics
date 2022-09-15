import sys
import yaml
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import configuration.ode as ode

class System:

    def __init__(self):

        with open('configuration/inputs.yml', 'r') as f:
            inputs = yaml.safe_load(f)

        self.params = inputs['parameters']
        self.ic = inputs['initial_conditions']
        self.time = inputs['time']

        self.vars = list(self.ic.keys())
        self.ic = [self.ic[k] for k in self.vars]
        self.timeseries = None


    def solver(self):
                
        t = self.time['ti']
        x = np.array(self.ic)

        ts = np.zeros(int((self.time['tf']-self.time['ti'])/self.time['dt'])+1)
        xs = np.zeros((int((self.time['tf']-self.time['ti'])/self.time['dt'])+1, len(x)))
        cc = 0

        while t < self.time['tf']:

            k1 = self.time['dt'] * ode.ode(x, t, self.params)
            k2 = self.time['dt'] * ode.ode(x + k1/2, t + self.time['dt']/2, self.params)
            k3 = self.time['dt'] * ode.ode(x + k2/2, t + self.time['dt']/2, self.params)
            k4 = self.time['dt'] * ode.ode(x + k3, t + self.time['dt'], self.params)
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

    def save_timeseries(self):
        if self.timeseries is not None:
            self.timeseries.to_csv('output/timeseries.csv', index=False)

if __name__=='__main__':
    S = System()
    S.solver()
    S.save_timeseries()