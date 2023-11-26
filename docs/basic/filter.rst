.. _filter:

===============
Filters
===============


Filter SearchFilters
---------------------

.. py:class:: SearchFilters.GAMES
.. py:class:: SearchFilters.CHANNELS
.. py:class:: SearchFilters.USERS
.. py:class:: SearchFilters.VIDEOS
.. py:class:: SearchFilters.STREAMS

    :reference: `tweety.filters.SearchFilters`

    .. code-block:: python

        from twitchDig.filters import SearchFilters

        # Assuming `app` is Bot Client Object

        app.search("kharltayyab", filter_=SearchFilters.GAMES)


Filter UserVideos
---------------------------

.. py:class:: UserVideosFilters.VIEWS
.. py:class:: UserVideosFilters.DEFAULT
.. py:class:: UserVideosFilters.TIME
.. py:class:: UserVideosFilters.UPLOAD_DATE


    :reference: `tweety.filters.UserVideosFilters`

    .. code-block:: python

        from twitchDig.filters import UserVideosFilters

        # Assuming `app` is Bot Client Object

        app.get_user_videos("kharltayyab", filter_=UserVideosFilters.TIME)

Filter UserClips
---------------------------

.. py:class:: UserClipsFilters.THIS_WEEK
.. py:class:: UserClipsFilters.TODAY
.. py:class:: UserClipsFilters.THIS_MONTH
.. py:class:: UserClipsFilters.DEFAULT
.. py:class:: UserClipsFilters.ALL


    :reference: `tweety.filters.UserClipsFilters`

    .. code-block:: python

        from twitchDig.filters import UserClipsFilters

        # Assuming `app` is Bot Client Object

        app.get_user_clips("kharltayyab", filter_=UserClipsFilters.ALL)

Filter GameStreams
---------------------------

.. py:class:: GameStreamsFilters.DEFAULT
.. py:class:: GameStreamsFilters.VIEWER_COUNT
.. py:class:: GameStreamsFilters.VIEWER_COUNT_ASC


    :reference: `tweety.filters.GameStreamsFilters`

    .. code-block:: python

        from twitchDig.filters import GameStreamsFilters

        # Assuming `app` is Bot Client Object

        app.get_game_clips("tekken 7", filter_=GameStreamsFilters.DEFAULT)


Filter GameVideos
---------------------------

.. py:class:: GameVideosFilters.VIEWS
.. py:class:: GameVideosFilters.DEFAULT
.. py:class:: GameVideosFilters.TIME
.. py:class:: GameVideosFilters.UPLOAD_DATE


    :reference: `tweety.filters.GameVideosFilters`

    .. code-block:: python

        from twitchDig.filters import GameVideosFilters

        # Assuming `app` is Bot Client Object

        app.get_game_videos("tekken 7", filter_=UserVideosFilters.TIME)

Filter GameClips
---------------------------

.. py:class:: GameClipsFilters.THIS_WEEK
.. py:class:: GameClipsFilters.TODAY
.. py:class:: GameClipsFilters.THIS_MONTH
.. py:class:: GameClipsFilters.DEFAULT
.. py:class:: GameClipsFilters.ALL


    :reference: `tweety.filters.GameClipsFilters`

    .. code-block:: python

        from twitchDig.filters import GameClipsFilters

        # Assuming `app` is Bot Client Object

        app.get_game_clips("tekken 7", filter_=UserClipsFilters.ALL)