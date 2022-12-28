Configuration
=============

Configuration refers to the settings that determine the specifics of the simulation. For dynamics, these settings are given in the ``inputs.yml`` file in the ``configuration`` directory.

The inputs.yml file
+++++++++++++++++++++++

An example of the configuration file ``inputs.yml`` is as follows:

.. code-block:: yaml

    family: 'ode'

    ode_system: 'fhn'

    parameters:
        a: -0.7
        b: 0.8
        c: 12.5

    initial_conditions:
        x: 0.1
        y: 0.1

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

#. ``parameters``: This defines the parameters used in the system of ODE's. The value is a list of key/value pairs with the key being the variable associated with the parameter and value being its default value to be used in the system.

#. ``initial_conditions``: This defines dynamical variables as well as their initial values in the system of ODE's. Similar to the parameters, the value of this key is a list of key/value pairs with the key being the dynamical variable and value being its initial value to be used in the system.

#. ``time``: This contains time related configurations. It contains a list of key/value pairs:

  * ``ti``: initial time.
  * ``tf``: final time.
  * ``dt``: time-step.
  * ``tr``: transience. This is the fraction of time-period that will be considered transience and will not be written in the timeseries.