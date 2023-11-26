
.. _all-functions:

=============
All Available Functions
=============

This page contains all the public method available to work with

.. note:: All Examples on the page assumes that `app` is the `Bot` class instance

Get User Info
---------------------

- .. py:method:: Bot().get_user(username: str)

    Get the User Info of the specified username or user_id

    .. py:data:: Arguments

        .. py:data:: username
            :type: str

            Username or User ID of the user you want to get info of.


    .. py:data:: Return

        :return: `User`


    .. code-block:: python

       user = app.get_user('kharltayyab')


Get User Videos
---------------------

- .. py:method:: Bot().get_user_videos(username: str ,sort: str = "TIME", pages: int = 1, cursor: str = None, wait_time: int = 2)

    Get the Videos of the specified username

    .. py:data:: Arguments

        .. py:data:: username (Required)
            :type: str

            Username or User ID of the user you want to get Videos of.

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Videos Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `UserVideos`


    .. code-block:: python

       videos = app.get_user_videos('kharltayyab')
       for video in videos:
           print(video)


- .. py:method:: Bot().iter_user_videos(username: str ,sort: str = "TIME", pages: int = 1, cursor: str = None, wait_time: int = 2)

    Get the Videos of the specified username as a generator

    .. py:data:: Arguments

        .. py:data:: username (Required)
            :type: str

            Username or User ID of the user you want to get Videos of.

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Videos Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: Generator : (`UserVideos` , list[`Video`])


    .. code-block:: python

       for _, videos in app.iter_user_videos('kharltayyab'):
           print(videos)

Get User Video Clips
---------------------

- .. py:method:: Bot().get_user_clips(username: str ,sort: str = "TIME", pages: int = 1, cursor: str = None, wait_time: int = 2)

    Get the Videos Clips of the specified username

    .. py:data:: Arguments

        .. py:data:: username (Required)
            :type: str

            Username or User ID of the user you want to get Video Clips of.

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Clips Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `UserClips`


    .. code-block:: python

       clips = app.get_user_clips('kharltayyab')
       for clip in clips:
           print(clip)


- .. py:method:: Bot().iter_user_clips(username: str ,sort: str = "TIME", pages: int = 1, cursor: str = None, wait_time: int = 2)

    Get the Video Clips of the specified username as a generator

    .. py:data:: Arguments

        .. py:data:: username (Required)
            :type: str

            Username or User ID of the user you want to get Video Clips of.

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Clips Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: Generator : (`UserClips` , list[`Clip`])


    .. code-block:: python

       for _, clips in app.iter_user_clips('kharltayyab'):
           print(clips)


Searching a Keyword
---------------------

- .. py:method:: Bot().search(keyword: str, filter_: str = "SearchStreams", pages: int = 1, wait_time: int = 2, cursor: str = None)

    Search for a on Twitch

    .. py:data:: Arguments

        .. py:data:: keyword (Required)
            :type: str

            The keyword which is supposed to be searched

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get


        .. py:data:: filter_ (optional)
            :type: str
            :value: "SearchStreams"

            Filter you would like to apply on the search. More about :ref:`filter`

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `Search`


    .. code-block:: python

       results = app.search('kharltayyab')
       for result in results:
           print(result)

- .. py:method:: Bot().iter_search(keyword: str, filter_: str = "SearchStreams", pages: int = 1, wait_time: int = 2, cursor: str = None)

    Search for a on Twitch as a generator

    .. py:data:: Arguments

        .. py:data:: keyword (Required)
            :type: str

            The keyword which is supposed to be searched

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get


        .. py:data:: filter_ (optional)
            :type: str
            :value: "SearchStreams"

            Filter you would like to apply on the search. More about :ref:`filter`

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: Generator: (`Search`, list[`Clip` | `Video` | `User` | `Stream`])


    .. code-block:: python

       for _, results in app.iter_search('kharltayyab'):
           print(results)

Get Top Streams
---------------------

- .. py:method:: Bot().get_top_streams(tags: List[str] = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Twitch Top Streams

    .. py:data:: Arguments

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `TopStreams`


    .. code-block:: python

       streams = app.get_top_streams()
       for stream in streams:
           print(stream)

- .. py:method:: Bot().iter_top_streams(tags: List[str] = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Twitch Top Streams as generator

    .. py:data:: Arguments

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `TopStreams`, list[`Stream`]


    .. code-block:: python

       for _, streams in app.iter_top_streams():
           print(streams)


Get Top Games
---------------------

- .. py:method:: Bot().get_top_games(tags: List[str] = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Twitch Top Games

    .. py:data:: Arguments

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `TopGames`


    .. code-block:: python

       games = app.get_top_games()
       for game in games:
           print(game)

- .. py:method:: Bot().iter_top_games(tags: List[str] = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Twitch Top Games as generator

    .. py:data:: Arguments

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `TopStreams`, list[`Game`]


    .. code-block:: python

       for _, games in app.iter_top_games():
           print(games)

Get Game Streams
---------------------

- .. py:method:: Bot().get_game_streams(game: Union[str, int, Game], tags: List[str] = None, sort: str = "VIEWER_COUNT", pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Streams of specific game

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameStreams`


    .. code-block:: python

       streams = app.get_game_streams()
       for stream in streams:
           print(stream)

- .. py:method:: Bot().iter_top_games(game: Union[str, int, Game], tags: List[str] = None, sort: str = "VIEWER_COUNT", pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Streams of specific game as generator

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: tags
            :type: list[str]

            List of tags to look for in streams

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameStreams`, list[`Stream`]


    .. code-block:: python

       for _, streams in app.iter_game_streams():
           print(streams)

Get Game Clips
---------------------

- .. py:method:: Bot().get_game_clips(game: Union[str, int, Game], sort: str = "VIEWER_COUNT", languages: str = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Clips of specific game

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: languages
            :type: str

            What should be the language of clip

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameClips`


    .. code-block:: python

       clips = app.get_game_clips()
       for clip in clips:
           print(clip)

- .. py:method:: Bot().iter_game_clips(game: Union[str, int, Game], sort: str = "VIEWER_COUNT", languages: str = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Clips of specific game as generator

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: languages
            :type: str

            What should be the language of clip

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameClips`, list[`Clip`]


    .. code-block:: python

       for _, clips in app.get_game_clips():
           print(clips)

Get Game Videos
---------------------

- .. py:method:: Bot().get_game_videos(game: Union[str, int, Game], sort: str = "VIEWER_COUNT", languages: str = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Videos of specific game

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: languages
            :type: str

            What should be the language of clip

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameVideos`


    .. code-block:: python

       videos = app.get_game_videos()
       for video in videos:
           print(video)

- .. py:method:: Bot().iter_game_videos(game: Union[str, int, Game], sort: str = "VIEWER_COUNT", languages: str = None, pages: int = 1, wait_time: int = 2, cursor: str = None)

    Get Videos of specific game as generator

    .. py:data:: Arguments

        .. py:data:: game
            :type: str

            Name of the Game

        .. py:data:: languages
            :type: str

            What should be the language of clip

        .. py:data:: sort
            :type: str

            Sort the Results

        .. py:data:: pages (optional)
            :type: int
            :value: 1

            Number of Pages you want to get

        .. py:data:: wait_time (optional)
            :type: int
            :value: 2

            Number of seconds to wait between multiple requests

        .. py:data:: cursor (optional)
            :type: str
            :value: None

             Pagination cursor if you want to get the pages from that cursor up-to (This cursor is different from actual API cursor)


    .. py:data:: Return

        :return: `GameVideos`, list[`Video`]


    .. code-block:: python

       for _, videos in app.get_game_videos():
           print(videos)