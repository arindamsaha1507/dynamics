Defining New Sets of ODE's
==========================

The main aim of Dynamics is to make simulating and analysing new dynamical systems with ease. Therefore, here we describe in detail how to define new sets of dynamical systems in Dynamics. In order to do so, we have to alter only the files in the ``configuration`` directory. Specifically, we need to modify the ``inputs.yml`` and ``ode.py`` files. The specific modifications are as follows.

Changes to the inputs.yml file
------------------------------

This is a YAML file with a bunch of key/value pairs.

#. Set the ``family`` key to ``ode``
#. Give a unique name to your dynamical system under the key ``ode_system``.
#. Under the ``parameters`` key, declare the names of the parameters used. For each parameter, define the ``max``, ``min`` and ``default`` keys.
#. Under the ``initial_conditions`` key, declare the names of the dynamical variables used. For each variable, define the ``max``, ``min`` and ``default`` keys.
#. Under the ``time`` key, define the initial time as ``ti``, final time as ``tf``, time-step as ``dt`` and the fraction of total time to be considered transience as ``tr``.

.. warning:: 
    Do not change the indentation of the ``inputs.yml`` file.

Changes to the ode.py file
--------------------------

In this file, a number of functions are defined. You would add one two new functions and modify two existing functions. 

Notice that 
#. In the initial portion of the file, two functions namely ``ode()`` and ``jacobian()`` are defined. 
#. Thereafter, there is a comment namely ``# ODE Systems``. Under this comment, there are functions for the predefined systems of ODE's. 
#. Below that is a comment ``# Jacobians`` under which, the Jacobians of the ODE's are defined.

We will modify these three sections of the file one-by-one.

#. In the initial section, note that, both ``ode()`` and ``jacobian()`` functions have an ``if...elif...else`` block. It is in this block that Dynamics chooses the ODE system based on the ``type`` argument. In these ``if...elif...else`` blocks, add an elif segment which selects the new system of ODE's and Jacobians which we shall define in the next step. Note that the ``type`` argument is taken from the ``ode_system`` key of the ``inputs.yml`` file.
#. In the ``# ODE Systems`` section, define a new function that describes your system.
#. In the ``# Jacobians`` section, define a new function that Jacobian of your system.

Please take help of the functions already defined in order to define functions in steps 2 and 3.


That is all! Now you can run your simulations by issuing the following command in the terminal::
    
    python3 run.py

For the available options to run Dynamics, see :ref:`advanced usage with command-line options`.