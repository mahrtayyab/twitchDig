
_ROLES = """
isAffiliate
isGlobalMod 
isPartner 
isSiteAdmin 
isStaff
"""

_SOCIAL = """
__typename
id
name
title
url
"""


_BADGE = """
__typename
imageURL
setID 
title 
version 
"""

_CHANNEL = """
__typename
socialMedias { _social_ }
""".replace("_social_", _SOCIAL)

_USER_STREAM = """
 __typename
id
createdAt
previewImageURL
freeformTags { name } 
type
viewersCount
averageFPS
broadcasterSoftware
height
"""

_BROADCASTER = _USER = """
__typename
broadcastSettings { title isMature }
createdAt
displayName
primaryColorHex
id
broadcastBadges { _badge_ }
login
profileImageURL(width: 300)
roles { _roles_ }
followers { totalCount }
bannerImageURL
description
lastBroadcast { startedAt }
freeformTags { name }
channel { _channel_ }
stream { _stream_ }
""".replace("_roles_", _ROLES).replace("_channel_", _CHANNEL).replace("_badge_", _BADGE).replace("_stream_", _USER_STREAM)

_GAME = """
__typename
id
displayName
name
tags(tagType: CONTENT) { id localizedName } 
originalReleaseDate
viewersCount
followersCount
broadcastersCount
boxArtURL
"""

_ACCESS_TOKEN = """
__typename
signature
value
"""

_STREAM = """
__typename
id
createdAt
broadcaster { _broadcaster_ }
game { _game_ }
previewImageURL
freeformTags { name } 
type
viewersCount
averageFPS
broadcasterSoftware
height
""".replace("_broadcaster_", _BROADCASTER).replace("_game_", _GAME)

_VIDEO = """
__typename
animatedPreviewURL 
broadcastType 
contentTags { id localizedName } 
createdAt 
game { _game_ } 
id 
lengthSeconds
owner { _user_ } 
previewThumbnailURL 
title 
viewCount 
""".replace("_game_", _GAME).replace("_user_", _USER)

# playbackAccessToken { _playback_access_token_ }

_CLIP = """
__typename
createdAt
id
isFeatured
durationSeconds
broadcaster { _broadcaster_ }
creationState
game { _game_ } 
slug 
thumbnailURL 
title 
video { _video_ } 
videoOffsetSeconds 
viewCount 
""".replace("_game_", _GAME).replace("_broadcaster_", _USER).replace("_video_", _VIDEO).replace("_playback_access_token_", _ACCESS_TOKEN)


GetCurrentUser = """
query GetCurrentUser { 
    currentUser { 
        _broadcaster_ 
    } 
}
""".replace("_broadcaster_", _USER)

TopStreams = """
query TopStreams($tags: [String!], $first: Int, $after: Cursor) {
    streams(first: $first, after: $after, options: { freeformTags: $tags }) {
        edges {
            cursor
            node { _stream_ }
        }
        pageInfo {
            hasNextPage
        }
    }
}
""".replace("_stream_", _STREAM)

SearchVideos = """
query SearchVideos($query: String!, $first: Int, $after: String) {
    searchFor(userQuery: $query, platform: "", target: { cursor: $after index: VOD limit: $first } ) {
        videos {
            cursor 
            items { _video_ } 
            pageInfo { 
                hasNextPage 
            } 
        } 
    } 
}
""".replace("_video_", _VIDEO)

SearchStreams = """
query SearchStreams($query: String!, $first: Int, $after: Cursor) { 
    searchStreams(userQuery: $query, first: $first, after: $after) { 
        edges { 
            cursor 
            node { _stream_ } 
        } 
        pageInfo { 
            hasNextPage 
        } 
    } 
}
""".replace("_stream_", _STREAM)

SearchChannels = """
query SearchChannels($query: String!, $first: Int, $after: Cursor) { 
    searchUsers(userQuery: $query, first: $first, after: $after) { 
        edges { 
            cursor 
            node { _user_ } 
        } 
        pageInfo { 
            hasNextPage 
        } 
    } 
}
""".replace("_user_", _USER)

SearchGames = """
query SearchGames($query: String!, $first: Int, $after: Cursor) { 
    searchCategories(query: $query, first: $first, after: $after) { 
        edges { 
            cursor 
            node { _game_ } 
        } 
        pageInfo { 
            hasNextPage 
        } 
    } 
}
""".replace("_game_", _GAME)

UserChannelPage = """
query UserChannelPage($id: ID, $login: String) { 
    user(id: $id, login: $login, lookupType: ALL) { _user_ } 
}
""".replace("_user_", _USER)

UserByLogin = """
query User($id: ID, $login: String) { 
    user(id: $id, login: $login, lookupType: ALL) { _user_ } 
}""".replace("_user_", _USER)

UserVideos = """
query UserVideos($id: ID, $login: String, $sort: VideoSort, $types: [BroadcastType!], $first: Int, $after: Cursor) { 
    user(id: $id, login: $login, lookupType: ALL) { 
        _user_
        videos(first: $first, after: $after, types: $types, sort: $sort) { 
            edges { 
                cursor 
                node { _video_ } 
            } 
            pageInfo { 
                hasNextPage 
            } 
        } 
    } 
}
""".replace("_user_", _USER).replace("_video_", _VIDEO)

UserClips = """
query UserClips($id: ID, $login: String, $sort: ClipsPeriod, $first: Int, $after: Cursor) { 
    user(id: $id, login: $login, lookupType: ALL) { 
        clips(first: $first, after: $after, criteria: { 
            period: $sort 
        } 
    )  { 
        edges { 
            cursor 
            node { _clip_ } 
        } 
        pageInfo { 
            hasNextPage 
        } 
    } 
    _user_
} 
}
""".replace("_clip_", _CLIP).replace("_user_", _USER)

TopGames = """
query TopGames($tags: [String!], $first: Int, $after: Cursor) { 
    games(first: $first, after: $after, options: { tags: $tags } ) { 
        edges { 
            cursor 
            node { _game_ } 
        } 
        pageInfo { 
            hasNextPage 
        } 
    } 
}
""".replace("_game_", _GAME)

GameStreams = """
query GameStreams($id: ID, $name: String, $sort: StreamSort, $tags: [String!], $first: Int, $after: Cursor) { 
    game(id: $id, name: $name) { 
        streams(first: $first, after: $after, options: { 
            sort: $sort freeformTags: $tags 
        } 
    ) { 
        edges { 
            cursor 
                node { _stream_ } 
            } 
            pageInfo { 
                hasNextPage 
            } 
        } 
    } 
}
""".replace("_stream_", _STREAM)

GameVideos = """
query GameVideos($id: ID, $name: String, $languages: [String!], $sort: VideoSort, $type: [BroadcastType!], $first: Int, $after: Cursor) { 
    game(id: $id, name: $name) { 
        videos(first: $first, after: $after, languages: $languages, types: $type, sort: $sort) { 
            edges { 
                cursor 
                node { _video_ } 
            } 
            pageInfo { 
                hasNextPage 
            } 
        } 
    } 
}
""".replace("_video_", _VIDEO)

GameClips = """
query GameClips($id: ID, $name: String, $languages: [Language!], $sort: ClipsPeriod, $first: Int, $after: Cursor) { 
    game(id: $id, name: $name) { 
        clips(first: $first, after: $after, criteria: { languages: $languages period: $sort } ) { 
            edges { 
                cursor 
                node { _clip_  } 
            } 
            pageInfo { 
                hasNextPage 
            } 
        } 
    } 
}
""".replace("_clip_", _CLIP)


USER_BADGES = """
query UserBadges($id: ID, $login: String, $quality: BadgeImageSize) { 
    user(id: $id, login: $login, lookupType: ALL) { 
        broadcastBadges { 
            _badge_
        } 
    } 
}
""".replace("_badge_", _BADGE)