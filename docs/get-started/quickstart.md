# Quickstart

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