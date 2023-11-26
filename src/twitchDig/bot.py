from typing import Union, Tuple, List, Generator
from .http import Request
from .filters import UserVideosFilters, UserClipsFilters, GameStreamsFilters, GameClipsFilters, GameVideosFilters, \
    SearchFilters
from .types.search import Search
from .types.twitch_types import StreamAccessToken, User, Video, Stream, Clip, Game
from .types.user import UserVideos, UserClips
from .types.top import TopGames, TopStreams
from .types.game import GameStreams, GameClips, GameVideos
from .exceptions import UserNotFound, AccessTokenNotFound
from .utils import find_objects, parse_game_from_object, parse_user_from_object


class Bot:
    def __init__(self, auth_token=None, proxy=None):
        self.auth_token = auth_token
        self.request = Request(proxy=proxy, auth_token=auth_token)
        self.me = None

        if self.auth_token:
            self.me = self._get_current_user()

        self.get_channel = self.get_user

    def _get_current_user(self):
        response = self.request.get_current_user()
        user = response.get("data", {}).get('currentUser')
        if not user:
            raise ValueError("Invalid Auth Token")

        return User(self, user)

    def get_user(self, username) -> User:
        """
        Get a User Info

        :param username: Either username , channel_name or user_id
        :return: .type.twitch_types.User
        """

        if str(username).isdigit():
            response = self.request.get_user_by_id(username)
        else:
            response = self.request.get_user_by_username(username)

        user = response.get('data', {}).get('user')

        if not user:
            raise UserNotFound("User Not Found", response)

        return User(self, user)

    def get_user_videos(
            self,
            username: Union[str, int, Video, User, Stream, Clip],
            sort: str = UserVideosFilters.TIME,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> UserVideos:
        """
        Get the Videos of the User

        :param username: username or user_id
        :param sort: UserVideosFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests
        :return: .types.user.UserVideos
        """

        username = parse_user_from_object(username)

        user_videos = UserVideos(self, username, sort=sort, pages=pages, cursor=cursor, wait_time=wait_time)
        list(user_videos.generator())
        return user_videos

    def iter_user_videos(
            self,
            username: Union[str, int, Video, User, Stream, Clip],
            sort: str = UserVideosFilters.TIME,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[UserVideos, List[Video], None]:
        """
        Get the Videos of the User as Generator

        :param username: username or user_id
        :param sort: UserVideosFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.user.UserVideos, List[Video]
        """

        username = parse_user_from_object(username)

        user_videos = UserVideos(self, username, sort=sort, pages=pages, cursor=cursor, wait_time=wait_time)
        return user_videos.generator()

    def get_user_clips(
            self,
            username: Union[str, int, Video, User, Stream, Clip],
            sort: str = UserClipsFilters.ALL,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> UserClips:
        """
        Get the Clips of User

        :param username: username or user_id
        :param sort: UserClipsFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .type.user.UserClips
        """

        username = parse_user_from_object(username)
        user_clips = UserClips(self, username, sort=sort, pages=pages, cursor=cursor, wait_time=wait_time)
        list(user_clips.generator())
        return user_clips

    def iter_user_clips(
            self,
            username: Union[str, int, Video, User, Stream, Clip],
            sort: str = UserClipsFilters.ALL,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[UserClips, List[Clip], None]:
        """
         Get the Clips of User as Generator

        :param username: username or user_id
        :param sort: UserClipsFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .type.user.UserClips, List[Clip]
        """

        username = parse_user_from_object(username)
        user_clips = UserClips(self, username, sort=sort, pages=pages, cursor=cursor, wait_time=wait_time)
        return user_clips.generator()

    def search(
            self,
            keyword: str,
            filter_: str = SearchFilters.STREAMS,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Search:
        """
        Search a keyword

        :param keyword: Actual Search Term
        :param filter_: Filters to apply on search (SearchFilters)
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.search.Search
        """

        search = Search(self, keyword, filter_, pages, cursor, wait_time)
        list(search.generator())
        return search

    def iter_search(
            self,
            keyword: str,
            filter_: str = SearchFilters.STREAMS,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[Search, List[Union[Clip, Video, User, Stream]], None]:

        """
        Search a keyword as Generator

        :param keyword: Actual Search Term
        :param filter_: Filters to apply on search (SearchFilters)
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.search.Search, List[Clip, Video, Stream, User]
        """

        search = Search(self, keyword, filter_, pages, cursor, wait_time)
        return search.generator()

    def get_top_streams(
            self,
            tags: List[str] = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> TopStreams:
        """
        Get Top Streams

        :param tags: List of tags to look for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.top.TopStreams
        """

        top_streams = TopStreams(self, tags, pages, cursor, wait_time)
        list(top_streams.generator())
        return top_streams

    def iter_top_streams(
            self,
            tags: List[str] = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[TopStreams, List[Stream], None]:
        """
        Get Top Streams as generator

        :param tags: List of tags to look for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.top.TopStreams, List[.types.twitch_types.Stream]
        """

        top_streams = TopStreams(self, tags, pages, cursor, wait_time)
        return top_streams.generator()

    def get_top_games(
            self,
            tags: List[str] = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> TopGames:
        """
        Get Top Games

        :param tags: List of tags to look for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.top.TopGames
        """

        top_games = TopGames(self, tags, pages, cursor, wait_time)
        list(top_games.generator())
        return top_games

    def iter_top_games(
            self,
            tags: List[str] = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[TopGames, List[Game], None]:
        """
        Get Top Games as Generator

        :param tags: List of tags to look for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.top.TopGames, List[.types.twitch_types.Game]
        """

        top_games = TopGames(self, tags, pages, cursor, wait_time)
        return top_games.generator()

    def get_game_streams(
            self,
            game: Union[str, int, Game],
            tags: List[str] = None,
            sort: str = GameStreamsFilters.VIEWER_COUNT,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> GameStreams:

        """
        Get Streams of specific Game
        :param game: Actual Game you are looking for
        :param tags: List of tags to look for
        :param sort: GameStreamsFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameStreams
        """

        game = parse_game_from_object(game)
        game_streams = GameStreams(self, game, tags, sort, pages, cursor, wait_time)
        list(game_streams.generator())
        return game_streams

    def iter_game_streams(
            self,
            game: Union[str, int, Game],
            tags: List[str] = None,
            sort: str = GameStreamsFilters.VIEWER_COUNT,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[GameStreams, List[Stream], None]:

        """
        Get Streams of specific Game as generator
        :param game: Actual Game you are looking for
        :param tags: List of tags to look for
        :param sort: GameStreamsFilters Sort
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameStreams, List[Stream]
        """

        game = parse_game_from_object(game)
        game_streams = GameStreams(self, game, tags, sort, pages, cursor, wait_time)
        return game_streams.generator()

    def get_game_clips(
            self,
            game: Union[str, int, Game],
            sort: str = GameClipsFilters.ALL,
            languages: str = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> GameClips:
        """
        Get the recorded clips of a specific game

        :param game: Actual Game you are looking for
        :param sort: GameClipsFilters Sort
        :param languages: Language of clip you are looking for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameClips
        """

        game = parse_game_from_object(game)
        game_clips = GameClips(self, game, sort, languages, pages, cursor, wait_time)
        list(game_clips.generator())
        return game_clips

    def iter_game_clips(
            self,
            game: Union[str, int, Game],
            sort: str = GameClipsFilters.ALL,
            languages: str = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[GameClips, List[Clip], None]:
        """
        Get the recorded clips of a specific game as generator

        :param game: Actual Game you are looking for
        :param sort: GameClipsFilters Sort
        :param languages: Language of clip you are looking for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameClips, List[Clip]
        """

        game = parse_game_from_object(game)
        game_clips = GameClips(self, game, sort, languages, pages, cursor, wait_time)
        return game_clips.generator()

    def get_game_videos(
            self,
            game: Union[str, int, Game],
            sort: str = GameVideosFilters.VIEWS,
            languages: str = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> GameVideos:
        """
        Get the videos of a specific game

        :param game: Actual Game you are looking for
        :param sort: GameClipsFilters Sort
        :param languages: Language of clip you are looking for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                          if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameVideos
        """

        game = parse_game_from_object(game)
        game_videos = GameVideos(self, game, sort, languages, pages, cursor, wait_time)
        list(game_videos.generator())
        return game_videos

    def iter_game_videos(
            self,
            game: Union[str, int, Game],
            sort: str = GameVideosFilters.VIEWS,
            languages: str = None,
            pages: int = 1,
            cursor: str = None,
            wait_time: Union[int, str, Tuple, List] = 2
    ) -> Generator[GameVideos, List[Video], None]:
        """
        Get the videos of a specific game as generator

        :param game: Actual Game you are looking for
        :param sort: GameClipsFilters Sort
        :param languages: Language of clip you are looking for
        :param pages: Number of pages to get
        :param cursor: Pagination Cursor to get the results from that cursor up-to
        :param wait_time: Number of seconds to wait between multiple requests,
                         if iterable is provided , it will randomly select the wait time between first two elements
        :return: .types.game.GameVideos, List[Video]
        """

        game = parse_game_from_object(game)
        game_videos = GameVideos(self, game, sort, languages, pages, cursor, wait_time)
        return game_videos.generator()

    @staticmethod
    def _get_access_token(response):
        PlaybackAccessToken = find_objects(response, "__typename", "PlaybackAccessToken", recursive=False)
        if not PlaybackAccessToken:
            raise AccessTokenNotFound("Access Token Not Found", response)

        return StreamAccessToken(PlaybackAccessToken)

    def _get_stream_token(self, username):
        response = self.request.get_stream_access_token(username)
        return self._get_access_token(response)

    def _get_vod_access_token(self, video_id):
        response = self.request.get_vod_access_token(video_id)
        return self._get_access_token(response)

    def _get_clip_access_token(self, clip_slug):
        response = self.request.get_clip_access_token(clip_slug)
        return self._get_access_token(response)

    def get_stream_link(self, username):
        access_token = self._get_stream_token(username)
        return self.request.get_stream_link(username, access_token.signature, access_token.token)

    def get_video_link(self, video_id):
        access_token = self._get_vod_access_token(video_id)
        return self.request.get_vod_link(video_id, access_token.signature, access_token.token)

    def get_clip_link(self, clip_slug):
        access_token = self._get_clip_access_token(clip_slug)
        url = access_token.value['clip_uri']
        return self.request.get_clip_link(url, access_token.signature, access_token.token)

