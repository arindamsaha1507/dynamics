Advanced Usage with Command-line Options
========================================

Apart from the configuration files listed in :ref:`overview of the configuration files`, the behaviour of the Dynamics program can be changed using command line options. We list all possible options with examples here.

Random initial conditions and parameter values
----------------------------------------------

If we want the simulations to start with a random initial value of ``x``, we can issue the following command from the ``dynamics`` directory::

    python3 run.py --random_ic x

Random values for initial conditions of multiple variables can be given by separating them with a semicolon. For instance, if in the previous example, we want to have random initial conditions for ``x`` and ``y``, we can run::

    python3 run.py --random_ic x;y

Similar to the initial conditions, if we want to run a simulation with random values of parameters ``a`` abd ``b``, we can do so using::

    python3 run.py --random_params a;b

Computing local eigenvalues
---------------------------

Dynamics can also compute local eigenvalues for all simulated trajectories. This helps us identify the stable and unstable portions of periodic quasi-periodic and chaotic attractors in addition to the fixed point attractors. To do this, we use the ``--eigen`` option::
    
    python3 run.py --eigen

This creates a new file (named ``eigenvalues.csv`` by default) which stores the local eigenvalues of the trajectory at each time step.

Changing the output filenames
-----------------------------

The output files for the timeseries and the eigenvalues are named ``timeseries.csv`` and ``eigenvalues.csv`` by default. These filenames can be changed using the ``--outfile`` and the ``--evfile`` options as shown below::

    python3 run.py --outfile out.csv
    python3 run.py --evfile ev.csv

Combining the options
---------------------

All the options described above can be combined in any order and combination. For example::

    python3 run.py --eigen --random_ic x;y

randomises the initial values for ``x`` and ``y`` and also computes the eigenvalues.