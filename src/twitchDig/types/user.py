from .base import BaseGeneratorClass, populate_dict
from ..utils import find_objects
from .twitch_types import *
from ..filters import UserVideosFilters,UserClipsFilters

class UserVideos(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream
    }
    FILTERS = UserVideosFilters

    def __init__(self, client, username, sort, pages, cursor, wait_time):
        self._client = client
        self.username = username
        self.sort = sort
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
            if str(self.username).isdigit():
                response = self._client.request.get_user_videos_by_id(self.username, self.sort, self.cursor)
            else:
                response = self._client.request.get_user_videos_by_username(self.username, self.sort, self.cursor)
            self._raise_error(response)

            _user = find_objects(response, "__typename", "User", recursive=False)
            self.user = User(self._client, _user)

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
        return "UserVideos(user={}, sort={}, results={})".format(
            self.user, self.sort, len(self.results)
        )

class UserClips(BaseGeneratorClass):
    TYPES = {
        "Game": Game,
        "Video": Video,
        "User": User,
        "Channel": User,
        "Stream": Stream,
        "Clip": Clip
    }
    FILTERS = UserClipsFilters

    def __init__(self, client, username, sort, pages, cursor, wait_time):
        self._client = client
        self.username = username
        self.sort = sort
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
            if str(self.username).isdigit():
                response = self._client.request.get_user_clips_by_id(self.username, self.sort, self.cursor)
            else:
                response = self._client.request.get_user_clips_by_username(self.username, self.sort, self.cursor)
            self._raise_error(response)
            _user = find_objects(response, "__typename", "User", recursive=False)

            self.user = User(self._client, _user)
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
        return "UserClips(user={}, sort={}, results={})".format(
            self.user, self.sort, len(self.results)
        )