from .base import BaseGeneratorClass, populate_dict
from ..utils import find_objects
from .twitch_types import *

class TopGames(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream
    }

    def __init__(self, client, tags, pages, cursor, wait_time):
        self._client = client
        self.tags = tags
        self.cursor = cursor
        self.pages = pages
        self.wait_time = wait_time
        self.has_next_page = True
        self.user = None
        self.results = []
        super().__init__()

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            response = self._client.request.top_games(self.tags, self.cursor)

            working_object = find_objects(response, "__typename", "Game", recursive=True)

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
        return "TopGames(tags={}, results={})".format(
            self.tags, len(self.results)
        )

class TopStreams(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream
    }

    def __init__(self, client, tags, pages, cursor, wait_time):
        self._client = client
        self.tags = tags
        self.cursor = cursor
        self.pages = pages
        self.wait_time = wait_time
        self.has_next_page = True
        self.user = None
        self.results = []
        super().__init__()

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            response = self._client.request.top_streams(self.tags, self.cursor)

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

    def __repr__(self):
        return "TopStreams(tags={}, results={})".format(
            self.tags, len(self.results)
        )