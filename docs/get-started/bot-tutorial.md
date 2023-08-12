# Bot Tutorial
Adapted from GroupMe's [offical bots tutorial](https://dev.groupme.com/tutorials/bots).

## Prerequisites
- [Create a GroupMe account and obtain your API key](/get-started/quickstart#prerequisites)
- Have `python >= 3.10` and `pip` installed on your system
- [Have `groupmeme` installed on your system](/get-started/quickstart#installation)

## Initialize GroupMeme with API token and API url
```python
from groupmeme import init_groupmeme
from groupmeme.api import Group, Bot

init_groupmeme(
  api_url='https://api.groupme.com/v1/', # default
  api_token='API_TOKEN'
)
```

## Create a testing group
```python
test_group = Group._create(
  name='Testing Group'
)
```

## Create and Register your bot
```python
test_bot = Bot._create('Test Bot', test_group.id)
```
## Make your bot do something
```python
test_bot.send_message('Hello World!')
```

## Final code: <!-- {docsify-ignore} -->
```python
from groupmeme import init_groupmeme
from groupmeme.api import Group, Bot

init_groupmeme(
  api_url='https://api.groupme.com/v1/', # default
  api_token='API_TOKEN'
)

# create a group called 'Test Group'
test_group = Group._create('Test Group')

# create a bot called 'Test Bot'
test_bot = Bot._create('Test Bot', test_group.id)

# send a message from 'Test Bot' in the 'Test Group' chat
test_bot.send_message('Hello World!')
```