import numpy as np

def ode(t, x, p, type):

    if type == 'fhn':
        return fhn(x, p)
    elif type == 'resource':
        return resource(x, p)

def jacobian(t, x, p, type):

    if type == 'fhn':
        return jac_fhn(x, p)

# ODE Systems

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

# Jacobians

def jac_fhn(x, p):
    
    assert len(x) == 2

    return np.array([
        [
            1 - x[0]**2,
            -1
        ],
        [
            1/p['c'],
            p['b']/p['c']
        ]
    ])

def resource_fhn(x, p):

    assert len(x) == 1

    return np.array([
        [
            p['r'] - 2*p['r']*x[0] - p['p']
        ]
    ])