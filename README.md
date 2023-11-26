# twitchDig
Fun Project to Scrape Twitch

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Internet Connection
* Python 3.6+
* httpx 
* websocket

## Installation: 
```bash
pip install twitchDig
```

## Keep synced with latest fixes

##### **Pip might not be always updated , so to keep everything synced.**

```bash
pip install https://github.com/mahrtayyab/twitchDig/archive/main.zip --upgrade 
```

## A Quick Example:
```python
from twitchDig.bot import Bot

app = Bot()

user = app.get_user("kharltayyab")
print(user)
```

Full Documentation and Changelogs are [here](https://mahrtayyab.github.io/twitchDig_docs/)
