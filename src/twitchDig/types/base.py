import time
from functools import wraps
from ..filters import Languages, SearchFilters
from ..utils import find_objects, parse_wait_time
from ..exceptions import GameNotFound, UserNotFound


class BaseGeneratorClass(dict):

    def __init__(self):
        super().__init__()
        self._parse_args()

    def _parse_args(self):
        if hasattr(self, "languages"):
            if not self.languages or self.languages not in Languages:
                self.languages = None

        if hasattr(self, "sort") and hasattr(self, "FILTERS"):
            if self.sort not in list(self.FILTERS) or not self.sort:
                self.sort = self.FILTERS.DEFAULT

        if hasattr(self, "filter") and hasattr(self, "FILTERS"):
            if self.filter not in list(self.FILTERS) or not self.filter:
                self.filter = SearchFilters.STREAMS

        if hasattr(self, "tags"):
            if isinstance(self.tags, str):
                self.tags = [self.tags]
            elif isinstance(self.tags, (tuple, list, set)):
                self.tags = [i for i in self.tags]
            else:
                self.tags = []

    def _get_cursor(self, response):
        cursor = find_objects(response, "cursor", value=None)

        if not cursor:
            return False

        if isinstance(cursor, list):
            try:
                cursor = [i for i in cursor if i][0]
            except IndexError:
                return False

        if cursor == self.cursor:
            return False

        self.cursor = cursor
        return True

    def generator(self):
        for page in range(1, int(self.pages) + 1):
            results = self.get_next_page()

            yield self, results

            if not self.has_next_page:
                break

            if page != self.pages:
                time.sleep(parse_wait_time(self.wait_time))

        return self

    def __getitem__(self, index):
        if isinstance(index, str):
            return getattr(self, index)

        return self.results[index]

    def __iter__(self):
        for _result in self.results:
            yield _result

    def _raise_error(self, response):
        if "Game" in str(self.__class__.__name__):
            if not response.get('data', {}).get('game', {}):
                raise GameNotFound("Game not Found", response)
        elif "User" in str(self.__class__.__name__):
            if not response.get('data', {}).get('user', {}):
                raise UserNotFound("User not Found", response)

def populate_dict(attributes):
    _attributes = [i for i in attributes]

    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            value = method(self, *args, **kwargs)
            for attribute in _attributes:
                if hasattr(self, attribute):
                    self[attribute] = getattr(self, attribute)
            return value
        return wrapper
    return decorator
