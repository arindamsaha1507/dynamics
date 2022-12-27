Usage
=====

Although Dynamics is written to be run using the FabSim plugin FabDynamics, it can also be run as a standalone program to simulate dynamical systems. Currently we can use it to simulate any system of ODE's using RK4 numerical solver. For a basic run, from the dynamics directory, simply execute::

    python3 run.py

This would create a file called ``timeseries.csv`` with the timeseries excluding the transience. To plot the timeseries, use::

    python3 plotter.py

To configure the exact system of ODE to use, please see the Configuration page.

.. note:: 
    We understand that these are fairly basic functionalities and visualisations. We intend to provide more advanced post-processing and visualisations in the FabDynamics module. For the Dynamics module, we intend to focus on simulating more types of systems in future such as maps, DDE's, SDE's, PDE's and networks.