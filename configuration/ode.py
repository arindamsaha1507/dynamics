import numpy as np

def ode(x, t, p, type):

    if type == 'fhn':
        return fhn(x, p)

def fhn(x, p):
    
    assert len(x) == 2

    return np.array([
        x[0] - (x[0]**3)/3.0 - x[1] + 0.5,
        (x[0] + p['a'] - p['b']*x[1])/p['c']
    ])