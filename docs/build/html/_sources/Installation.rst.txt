Installation
============

Installing Dynamics is easy. All you require is a linux based machine with Python3 installed on it.

.. attention:: 
    An important and **very** useful tool for installing python based packages is pip. You would require pip3 (pip for python3) for installing Dynamics too. Install pip3 if you don't have it already::

        sudo apt update
        sudo apt install python3-pip


#. Firstly, clone the repository::
   
    git clone https://github.com/arindamsaha1507/dynamics.git

#. A new directory called **dynamics** would have been created in your present working directory. Change into that directory with::

    cd dynamics

#. Install all required packages for dynamics::

    pip3 install -r requirements.txt

#. Test that the installation is successful using::

    python3 run.py

.. note:: 
    Once Dynamics is installed using git, it is very easy to update it to the latest version by running the following command from within the **dynamics** directory::

        git pull

    It is a good practice to update Dynamics every few days to keep up with the latest changes in the code.