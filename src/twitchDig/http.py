import httpx
from .exceptions import TwitchError
from .utils import custom_json, find_objects
from .gql import GQL

httpx.Response.json_ = custom_json
class Request:
    HEADERS = {
        'Accept': 'multipart/mixed; deferSpec=20220824, application/json',
        'Content-Type': 'application/json',
        'Connection': 'Keep-Alive',
        'Client-ID': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
        'Accept-Language': 'en-us',
        'X-Device-ID': 'c1ba265a605444e83be2581e87774720',
        'Api-Consumer-Type': 'mobile; Android/1608016',
        'X-App-Version': '16.8.1',
        'Client-Session-Id': 'b206b5e7-04a2-4165-8906-ade96cfba088',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 Build/TP1A.221005.002.B2) tv.twitch.android.app/16.8.1/1608016',
    }

    def __init__(self, proxy=None, auth_token=None):
        self._proxy = proxy
        self._auth_token = auth_token
        self._client = httpx.Client(headers=self.HEADERS, proxies=self._proxy)
        self._gql = GQL()

        if self._auth_token:
            self._client.headers.update({"Authorization": f"OAuth {self._auth_token}"})

    @staticmethod
    def _raise_error(response):
        errors = find_objects(response, "errors", None, recursive=False)
        if errors:
            error = errors[0] if isinstance(errors, list) else errors
            raise TwitchError(error.get("message"), response)

    def _send_request(self, **request_data):
        response = self._client.request(**request_data)

        response_json = response.json_()  # noqa

        self._raise_error(response_json)
        if response_json:
            return response.json()

        return response.content

    def get_current_user(self):
        request_data = self._gql.GetCurrentUser()
        response = self._send_request(**request_data)
        return response

    def search(self, keyword, filter_, cursor):
        request_data = self._gql.Search(keyword=keyword, filter_=filter_, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def top_streams(self, tags, cursor):
        request_data = self._gql.TopStreams(tags=tags, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def top_games(self, tags, cursor):
        request_data = self._gql.TopGames(tags=tags, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_user_by_username(self, username):
        request_data = self._gql.UserByLogin(username=username)
        response = self._send_request(**request_data)
        return response

    def get_user_by_id(self, channel_id):
        request_data = self._gql.UserById(channel_id=channel_id)
        response = self._send_request(**request_data)
        return response

    def get_user_videos_by_id(self, channel_id, sort, cursor):
        request_data = self._gql.UserVideos(channel_id=channel_id, sort=sort, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_user_videos_by_username(self, username, sort, cursor):
        request_data = self._gql.UserVideos(username=username, sort=sort, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_user_clips_by_id(self, channel_id, sort, cursor):
        request_data = self._gql.UserClips(channel_id=channel_id, sort=sort, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_user_clips_by_username(self, username, sort, cursor):
        request_data = self._gql.UserClips(username=username, sort=sort, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_user_badges_by_id(self, user_id):
        request_data = self._gql.GetUserBadges(user_id=user_id)
        response = self._send_request(**request_data)
        return response

    def get_user_badges_by_username(self, username):
        request_data = self._gql.GetUserBadges(username=username)
        response = self._send_request(**request_data)
        return response

    def get_game_streams_by_name(self, game_name, sort, tags, cursor):
        request_data = self._gql.GameStreams(game_name=game_name, sort=sort, tags=tags, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_game_streams_by_id(self, game_id, sort, tags, cursor):
        request_data = self._gql.GameStreams(game_id=game_id, sort=sort, tags=tags, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_game_videos_by_name(self, game_name, sort, languages, cursor):
        request_data = self._gql.GameVideos(game_name=game_name, sort=sort, languages=languages, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_game_videos_by_id(self, game_id, sort, languages, cursor):
        request_data = self._gql.GameVideos(game_id=game_id, sort=sort, languages=languages, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_game_clips_by_name(self, game_name, sort, languages, cursor):
        request_data = self._gql.GameClips(game_name=game_name, sort=sort, languages=languages, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_game_clips_by_id(self, game_id, sort, languages, cursor):
        request_data = self._gql.GameClips(game_id=game_id, sort=sort, languages=languages, cursor=cursor)
        response = self._send_request(**request_data)
        return response

    def get_stream_access_token(self, channel_name):
        request_data = self._gql.GetStream(channel_name=channel_name)
        response = self._send_request(**request_data)
        return response

    def get_vod_access_token(self, video_id):
        request_data = self._gql.GetVODStream(video_id=video_id)
        response = self._send_request(**request_data)
        return response

    def get_clip_access_token(self, clip_slug):
        request_data = self._gql.GetClipStream(clip_slug=clip_slug)
        response = self._send_request(**request_data)
        return response

    def get_stream_link(self, username, signature, token):
        return self._gql.GetStreamLink(username, signature, token)

    def get_vod_link(self, video_id, signature, token):
        return self._gql.GetVODLink(video_id, signature, token)

    def get_clip_link(self, url, signature, token):
        return self._gql.getClipLink(url, signature, token)
