class _Filter(type):

    def __iter__(self):
        for value in vars(self).values():
            if isinstance(value, str) and str(value).isupper():
                yield value

class Languages(metaclass=_Filter):
    ARABIC = "AR"
    AMERICAN_SIGN_LANGUAGE = "ASL"
    BULGARIAN = "BG"
    CATALAN = "CA"
    CZECH = "CS"
    DANISH = "DA"
    GERMAN = "DE"
    GREEK = "EL"
    ENGLISH = "EN"
    SPANISH = "ES"
    FINNISH = "FI"
    FRENCH = "FR"
    HINDI = "HI"
    HUNGARIAN = "HU"
    INDONESIAN = "ID"
    ITALIAN = "IT"
    JAPANESE = "JA"
    KOREAN = "KO"
    MALAY = "MS"
    DUTCH = "NL"
    NORWEGIAN = "NO"
    OTHER = "OTHER"
    POLISH = "PL"
    PORTUGUESE = "PT"
    ROMANIAN = "RO"
    RUSSIAN = "RU"
    SLOVAK = "SK"
    SWEDISH = "SV"
    THAI = "TH"
    TAGALOG = "TL"
    TURKISH = "TR"
    UKRAINIAN = "UK"
    VIETNAMESE = "VI"
    CHINESE_MANDARIN = "ZH"
    CHINESE_CANTONESE_HK = "ZH_HK"

class SearchFilters(metaclass=_Filter):
    GAMES = "SearchGames"
    CHANNELS = USERS = "SearchChannels"
    VIDEOS = "SearchVideos"
    STREAMS = "SearchStreams"

class UserVideosFilters(metaclass=_Filter):
    VIEWS = DEFAULT = "VIEWS"
    TIME = UPLOAD_DATE = "TIME"

class UserClipsFilters(metaclass=_Filter):
    LAST_WEEK = THIS_WEEK = "LAST_WEEK"
    LAST_DAY = TODAY = "LAST_DAY"
    LAST_MONTH = THIS_MONTH = "LAST_MONTH"
    ALL_TIME = ALL = DEFAULT = "ALL_TIME"

class GameStreamsFilters(metaclass=_Filter):
    VIEWER_COUNT = DEFAULT = "VIEWER_COUNT"
    VIEWER_COUNT_ASC = "VIEWER_COUNT_ASC"


GameVideosFilters = UserVideosFilters
GameClipsFilters = UserClipsFilters

