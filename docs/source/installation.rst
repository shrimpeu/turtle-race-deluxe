Installation
============

With executable file
--------------------

You can just downlaod the :code:`exe` file in the latest `releases`_ and enjoy the game!

With source code
----------------

The whole source code of this program is also available in `releases`_ in :code:`zip` file, or  clone the repository:

.. _releases: https://github.com/DatSudo/turtle-race-deluxe/releases 

.. code-block:: bash

   git clone https://www.github.com/DatSudo/turtle-race-deluxe.git

Pre-requisites
^^^^^^^^^^^^^^

* Before running the program, the required modules must be installed first:

   .. code-block:: bash

      pip install -r requirements.txt

* If the above command is not working, try

   .. code-block:: bash

      pip3 install -r requirements.txt

* Install :code:`Arcade Classic` font in `assets`_ folder.

.. _assets: https://github.com/DatSudo/turtle-race-deluxe/tree/main/assets/arcadeclassic

**Note:** If you are in Windows, you must install :code:`windows-curses` for :code:`bcrypt` to work.

.. code-block:: bash

   pip install windows-curses

Starting the program
^^^^^^^^^^^^^^^^^^^^

To start the game, try these following commands:

.. code-block:: bash

   python -m main # or
   python3 -m main # or
   py -m main

Documentation
=============

You can access the documentation `here`_.

.. _here: https://datsudo.github.io/turtle-race-deluxe/

License
=======

`GNU General Public License v3.0`_

.. _GNU General Public License v3.0: https://github.com/DatSudo/turtle-race-deluxe/blob/main/LICENSE