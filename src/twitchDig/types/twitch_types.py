import json

from ..filters import UserVideosFilters, UserClipsFilters
from ..utils import parse_time, find_objects, split_and_make_dict


class Video(dict):
    def __init__(self, client, video_json):
        self._client = client
        self._raw = video_json
        self.broadcast_type = self._raw.get('broadcastType', '')
        self.tags = [Tag(self._client, i) for i in self._raw.get('contentTags', [])]
        self.id = self._raw.get('id', 0)
        self.duration = self._raw.get('lengthSeconds', 0)
        self.preview_thumbnail_URL_large = self._raw.get('previewThumbnailURLLarge', None)
        self.preview_thumbnail_URL_medium = self._raw.get('previewThumbnailURLMedium', None)
        self.date = self._get_date()
        self.title = self._get_title()
        self.view_count = self._get_view_count()
        self.user = User(self._client, self._raw.get('owner')) if self._raw.get('owner') else None
        self.game = Game(self._client, self._raw.get('game')) if self._raw.get('game') else None
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    @property
    def owner(self):
        return self.user

    @property
    def content_tags(self):
        return self.tags

    @property
    def length_seconds(self):
        return self.duration

    @property
    def published_at(self):
        return self.date

    def _get_title(self):
        if self._raw.get('vodTitle'):
            return self._raw['vodTitle']

        return self._raw.get('title', '')

    def _get_date(self):
        if self._raw.get('publishedAt'):
            return parse_time(self._raw.get('publishedAt'))

        return parse_time(self._raw.get('createdAt'))

    def _get_view_count(self):
        if self._raw.get('vodViewCount'):
            return self._raw.get('vodViewCount')

        return self._raw.get('viewCount', 0)

    def get_link(self):
        return self._client.get_video_link(self.id)

    def __repr__(self):
        return "Video(id={}, title={}, date={}, duration={})".format(
            self.id, self.title, self.date, self.duration
        )

class Game(dict):
    def __init__(self, client, game_json):
        self._raw = game_json
        self._client = client
        self.id = self._raw.get('id', 0)
        self.display_name = self._raw.get('displayName', '')
        self.name = self._raw.get('name', '')
        self.original_release_date = parse_time(self._raw.get('originalReleaseDate', None))
        self.viewers_count = self._raw.get('viewersCount', 0)
        self.followers_count = self._raw.get('followersCount', 0)
        self.broadcasters_count = self._raw.get('broadcastersCount', 0)
        self.box_art_URL = self._raw.get('boxArtURL')
        self.cover_URL = self._raw.get('coverURL')
        self.name = self._raw.get('name', '')
        self.tags = [Tag(self._client, i) for i in self._raw.get('gameTags', []) if i.get('__typename', '') == 'Tag']
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    def __repr__(self):
        return "Game(id={}, name={})".format(self.id, self.name)

class Tag(dict):
    def __init__(self, client, tag_json):
        self._raw = tag_json
        self._client = client
        self.id = self._raw.get('id', 0)
        self.isAutomated = self._raw.get('isAutomated', False)
        self.isLanguageTag = self._raw.get('isLanguageTag', False)
        self.localizedDescription = self._raw.get('localizedDescription', '')
        self.localizedName = self._raw.get('localizedName', '')
        self.scope = self._raw.get('scope', None)
        self.tagName = self.name = self._raw.get('tagName', '')
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    def __repr__(self):
        return "Tag(id={}, name={})".format(self.id, self.name)

class User(dict):
    def __init__(self, client, user_json):
        self._raw = user_json
        self._client = client
        self._channelMetadata = self._raw.get('channel', {})
        self.id = self.channel_id = self._raw.get('channelId', 0)
        if not self.id:
            self.id = self.channel_id = self._raw.get('id', 0)

        self.banner_image_URL = self._raw.get('bannerImageURL')
        self.date = self._get_created_at()
        self.description = self._raw.get('description', '')
        self.display_name = self.name = self._raw.get('displayName')
        self.followers_count = self._raw.get('followers', {}).get('totalCount', 0)
        self.login = self.username = self._raw.get('login', '')
        self.profile_image_URL = self._raw.get('profileImageURL')
        self.primary_color_hex = self._raw.get('primaryColorHex')
        self.is_mature = self._raw.get('broadcastSettings', {}).get('isMature', False)
        self.last_broadcast = parse_time(self._raw.get('lastBroadcast', {}).get('startedAt', None))
        self.is_affiliate = self._raw.get('roles', {}).get('isAffiliate', False)
        self.is_partner = self._raw.get('roles', {}).get('isPartner', None)
        self.is_staff = self._raw.get('roles', {}).get('isStaff', None)
        self.is_site_admin = self._raw.get('roles', {}).get('isSiteAdmin', None)
        self.is_global_mod = self._raw.get('roles', {}).get('isGlobalMod', None)
        self.stream = Stream(self._client, self._raw.get('stream')) if self._raw.get('stream') else None
        self.badges = [Badge(self._client, i) for i in self._raw.get('broadcastBadges')] if self._raw.get('broadcastBadges') else []
        self.socials = [Social(self._client, i) for i in self._channelMetadata.get('socialMedias', [])]
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    @property
    def created_at(self):
        return self.date

    def _get_created_at(self):
        if self._raw.get('createdAt'):
            return parse_time(self._raw.get('createdAt'))
        return None

    def get_videos(self, sort=UserVideosFilters.TIME, pages=1, cursor=None, wait_time=2):
        return self._client.get_user_videos(self.id, sort, pages, cursor, wait_time)

    def iter_videos(self, sort=UserVideosFilters.TIME, pages=1, cursor=None, wait_time=2):
        return self._client.iter_user_videos(self.id, sort, pages, cursor, wait_time)

    def get_clips(self, sort=UserClipsFilters.ALL, pages=1, cursor=None, wait_time=2):
        return self._client.get_user_clips(self.id, sort, pages, cursor, wait_time)

    def iter_clips(self, sort=UserClipsFilters.ALL, pages=1, cursor=None, wait_time=2):
        return self._client.iter_user_clips(self.id, sort, pages, cursor, wait_time)

    def __repr__(self):
        return "User(id={}, name={})".format(self.id, self.name)

class Badge(dict):
    def __init__(self, client, badge_json):
        self._raw = badge_json
        self._client = client
        self.id = self.set_id = self._raw.get('setID')
        self.title = self._raw.get('title')
        self.version = self._raw.get('version')
        self.imageURL = self._raw.get('imageURL')
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    def __repr__(self):
        return "Badge(title={}, id={})".format(self.title, self.id)

class Social(dict):
    def __init__(self, client,  social_json):
        self._raw = social_json
        self._client = client
        self.id = self._raw.get('id', 0)
        self.name = self._raw.get('name', '')
        self.title = self._raw.get('title', '')
        self.url = self._raw.get('url', None)
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    def __repr__(self):
        return "Social(name={}, title={})".format(self.name, self.title)


class Stream(dict):
    def __init__(self, client,  stream_json):
        self._raw = stream_json
        self._client = client
        self.fps = self._raw.get('averageFPS', 0)
        self.broadcaster_software = self._raw.get('broadcasterSoftware')
        self.game = Game(self._client, self._raw.get('game')) if self._raw.get('game') else None
        self.height = self._raw.get('height', 0)
        self.id = self._raw.get('id', 0)
        self.is_encrypted = self._raw.get('isEncrypted', False)
        self.preview_image_URL_large = self._raw.get('previewImageURLLarge')
        self.preview_image_URL_medium = self._raw.get('previewImageURLMedium')
        self.preview_image_URL_small = self._raw.get('previewImageURLSmall')
        self.preview_image_URL_template = self._raw.get('previewImageURLTemplate')
        self.date = parse_time(self._raw.get('streamDate'))
        self.tags = [Tag(self._client, i) for i in self._raw.get('streamTags', [])]
        self.title = self._raw.get('streamTitle', '')
        self.view_count = self._raw.get('streamViewCount', 0)
        self.type = self._raw.get('type')
        self.user = self._get_user()
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    @property
    def broadcaster(self):
        return self.user

    def _get_user(self):
        if self._raw.get('streamBroadcaster'):
            return User(self._client, self._raw['streamBroadcaster'])

        if self._raw.get('broadcaster'):
            return User(self._client, self._raw['broadcaster'])

        return None

    def get_link(self):
        return self._client.get_stream_link(self.user.username)

    def __repr__(self):
        return "Stream(id={}, type={}, game={})".format(self.id, self.type, self.game)

class StreamAccessToken(dict):
    def __init__(self, token_json):
        self._raw = token_json
        self.signature = self._raw.get('signature')
        self.value = self.token = json.loads(self._raw.get('value', ''))
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

class Clip(dict):
    def __init__(self, client, clip_json):
        self._raw = clip_json
        self._client = client
        self.date = self._get_created_at()
        self.duration = self._raw.get('durationSeconds')
        self.id = self._raw.get('id')
        self.is_featured = self._raw.get('isFeatured')
        self.creation_state = self._raw.get('creationState')
        self.slug = self._raw.get('slug')
        self.thumbnail_URL = self._raw.get('thumbnailURL')
        self.title = self._raw.get('title')
        self.video_Offset_seconds = self._raw.get('videoOffsetSeconds')
        self.view_count = self._raw.get('viewCount')
        self.video = Video(self._client, self._raw.get('video')) if self._raw.get('video') else None
        self.game = Game(self._client, self._raw.get('game')) if self._raw.get('game') else None
        self.user = User(self._client, self._raw['broadcaster']) if self._raw.get('broadcaster') else None
        super().__init__({k: v for k, v in vars(self).items() if not str(k).startswith("_")})

    @property
    def broadcaster(self):
        return self.user

    @property
    def created_at(self):
        return self.date

    def _get_created_at(self):
        if self._raw.get('createdAt'):
            return parse_time(self._raw.get('createdAt'))
        return None

    def get_link(self):
        return self._client.get_clip_link(self.slug)

    def __repr__(self):
        return "Clip(video={}, game={}, videoOffsetSecond={})".format(
            self.video, self.game, self.video_Offset_seconds
        )

class ChatRoomState:
    def __init__(self, chatroom_client, message):
        self._chatroom_client = chatroom_client
        self.emote_only = None
        self.followers_only = None
        self.subscribers_only = None
        self.r9k = None
        self.room_id = None
        self.slow = None
        self._command = None
        self._channel_name = None
        self._message = message
        self._parse()

    def _parse(self):
        parts = self._message[1:].split(" ")
        self._command = parts[1]
        self._channel_name = parts[2][1:]
        state = split_and_make_dict(parts[3])

        for k, v in state.items():
            key = str(k).replace("@", "").strip()
            if key == "emote-only":
                self.emote_only = True if str(v) != "0" else False
            elif key == "followers-only":
                self.followers_only = True if str(v) != "0" else False
            elif key == "r9k":
                self.r9k = True if str(v) != "0" else False
            elif key == "room-id":
                self.room_id = int(v)
            elif key == "slow":
                self.slow = int(v) if str(v) != "0" else False
            elif key == "subs-only":
                self.subscribers_only = True if str(v) != "0" else False

    def __repr__(self):
        return "ChatRoomState(emote_only={}, followers_only={}, r9k={}, room_id={}, slow={}, subscribers_only={})".format(
            self.emote_only, self.followers_only, self.r9k, self.room_id, self.slow, self.subscribers_only
        )

class ChatMessage:
    def __init__(self, chatroom_client, message):
        self._chatroom_client = chatroom_client
        self.sender_username = None
        self.text = None
        self.badge_info = None
        self.badges = None
        self.color = None
        self.sender_name = None
        self.id = None
        self.mod = None
        self.room_id = None
        self.subscriber = None
        self.time = None
        self.sender_id = None
        self.sender_type = None
        self._message = message
        self._command = None
        self._channel_name = None
        self._parse()
        
    def _parse(self):
        parts = self._message[1:].split(" ")
        prefixes = split_and_make_dict(parts[0], ";", "=")
        self._command = parts[2]
        self._channel_name = parts[3]
        self.sender_username = parts[1][1:str(parts[1]).find("!")]
        self.text = self._message.split(f"{self._channel_name} :")[-1]
        self.badge_info = prefixes.get('badge-info', '')
        self.badges = prefixes.get('badges', '').split(",")
        self.color = prefixes.get('color', '')
        self.sender_name = prefixes.get('display-name', '')
        self.id = prefixes.get('id', '')
        self.mod = True if str(prefixes.get('mod', '')) == "1" else False
        self.room_id = prefixes.get('room-id', '')
        self.subscriber = prefixes.get('subscriber', '')
        self.time = prefixes.get('tmi-sent-ts', '')
        self.sender_id = prefixes.get('user-id', '')
        self.sender_type = prefixes.get('user-type', '')

    def __repr__(self):
        return "ChatMessage(id={}, sender_name={}, time={}, channel_name={})".format(
            self.id, self.sender_name, self.time, self._channel_name
        )