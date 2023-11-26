from .base import BaseGeneratorClass, populate_dict
from ..filters import SearchFilters
from ..utils import find_objects
from .twitch_types import *

class Search(BaseGeneratorClass):
    KEYS = {
        SearchFilters.VIDEOS: "Video",
        SearchFilters.CHANNELS: "User",
        SearchFilters.GAMES: "Game",
        SearchFilters.STREAMS: "Stream",
    }

    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream
    }

    FILTERS = KEYS.keys()

    def __init__(self, client, keyword, filter_, pages, cursor, wait_time):
        self._client = client
        self.keyword = keyword
        self.filter = filter_
        self.cursor = cursor
        self.pages = pages
        self.wait_time = wait_time
        self.has_next_page = True
        self.results = []
        super().__init__()

    @populate_dict(["results", "has_next_page", "cursor"])
    def get_next_page(self):
        thisPage = []
        if self.has_next_page:
            response = self._client.request.search(self.keyword, self.filter, self.cursor)
            working_object = find_objects(response, "__typename", self.KEYS.get(self.filter), recursive=True)

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
        return "Search(keyword={}, filter={}, results={})".format(
            self.keyword, self.filter, len(self.results)
        )