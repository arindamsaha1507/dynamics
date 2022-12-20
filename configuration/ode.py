import numpy as np

def ode(x, t, p, type):

    if type == 'fhn':
        return fhn(x, p)
    elif type == 'resource':
        return resource(x, p)

def fhn(x, p):
    
    assert len(x) == 2

    return np.array([
        x[0] - (x[0]**3)/3.0 - x[1] + 0.5,
        (x[0] + p['a'] - p['b']*x[1])/p['c']
    ])

def resource(x, p):

    assert len(x) == 1

    return np.array([
        p['r']*x[0]*(1.0-x[0]) - p['p']*x[0]
    ])