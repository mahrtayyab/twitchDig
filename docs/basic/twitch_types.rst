.. _twitch_types:

=============
Twitch Types
=============

This page contains all the Data Class returned by the different methods


UserVideos
---------------------

.. py:class:: UserVideos

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.user.UserVideos`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Video]

            List of User Videos

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

        .. py:attribute:: username
            :type: str | int

            User Identifier from User

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Video]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``UserVideos(user={user_identifier}, sort={sorting}, results={number_of_results})``


UserClips
---------------------

.. py:class:: UserClips

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.user.UserClips`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Clip]

            List of User Clips

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

        .. py:attribute:: username
            :type: str | int

            User Identifier from User

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Clip]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``UserClips(user={user_identifier}, sort={sorting}, results={number_of_results})``


GameStreams
---------------------

.. py:class:: GameStreams

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.game.GameStreams`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Stream]

            List of Game Stream

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

        .. py:attribute:: game
            :type: Game

            Actual Game in query

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Stream]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``GameStreams(game={game}, tags={tags}, sort={sorting}, results={number_of_results})``

GameClips
---------------------

.. py:class:: GameClips

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.game.GameClips`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Clip]

            List of Game Clip

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

        .. py:attribute:: game
            :type: Game

            Actual Game in query

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Stream]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``GameClips(game={game}, languages={tags}, sort={sorting}, results={number_of_results})``

GameVideos
---------------------

.. py:class:: GameVideos

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.game.GameVideos`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Game]

            List of Game Videos

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

        .. py:attribute:: game
            :type: Game

            Actual Game in query

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Game]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``GameVideos(game={game}, languages={tags}, sort={sorting}, results={number_of_results})``

Search
---------------------

.. py:class:: Search

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.search.Search`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Game | Clip | Stream | User]

            List of results

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Game | Clip | Stream | User]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``Search(keyword={keyword}, filter={filter}, results={number_of_results})``

TopGames
---------------------

.. py:class:: TopGames

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.top.TopGames`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Game]

            List of results

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Game]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``TopGames(tags={tags}, results={number_of_results})``

TopStreams
---------------------

.. py:class:: TopStreams

    Bases : `BaseGeneratorClass`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `twitch_types.types.top.TopStreams`

    .. py:data:: Attributes:

        .. py:attribute:: results
            :type: list[Stream]

            List of results

        .. py:attribute:: cursor
            :type: str

            Cursor for next page

        .. py:attribute:: has_next_page
            :type: bool

            Is next page of results available

    .. py:data:: Methods:

        .. py:method:: get_next_page()

            Get next page of videos if available

            .. py:data:: Return
                :type: list[Stream]


        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :return: ``TopStreams(tags={tags}, results={number_of_results})``

Video
---------------------

.. py:class:: Video

    Bases : `dict`

    .. note:: **This Object is JSON Serializable and Iterable**

    :reference: `tweety.types.twitch_types.Video`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: int

            ID of the Video

        .. py:attribute:: date
            :type: datetime.datetime

            DateTime at which the Video was created

        .. py:attribute:: duration
            :type: str

            Duration of video in seconds

        .. py:attribute:: title
            :type: str

            Title of the Video

        .. py:attribute:: view_count
            :type: str

            View Count of the Video

        .. py:attribute:: user
            :type: User

            User who have uploaded this video

        .. py:attribute:: game
            :type: Game

            Which game is begin played in Twitch

    .. py:data:: Methods:


        .. py:method:: get_link()

            Get m3u8 stream link of the video

            .. py:data:: Return
                :type: str

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``Video(id={id_of_video}, title={title_of_video}, date={date_of_video}, duration={duration_of_video})``

Game
---------------------

.. py:class:: Game

    Bases : `dict`

    .. note:: **This Object is JSON Serializable**

    :reference: `tweety.types.twitch_types.Game`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: str

            ID of the Game

        .. py:attribute:: display_name
            :type: str

            Display Name of the game

        .. py:attribute:: name
            :type: str

            Name of the game


        .. py:attribute:: original_release_date
            :type: datetime.datetime

            Release Date of the Game

        .. py:attribute:: viewers_count
            :type: str

            Viewer Count of the Video

        .. py:attribute:: followers_count
            :type: str

            Followers Count of the Video

        .. py:attribute:: broadcasters_count
            :type: str

            Broadcaster Count of the Video

    .. py:data:: Methods:

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``Game(id={id_of_the_game}, name={name_of_the_game})``


User
---------------------

.. py:class:: User

    Bases : `dict`

    .. note:: **This Object is JSON Serializable**

    :reference: `tweety.types.twitch_types.User`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: int

            ID of the user

        .. py:attribute:: channel_id
            :type: int

            Channel ID of the user

        .. py:attribute:: date
            :type: datetime.datetime

            Date time of the user creation


        .. py:attribute:: description
            :type: str

            Description of the user

        .. py:attribute:: display_name
            :type: str

            Display Name of the User

        .. py:attribute:: followers_count
            :type: int

            Number of followers this user has

        .. py:attribute:: username
            :type: str

            username of the user

        .. py:attribute:: is_mature
            :type: bool

            Do user post mature content [18+]

        .. py:attribute:: is_affiliate
            :type: bool

            Is user affiliate

        .. py:attribute:: is_partner
            :type: bool

            Is user partner of twitch

        .. py:attribute:: is_staff
            :type: bool

            Is user staff member of twitch

        .. py:attribute:: is_site_admin
            :type: bool

            Is user site admin of twitch

        .. py:attribute:: is_global_mod
            :type: bool

            Is user global moderaot of twitch

        .. py:attribute:: stream
            :type: Stream | None

            Ongoing Stream of the user

        .. py:attribute:: socials
            :type: list[Social]

            Social Links of the user

    .. py:data:: Methods:

        .. py:method:: get_videos(sort : str = "TIME", pages=1, cursor=None, wait_time=2)

            Get Video of the User

        .. py:method:: iter_videos(sort : str = "TIME", pages=1, cursor=None, wait_time=2)

            Get Video of the User as generator

        .. py:method:: get_clips(sort : str = "ALL_TIME", pages=1, cursor=None, wait_time=2)

            Get Clips of the User

        .. py:method:: iter_clips(sort : str = "ALL_TIME", pages=1, cursor=None, wait_time=2)

            Get Clips of the User as generator

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``User(id={id_of_user}, name={name_of_user})``

Social
---------------------

.. py:class:: Social

    Bases : `dict`

    .. note:: **This Object is JSON Serializable**

    :reference: `tweety.types.twitch_types.Social`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: str

            ID of the Social Link

        .. py:attribute:: name
            :type: str

            Name of social platform

        .. py:attribute:: title
            :type: str

            Title of social profile


        .. py:attribute:: url
            :type: str

            URL of social profile

    .. py:data:: Methods:

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``Social(name={name}, title={title})``

Stream
---------------------

.. py:class:: Stream

    Bases : `dict`

    .. note:: **This Object is JSON Serializable**

    :reference: `tweety.types.twitch_types.Stream`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: str

            ID of the Stream

        .. py:attribute:: fps
            :type: int

            FPS of stream

        .. py:attribute:: broadcaster_software
            :type: str

            Name of software begin used for broadcasting / stream

        .. py:attribute:: game
            :type: Game

            Game begin played in stream

        .. py:attribute:: date
            :type: datetime.datetime

            Datetime at which the stream was started

        .. py:attribute:: title
            :type: str

            Title of stream

        .. py:attribute:: view_count
            :type: int

            Total Views of the Stream

        .. py:attribute:: user
            :type: User

            User who is streaming

        .. py:attribute:: type
            :type: str

            Type of the stream

    .. py:data:: Methods:

         .. py:method:: get_link()

            Get m3u8 streamable link of the stream

            .. py:data:: Return
                :type: str

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``Stream(id={id}, type={type}, game={game})``

Clip
---------------------

.. py:class:: Clip

    Bases : `dict`

    .. note:: **This Object is JSON Serializable**

    :reference: `tweety.types.twitch_types.Clip`

    .. py:data:: Attributes:

        .. py:attribute:: id
            :type: str

            ID of the Clip

        .. py:attribute:: duration
            :type: int

            Duration of Clip in seconds

        .. py:attribute:: is_featured
            :type: bool

            Is this clip being featured

        .. py:attribute:: slug
            :type: str

            Unique slug of clip

        .. py:attribute:: date
            :type: datetime.datetime

            Datetime at which the clip was created

        .. py:attribute:: title
            :type: str

            Title of Clip

        .. py:attribute:: view_count
            :type: int

            Total Views of the Clip

        .. py:attribute:: user
            :type: User

            User who is streaming

        .. py:attribute:: video_Offset_seconds
            :type: int

            Offset of the video in seconds

        .. py:attribute:: video
            :type: Video

            Video from which this clip was created

        .. py:attribute:: game
            :type: Game

            Game being played in clip

        .. py:attribute:: user
            :type: User

            Who is the owner of this clip

    .. py:data:: Methods:

         .. py:method:: get_link()

            Get m3u8 streamable link of the clip

            .. py:data:: Return
                :type: str

        .. py:method:: __repr__()

            Developer Representation of the Object

            .. py:data:: Return
                :type: str

                :value: ``Clip(video={video}, game={game}, videoOffsetSecond={offset_seconds})``