import json
from functools import wraps
from urllib.parse import urlencode
from . import models


def return_dict(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        raw_return = f(self, *args, **kwargs)
        if len(raw_return) == 3:
            return dict(method=raw_return[0], url=raw_return[1], json=raw_return[2])

    return wrapper

class GQL:
    URL = "https://gql.twitch.tv/gql"
    POST_METHOD = "POST"
    GET_METHOD = "GET"
    STREAM_LINK = "https://usher.ttvnw.net/api/channel/hls/{username}.m3u8"
    VOD_LINK = "https://usher.ttvnw.net/vod/{video_id}.m3u8"

    @return_dict
    def GetCurrentUser(self):
        json_data = {
            'operationName': 'GetCurrentUser',
            'variables': {
            },
            'query': models.GetCurrentUser,
        }
        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GetUserBadges(self, user_id=None, username=None):
        json_data = {
            'operationName': 'UserBadges',
            'variables': {
                'id': str(user_id),
                'quality': 'QUADRUPLE',
            },
            'query': models.USER_BADGES,
        }

        if user_id:
            json_data['variables']['id'] = str(user_id)
        elif username:
            json_data['variables']['login'] = str(username)
        else:
            raise ValueError("Either user_id or username is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def Search(self, keyword, filter_, cursor=None):
        json_data = {
            'operationName': filter_,
            'variables': {
                'query': str(keyword),
                'first': 30,
                'after': cursor,
            },
            'query': getattr(models, filter_),
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def TopStreams(self, tags, cursor=None):
        json_data = {
            'operationName': 'TopStreams',
            'variables': {
                'tags': tags,
                'first': 30,
                'after': cursor,
            },
            'query': models.TopStreams,
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def UserVideos(self, channel_id=None, username=None, sort=None, cursor=None):
        json_data = {
            'operationName': 'UserVideos',
            'variables': {
                'sort': sort,
                'types': None,
                'first': 30,
                'after': cursor,
            },
            'query': models.UserVideos,
        }
        if channel_id:
            json_data['variables']['id'] = str(channel_id)
        elif username:
            json_data['variables']['login'] = str(username)
        else:
            raise ValueError("Either channel_id or username is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def UserClips(self, channel_id=None, username=None, sort=None, cursor=None):
        json_data = {
            'operationName': 'UserClips',
            'variables': {
                'sort': sort,
                'first': 20,
                'after': cursor
            },
            'query': models.UserClips,
        }
        if channel_id:
            json_data['variables']['id'] = str(channel_id)
        elif username:
            json_data['variables']['login'] = str(username)
        else:
            raise ValueError("Either channel_id or username is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def UserByLogin(self, username):
        json_data = {
            'operationName': 'User',
            'variables': {
                'login': username,
            },
            'query': models.UserByLogin,
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def UserById(self, channel_id):
        json_data = {
            'operationName': 'UserChannelPage',
            'variables': {
                'id': channel_id,
            },
            'query': models.UserChannelPage,
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def TopGames(self, tags, cursor):
        json_data = {
            'operationName': 'TopGames',
            'variables': {
                'tags': tags,
                'first': 30,
                'after': cursor,
            },
            'query': models.TopGames,
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GameStreams(self, game_id=None, game_name=None, sort='VIEWER_COUNT', tags=None, cursor=None):
        json_data = {
            'operationName': 'GameStreams',
            'variables': {
                'sort': sort,
                'tags': tags,
                'first': 30,
                'after': cursor,
            },
            'query': models.GameStreams,
        }
        if game_id:
            json_data['variables']['id'] = str(game_id)
        elif game_name:
            json_data['variables']['name'] = str(game_name)
        else:
            raise ValueError("Either game_id or game_name is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GameVideos(self, game_id=None, game_name=None, sort='VIEWS', languages=None, cursor=None):
        json_data = {
            'operationName': 'GameVideos',
            'variables': {
                'languages': languages,
                'sort': sort,
                'type': None,
                'first': 30,
                'after': cursor,
            },
            'query': models.GameVideos,
        }
        if game_id:
            json_data['variables']['id'] = str(game_id)
        elif game_name:
            json_data['variables']['name'] = str(game_name)
        else:
            raise ValueError("Either game_id or game_name is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GameClips(self, game_id=None, game_name=None, sort='LAST_WEEK', languages=None, cursor=None):
        json_data = {
            'operationName': 'GameClips',
            'variables': {
                'languages': languages,
                'sort': sort,
                'first': 20,
                'after': cursor,
            },
            'query': models.GameClips,
        }
        if game_id:
            json_data['variables']['id'] = str(game_id)
        elif game_name:
            json_data['variables']['name'] = str(game_name)
        else:
            raise ValueError("Either game_id or game_name is required")

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GetStream(self, channel_name):
        json_data = {
            'operationName': 'StreamAccessTokenQuery',
            'variables': {
                'channelName': channel_name,
                'params': {
                    'platform': 'android',
                    'playerType': 'mobile_player',
                },
            },
            'extensions': {
                'persistedQuery': {
                    'version': 1,
                    'sha256Hash': '7eed2ee5b1985ae883ff02635899c40aede59a9d8313e959ae1a80210b71bb15',
                },
            },
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GetVODStream(self, video_id):
        json_data = {
            'extensions': {
                'persistedQuery': {
                    'sha256Hash': '0828119ded1c13477966434e15800ff57ddacf13ba1911c129dc2200705b0712',
                    'version': 1,
                },
            },
            'operationName': 'PlaybackAccessToken',
            'variables': {
                'isLive': False,
                'login': '',
                'isVod': True,
                'vodID': str(video_id),
                'playerType': 'channel_home_live',
            },
        }

        return self.POST_METHOD, self.URL, json_data

    @return_dict
    def GetClipStream(self, clip_slug):
        json_data = {
            'extensions': {
                'persistedQuery': {
                    'sha256Hash': '36b89d2507fce29e5ca551df756d27c1cfe079e2609642b4390aa4c35796eb11',
                    'version': 1,
                },
            },
            'operationName': 'VideoAccessToken_Clip',
            'variables': {
                'slug': clip_slug,
            },
        }
        return self.POST_METHOD, self.URL, json_data

    def GetStreamLink(self, username, signature, token):
        link = self.STREAM_LINK.format(username=username)
        params = {
            "token": str(json.dumps(token)).strip().replace(" ", ""),
            "sig": signature,
            'player_backend': 'Core',
            'fast_bread': 'true',
            'allow_source': 'true',
            'transcode_mode': 'cbr_v1',
        }
        return f"{link}?{urlencode(params)}"

    def GetVODLink(self, video_id, signature, token):
        link = self.VOD_LINK.format(video_id=video_id)
        params = {
            "token": str(json.dumps(token)).strip().replace(" ", ""),
            "sig": signature,
            'player_backend': 'Core',
            'fast_bread': 'true',
            'allow_source': 'true',
            'transcode_mode': 'cbr_v1',
        }
        return f"{link}?{urlencode(params)}"

    @staticmethod
    def getClipLink(url, signature, token):
        params = {
            "token": str(json.dumps(token)).strip().replace(" ", ""),
            "sig": signature,
            'player_backend': 'Core',
            'fast_bread': 'true',
            'allow_source': 'true',
            'transcode_mode': 'cbr_v1',
        }
        return f"{url}?{urlencode(params)}"

