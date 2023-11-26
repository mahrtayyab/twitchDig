========================
TwitchDig's Documentation
========================

.. code-block:: python

    from twitchDig.bot import Bot

    app = Bot()

    user = app.get_user("kharltayyab")
    print(user)


* Are you new here? Jump straight into :ref:`installation`!
* Looking for All Available Functions? See :ref:`all-functions`.
* Did you upgrade the library? Please read :ref:`changelog`.


What is this?
-------------

Twitch is a popular video/game streaming platform used by millions of people.
This library is meant to scrape the Videos, Users , Games and Search Results from Twitch.

How should I use the documentation?
-----------------------------------

If you are getting started with the library, you should follow the
documentation in order by pressing the "Next" button at the bottom-right
of every page.

You can also use the menu on the left to quickly skip over sections.

.. toctree::
    :hidden:
    :caption: Get Started

    basic/installation
    basic/quick-start


.. toctree::
    :hidden:
    :caption: References

    basic/all-functions
    basic/twitch_types
    basic/exceptions

.. toctree::
    :hidden:
    :caption: Filters

    basic/filter

.. toctree::
    :hidden:
    :caption: Miscellaneous

    misc/changelog
