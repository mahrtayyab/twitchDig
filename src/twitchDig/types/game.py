from .base import BaseGeneratorClass, populate_dict
from ..filters import GameVideosFilters, GameClipsFilters, GameStreamsFilters
from ..utils import find_objects
from .twitch_types import *

class GameStreams(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream
    }
    FILTERS = GameStreamsFilters

    def __init__(self, client, game, tags, sort, pages, cursor, wait_time):
        self._client = client
        self.tags = tags
        self.cursor = cursor
        self._game = game
        self.pages = pages
        self.sort = sort
        self.wait_time = wait_time
        self.has_next_page = True
        self.results = []
        super().__init__()

    @property
    def game(self):
        return self.results[0].game

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            if str(self._game).isdigit():
                response = self._client.request.get_game_streams_by_id(self._game, self.sort, self.tags, self.cursor)
            else:
                response = self._client.request.get_game_streams_by_name(self._game, self.sort, self.tags, self.cursor)
            self._raise_error(response)
            working_object = find_objects(response, "__typename", "Stream", recursive=True)

            if not working_object:
                return thisPage

            items = working_object

            for item in items:
                _type = self.TYPES.get(item.get('__typename', ''))

                if _type:
                    thisPage.append(_type(self._client, item))

            self.results.extend(thisPage)
            self.has_next_page = self._get_cursor(response)
        return thisPage

    def __getitem__(self, index):
        if isinstance(index, str):
            return getattr(self, index)

        return self.results[index]

    def __iter__(self):
        for _result in self.results:
            yield _result

    def __repr__(self):
        return "GameStreams(game={}, tags={}, sort={}, results={})".format(
            self.game, self.tags, self.sort, len(self.results)
        )

class GameClips(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream,
        "Clip": Clip
    }
    FILTERS = GameClipsFilters

    def __init__(self, client, game, sort, languages, pages, cursor, wait_time):
        self._client = client
        self.cursor = cursor
        self.languages = languages
        self._game = game
        self.pages = pages
        self.sort = sort
        self.wait_time = wait_time
        self.has_next_page = True
        self.results = []
        super().__init__()

    @property
    def game(self):
        return self.results[0].game

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            if str(self._game).isdigit():
                response = self._client.request.get_game_clips_by_id(self._game, self.sort, self.languages, self.cursor)
            else:
                response = self._client.request.get_game_clips_by_name(self._game, self.sort, self.languages, self.cursor)
            self._raise_error(response)
            working_object = find_objects(response, "__typename", "Clip", recursive=True)

            if not working_object:
                return thisPage

            items = working_object

            for item in items:
                _type = self.TYPES.get(item.get('__typename', ''))

                if _type:
                    thisPage.append(_type(self._client, item))

            self.results.extend(thisPage)
            self.has_next_page = self._get_cursor(response)
        return thisPage

    def __repr__(self):
        return "GameClips(game={}, languages={}, sort={}, results={})".format(
            self.game, self.languages, self.sort, len(self.results)
        )

class GameVideos(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video
    }

    FILTERS = GameVideosFilters

    def __init__(self, client, game, sort, languages, pages, cursor, wait_time):
        self._client = client
        self.cursor = cursor
        self.languages = languages
        self._game = game
        self.pages = pages
        self.sort = sort
        self.wait_time = wait_time
        self.has_next_page = True
        self.results = []
        super().__init__()

    @property
    def game(self):
        return self.results[0].game

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            if str(self._game).isdigit():
                response = self._client.request.get_game_videos_by_id(self._game, self.sort, self.languages, self.cursor)
            else:
                response = self._client.request.get_game_videos_by_name(self._game, self.sort, self.languages, self.cursor)
            self._raise_error(response)
            working_object = find_objects(response, "__typename", "Video", recursive=True)

            if not working_object:
                return thisPage

            items = working_object

            for item in items:
                _type = self.TYPES.get(item.get('__typename', ''))

                if _type:
                    thisPage.append(_type(self._client, item))

            self.results.extend(thisPage)
            self.has_next_page = self._get_cursor(response)
        return thisPage

    def __repr__(self):
        return "GameVideos(game={}, languages={}, sort={}, results={})".format(
            self.game, self.languages, self.sort, len(self.results)
        )
