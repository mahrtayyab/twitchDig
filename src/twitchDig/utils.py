import base64
import datetime
import random
import string
import sys
import uuid
from dateutil import parser as date_parser

def replace_between_indexes(original_string, from_index, to_index, replacement_text):
    new_string = original_string[:from_index] + replacement_text + original_string[to_index:]
    return new_string


def decodeBase64(encoded_string):
    return str(base64.b64decode(bytes(encoded_string, "utf-8")))[2:-1]


def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

def parse_wait_time(wait_time):
    if not wait_time:
        return 0

    if isinstance(wait_time, (tuple, list)):
        return random.randint(*[int(i) for i in wait_time[:2]])

    return int(wait_time)

def custom_json(self):
    try:
        return self.json()
    except:
        return {}


def create_request_id():
    return str(uuid.uuid1())


def get_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=int(length)))

def find_objects(obj, key, value, recursive=True, none_value=None):
    results = []

    def find_matching_objects(_obj, _key, _value):
        if isinstance(_obj, dict):
            if _key in _obj:
                found = False
                if _value is None:
                    found = True
                    results.append(_obj[_key])
                elif (isinstance(_value, list) and _obj[_key] in _value) or _obj[_key] == _value:
                    found = True
                    results.append(_obj)

                if not recursive and found:
                    return results[0]

            for sub_obj in _obj.values():
                find_matching_objects(sub_obj, _key, _value)
        elif isinstance(_obj, list):
            for item in _obj:
                find_matching_objects(item, _key, _value)

    find_matching_objects(obj, key, value)

    if len(results) == 1:
        return results[0]

    if len(results) == 0:
        return none_value

    return results

def parse_time(time):
    if not time:
        return None

    if isinstance(time, int) or str(time).isdigit():
        try:
            return datetime.datetime.fromtimestamp(int(time))
        except (OSError, ValueError):
            return datetime.datetime.fromtimestamp(int(time) / 1000)

    time = time.replace(" +0000 ", "")

    return date_parser.parse(time)


def parse_user_from_object(_input):
    if _input.__class__.__name__ == "User":
        _input = _input.id
    elif _input.__class__.__name__ == "Video":
        _input = _input.owner.id
    elif _input.__class__.__name__ == "Stream":
        _input = _input.user.id
    elif _input.__class__.__name__ == "Clip":
        _input = _input.user.id

    return _input

def parse_game_from_object(_input):
    if _input.__class__.__name__ == "Video":
        _input = _input.game.id
    elif _input.__class__.__name__ == "Game":
        _input = _input.id
    elif _input.__class__.__name__ == "Stream":
        _input = _input.game.id
    elif _input.__class__.__name__ == "Clip":
        _input = _input.game.id

    return _input

def split_and_make_dict(_string_, a=";", b="="):
    result = {}
    parts = _string_.split(a)
    for part in parts:
        try:
            parts2 = part.split(b)
            if len(parts2) == 2:
                result[parts2[0].strip()] = parts2[1].strip()
            else:
                result[parts2[0].strip()] = None
        except:
            pass
    return result
