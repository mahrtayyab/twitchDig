.. _exceptions:

=============
Exceptions
=============

This page contains all the Exceptions raised by the different methods

TwitchError
------------------------

.. py:class:: TwitchError

    Bases : `Exception`

    :description: **This Exception is base exception for all other exceptions raised.**

    :reference: `tweety.exceptions.TwitchError`

    .. py:data:: Attributes:

        .. py:attribute:: message
            :type: str

            Main Exception Message

        .. py:attribute:: response
            :type: httpx.Response

            Raw Response returned by the Twitch

UserNotFound
------------------------

.. py:class:: UserNotFound

    Bases : `TwitchError`

    :description: **This Exception is raised when queries user is not found.**

    :reference: `tweety.exceptions.UserNotFound`

GameNotFound
------------------------

.. py:class:: GameNotFound

    Bases : `TwitchError`

    :description: **This Exception is raised when queries game is not found.**

    :reference: `tweety.exceptions.GameNotFound`

AccessTokenNotFound
------------------------

.. py:class:: AccessTokenNotFound

    Bases : `TwitchError`

    :description: **This Exception is raised when access token for a m3u8 link not found.**

    :reference: `tweety.exceptions.AccessTokenNotFound`