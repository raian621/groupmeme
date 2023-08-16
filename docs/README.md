# GroupMeme

Simple Python library for interfacing with the GroupMe API.

I plan to add support for bot commands when I finish implementing the basic GroupMe API routes.

## Features

### Bots
Create GroupMe bots and send messages from your bots to group chats.

### Member management
Add and remove members from your GroupMe groups.

### Group management
Create and disband GroupMe groups.

### Messages
Send messages to a group using GroupMeme.

### Attachments
Attach pictures, locations, events, and emojis to your messages and your bot's messages.

### User Settings
Change your name, email, zip code, and profile picture.


## Prerequisites

In order to use the GroupMe API, you must have:
- A GroupMe account: [Sign up for GroupMe](https://web.groupme.com/signup)
- A GroupMe API token: [GroupMe developer site](https://dev.groupme.com/)
  - Log in with your GroupMe account credentials
  - Click on 'Access Token' in the top right corner of the site to see your API token
  - Save your API token somewhere safe and **do not share your API token with anyone**
- Python >=3.10 and pip installed on your system

## Installation

This library is still in development so it's only available on test.pypi.org

```sh
pip install -i https://test.pypi.org/simple/ groupmeme
```

## Example Code

```py
from groupmeme.api import init_groupmeme, Group, Message

# load data needed to send authenticated requests to GroupMe API:
init_groupmeme(
  api_url='https://api.groupme.com/v3/',
  api_token='<GROUPME_API_TOKEN>'
)

# create a group:
group = Group._create(
  name='The Meme Team',
  description='Dankest memes in the west',
  image_url='https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ'
)

# send message to the newly created group:
Message._create(
  group_id=group.id,
  text='Hello World'
)
```