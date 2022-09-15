import numpy as np

def ode(x, t, p):

    assert len(x) == 2

    # return np.array([
    #     x[1],
    #     -x[0]
    # ])

    return np.array([
        x[0] - (x[0]**3)/3.0 - x[1] + 0.5,
        (x[0] + p['a'] - p['b']*x[1])/p['c']
    ])