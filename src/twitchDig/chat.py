import re
import traceback
import websocket
from .types.twitch_types import ChatRoomState, ChatMessage

UN_AUTHENTICATED_INITIAL_WS_MESSAGES = [
    "CAP REQ :twitch.tv/tags twitch.tv/commands",
    "PASS {token}",
    "NICK {nick}",
    "USER {nick} 8 * :{nick}",
]

AUTHENTICATED_INITIAL_WS_MESSAGES = [
    "CAP REQ :twitch.tv/tags twitch.tv/commands",
    "PASS oauth:{token}",
    "NICK {nick}"
]

JOIN_WS_MESSAGE = "JOIN #{username}"


class ChatRoom:
    URL = "wss://irc-ws.chat.twitch.tv/"
    TOKEN = "SCHMOOPIIE"
    WELCOME_MESSAGE_REGEX = re.compile(r":tmi\.twitch\.tv 001 (.*?) :Welcome,")
    HOST_MESSAGE_REGEX = re.compile(r"Your host is (.*?)\n")

    def __init__(self, client, channel_name, on_message_callback=None, auto_reconnect=True):
        self.room_state = None
        self.host = "tmi.twitch.tv"
        self.client = client
        self._on_message_callback = on_message_callback
        self._auto_reconnect = auto_reconnect

        if not self.client.me:
            self._nickname = self._get_nickname()

        self.channel_name = channel_name
        self.ws = self._create_connection()

    def run_forever(self):
        self.ws.run_forever()

    @staticmethod
    def _get_nickname():
        return "justinfan51081"

    def _get_initial_socket_messages(self):
        if self.client.me:
            nick = self.client.me.username
            token = self.client.auth_token
            messages = AUTHENTICATED_INITIAL_WS_MESSAGES
        else:
            nick = self._nickname
            token = self.TOKEN
            messages = UN_AUTHENTICATED_INITIAL_WS_MESSAGES
        return [i.format(nick=nick, token=token) for i in messages]

    def _create_connection(self):
        ws = websocket.WebSocketApp(
            url=self.URL,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        return ws

    def _on_open(self, socket):
        messages = self._get_initial_socket_messages()
        for message in messages:
            socket.send(message)

    def _on_message(self, socket, _message):
        message = _message.strip().replace("\n", " ")
        try:
            message = str(message)
            if re.match(self.WELCOME_MESSAGE_REGEX, message):
                try:
                    self.host = re.findall(self.HOST_MESSAGE_REGEX, message)[0]
                except:
                    pass
                socket.send(JOIN_WS_MESSAGE.format(username=self.channel_name))
            elif message.startswith("PING"):
                socket.send(f"PONG :{self.host}")
            else:
                irc_message = IRC_Parser(self, message).parse()
                if isinstance(irc_message, ChatRoomState):
                    self.room_state = irc_message
                elif isinstance(irc_message, ChatMessage):
                    if self._on_message_callback:
                        self._on_message_callback(irc_message)
        except:
            traceback.print_exc()

    def _on_error(self, socket, error):
        if self._auto_reconnect:
            self._create_connection()

    def _on_close(self, socket):
        if self._auto_reconnect:
            self._create_connection()


class IRC_Parser:
    SYSTEM_MESSAGES = re.compile(r'^:(?P<sender>\S+) (?P<command>\S+)(?: (?P<params>.+))?')
    CHAT_MESSAGES = re.compile(r'([a-zA-Z0-9_-]+)\s*=\s*([^;]*)(?:;|:)')

    def __init__(self, chatroom, message):
        self._message = message
        self._chatroom = chatroom

    def parse(self):
        if str(self._message).__contains__("ROOMSTATE"):
            return ChatRoomState(self._chatroom, self._message)
        elif str(self._message).__contains__("PRIVMSG"):
            return ChatMessage(self._chatroom, self._message)
        return None
