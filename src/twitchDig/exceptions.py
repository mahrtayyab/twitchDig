class TwitchError(Exception):
    def __init__(self, message, response):
        self.message = message
        self.response = response
        super().__init__(self.message)


class UserNotFound(TwitchError):
    def __init__(self, message, response):
        super().__init__(message, response)


class GameNotFound(TwitchError):
    def __init__(self, message, response):
        super().__init__(message, response)

class AccessTokenNotFound(TwitchError):
    def __init__(self, message, response):
        super().__init__(message, response)
