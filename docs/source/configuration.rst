Overview of the Configuration Files
===================================

Any simulation requires some prior settings to be defined. For dynamics, these settings are given in two files in the ``configuration`` directory. These files are:

* The ``inputs.yml`` file
* The ``ode.py`` file 

While the ODE's of the dynamical system to be simulated are given in ``ode.py``, the general parameters of the simulation are given in ``inputs.yml``. We now look at each of these files in detail.

The inputs.yml file
+++++++++++++++++++++++

The ``inputs.yml`` file determines general settings governing the simulation such as the parameters, initial conditions, timesteps and duration. An example of the file is as follows:

.. literalinclude:: ../../configuration/inputs.yml
    :language: yaml
    :linenos:

We now discuss each of the entry in the file.

The family key
--------------

The ``family`` key determines which class of system (maps, ode's, etc.) is being solved. Therefore, each ``inputs.yml`` file *must* have a ``family`` key. As of now, the only valid value for it is ``ode``. In future, we plan to add other types of families for maps, networks and other types of differential equations.

Depending on the value of the ``family`` key, the other contents of the ``input.yml`` file are determined.

The ode family
~~~~~~~~~~~~~~~~~~

If the ``family`` is ``ode``, then the ``inputs.yml`` file *must* contain the following keys.

#. ``ode_system``: It determines the set of differential equations being used. The value should be a user-defined name which has a corresponding entry in the ``ode.py`` file (discussed later in the document).

#. ``parameters``: This defines the parameters used in the system of ODE's. It lists the variables associated with the parameters and also declares the minimum, maximum and default values for each variable.

#. ``initial_conditions``: This defines dynamical variables as well as their initial values in the system of ODE's. Similar to the parameters, the minimum, maximum and the default values of the dynamical variables are declared.

#. ``time``: This contains time related configurations. It contains: ``ti`` and ``tf`` which give initial time of simulation. The time-step of the simulation is given by ``dt``; and the transience is given by ``tr``. Note that ``tr`` gives the fraction of time-period ``tf-ti`` that will be considered transience and will not be written in the timeseries.

The ode.py file
+++++++++++++++

The ``ode.py`` file defines the exact system of ODE's to be simulated. The file contains the following functions:

#. The ``ode(t, x, p, type)`` function selects the system of ODE based on the ``type`` input and evaluates it for parameter set ``p`` at the dynamical variables defined by ``x``. The argument ``type`` take the same value as ``ode_system`` in the ``inputs.yml`` file.

    .. literalinclude:: ../../configuration/ode.py
        :language: python
        :lines: 4-27
        :lineno-match:
        :linenos:

#. Similarly, the ``jacobian(t, x, p, type)`` function selects the Jacobian of the system based on the ``type`` input and evaluates it for parameter set ``p`` at the dynamical variables defined by ``x``. The argument ``type`` take the same value as ``ode_system`` in the ``inputs.yml`` file.

    .. literalinclude:: ../../configuration/ode.py
        :language: python
        :lines: 29-52
        :lineno-match:
        :linenos:

#. Finally, the file contains the list of systems of ODE's as functions. Note that, for each system of ODE's, the correcponding Jacobians are also defined.

    .. literalinclude:: ../../configuration/ode.py
        :language: python
        :lines: 54-
        :lineno-match:
        :linenos:
