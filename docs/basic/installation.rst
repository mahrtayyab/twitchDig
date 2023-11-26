.. _installation:

============
Installation
============

TwitchDig is a Python library, which means you need to download and install
Python from https://www.python.org/downloads/ if you haven't already. Once
you have Python installed, `upgrade pip`__ and run:

.. code-block:: sh

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade twitchDig

.. __: https://pythonspeed.com/articles/upgrade-pip/

**Please** do check the full documentation before upgrading if upgrading to new version

Dependencies
=====================

httpx_ : The library will be used to make the http/2 requests to Twitch

websocket_ : The library will be used to connect to chat socket


.. _httpx: https://github.com/encode/httpx
.. _websocket: https://github.com/websocket-client/websocket-client