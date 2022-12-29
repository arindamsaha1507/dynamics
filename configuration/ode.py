import numpy as np
import sys

def ode(t, x, p, type):
    """Selects the system of ODE's to be simulated based on the 'type'
    provided and evaluates it at a given time, for a given point in the phase
    space and for a given set of parameters.

    Args:
        t (float): Time at which the system of ODE is to be evaluated
        x (array of floats): Coordinates of the points in phase space at which 
            the system of ODE is to be evaluated
        p (dict of floats): Dictionary with parameter names and values at which 
            the system of ODE is to be evaluated
        type (string): Name of the system of ODE to be evaluated. There must be
            a function corresponding to this name defined later

    Returns:
        array of floats: Value of the evaluated system of ODE's
    """

    if type == 'fhn':
        return fhn(x, p)
    elif type == 'resource':
        return resource(x, p)
    else:
        sys.exit("Unknown name of system of ODE's")

def jacobian(t, x, p, type):
    """Selects the Jacobian for the 'type' of system of ODE's and evaluates it
    at a given time, for a given point in the phase space and for a given set 
    of parameters.

    Args:
        t (float): Time at which Jacobian is to be evaluated
        x (array of floats): Coordinates of the points in phase space at which 
            Jacobian is to be evaluated
        p (dict of floats): Dictionary with parameter names and values at which 
            Jacobian is to be evaluated
        type (string): Name of the system for which Jacobian to be evaluated. 
            There must be a function corresponding to this name defined later

    Returns:
        array of floats: Value of the evaluated Jacobian
    """

    if type == 'fhn':
        return jac_fhn(x, p)
    elif type == 'resource':
        return jac_resource(x, p)
    else:
        sys.exit("Unknown name of system of ODE's")

# ODE Systems

def fhn(x, p):
    """ODE's defining the FitzHugh-Nagumo system

    Args:
        x (array of floats): length 2 describing variables 'x' and 'y'
        p (dict of floats): contains keys describing parameters 'a', 'b', 'c'

    Returns:
        array of floats: Value of the function
    """
    
    assert len(x) == 2

    return np.array([
        x[0] - (x[0]**3)/3.0 - x[1] + 0.5,
        (x[0] + p['a'] - p['b']*x[1])/p['c']
    ])

def resource(x, p):
    """ODE's defining a simple resource dynamics

    Args:
        x (array of floats): length 1 describing variables 'x'
        p (dict of floats): contains keys describing parameters 'r' and 'p'

    Returns:
        array of floats: Value of the function
    """

    assert len(x) == 1

    return np.array([
        p['r']*x[0]*(1.0-x[0]) - p['p']*x[0]
    ])

# Jacobians

def jac_fhn(x, p):
    """Jacobian of the FitzHugh-Nagumo system

    Args:
        x (array of floats): length 2 describing variables 'x' and 'y'
        p (dict of floats): contains keys describing parameters 'a', 'b', 'c'

    Returns:
        array of floats: Value of the Jacobian
    """
    
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

def jac_resource(x, p):
    """Jacobian of the resource dynamics model

    Args:
        x (array of floats): length 1 describing variables 'x'
        p (dict of floats): contains keys describing parameters 'r' and 'p'

    Returns:
        array of floats: Value of the Jacobian
    """

    assert len(x) == 1

    return np.array([
        [
            p['r'] - 2*p['r']*x[0] - p['p']
        ]
    ])