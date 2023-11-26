===========
Quick-Start
===========

Let's see a longer example to learn some of the methods that the library
has to offer.

.. code-block:: python

    from twitchDig.bot import Bot

    app = Bot()

    user = app.get_user("kharltayyab")
    print(user)

Here, we show how to get the user information of the username `kharltayyab`

- Method ``get_user`` returns the instance of `User` class

- Reference to all Classes :ref:`twitch_types`!

