Configuration
=============

Configuration refers to the settings that determine the specifics of the simulation. For dynamics, these settings are given via

* The ``inputs.yml`` file in the ``configuration`` directory.
* The ``ode.py`` file in the ``configuration`` directory.
* The command-line arguments given when running ``run.py``.

The inputs.yml file
+++++++++++++++++++++++

An example of the configuration file ``inputs.yml`` is as follows:

.. code-block:: yaml

    family: 'ode'

    ode_system: 'fhn'

    parameters:
        a: 
            min: -1.0
            max: 1.0
            default: 0.7
        b: 
            min: 0.0
            max: 1.0
            default: 0.8
        c:
            min: 0.0
            max: 20.0
            default: 12.5

    initial_conditions:
        x: 
            min: -5.0
            max: 5.0
            default: 0.1
        y:
            min: -5.0
            max: 5.0
            default: 0.1

    time:
        ti: 0.0
        tf: 1000.0
        dt: 0.01
        tr: 0.8

We now discuss each of the entry in the file.

The family key
------------------

The ``family`` key determines which class of system (maps, ode's, etc.) is being solved. Therefore, each ``inputs.yml`` file *must* have a ``family`` key. As of now, the only valid value for it is ``ode``. In future, we plan to add other types of families for maps, networks and other types of differential equations.

Depending on the value of the ``family`` key, the other contents of the ``input.yml`` file are determined.

The ode family
~~~~~~~~~~~~~~~~~~

If the ``family`` is ``ode``, then the ``inputs.yml`` file *must* contain the following keys.

#. ``ode_system``: It determines the set of differential equations being used. The value should be a user-defined name which has a corresponding entry in the ``ode.py`` file (discussed later in the document).

#. ``parameters``: This defines the parameters used in the system of ODE's. It lists the variables associated with the parameters and also declares the minimum, maximum and default values for each variable.

#. ``initial_conditions``: This defines dynamical variables as well as their initial values in the system of ODE's. Similar to the parameters, the minimum, maximum and the default values of the dynamical variables are declared.

#. ``time``: This contains time related configurations. It contains: ``ti`` and ``tf`` which give initial time of simulation. The time-step of the simulation is given by ``dt``; and the transience is given by ``tr``. Note that ``tr`` gives the fraction of time-period ``tf-ti`` that will be considered transience and will not be written in the timeseries.