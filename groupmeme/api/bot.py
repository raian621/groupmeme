import requests
import groupmeme.config as config
from groupmeme.api.errors import UnexpectedStatusCodeError, APIParameterError
from groupmeme.objects import Attachment

class Bot:
  __attrs__ = [
    'name',
    'group_id',
    'bot_id',
    'avatar_url',
    'callback_url',
  ]
  
  data = dict()
  
  
  def __init__(self, name:str, group_id:str, bot_id:str, avatar_url:str=None, callback_url:str=None):
    """
    `Bot` constructor.
    
    params:
    - `name (str)`: Name of the `Bot` (this is what the `Bot` appears as in 
    the `Group`)
    - `group_id (str)`: ID of the `Group` that the `Bot` is in 
    - `bot_id (str)`: ID of the `Bot`
    - `avatar_url (str)` *optional*: URL to the profile picture of the `Bot`
    - `callback_url (str)` *optional*: URL that messages received by the `Bot`
    will be sent to via an HTTP POST request
    """
    self.name = name
    self.group_id = group_id
    self.bot_id = bot_id
    self.avatar_url = avatar_url
    self.callback_url = callback_url


  def __setattr__(self, name, value):
    if name in self.__attrs__ and name != 'data':
      self.data[name] = value
    else:
      raise AttributeError(name=name)


  def __getattr__(self, name):
    if name in self.__attrs__ and name != 'data':
      return self.data[name]
    else:
      raise AttributeError(name=name)


  def from_dict(bot_dict:dict):
    """
    Returns a `Bot` object initialized using the `bot_dict` parameter
    
    `bot_dict` must contain the keys `name`, `group_id`, `bot_id`, and 
    optionally `avatar_url`, `callback_url`
    
    params:
    - `bot_dict (dict)`: Used to initialize the returned `Bot` object.
    """
    missing_keys = []
    for key in ('name', 'group_id', 'bot_id'):
      if key not in bot_dict:
        missing_keys.append(key)
    
    if len(missing_keys) > 0:
      raise KeyError(f'Missing required key(s): {missing_keys}')

    return Bot(
      name=bot_dict['name'],
      group_id=bot_dict['group_id'],
      bot_id=bot_dict['bot_id'],
      avatar_url=bot_dict.get('avatar_url', None),
      callback_url=bot_dict.get('callback_url', None)
    )


  @staticmethod
  def _create(name:str, group_id:str, avatar_url:str, callback_url:str):
    """
    Creates a `Bot` and returns a `Bot` object.
    
    params:
    - `name (str)`: Name of the `Bot`
    - `group_id (str)`: ID for the `Group` that the `Bot` will be added to
    - `avatar_url (str)`: URL for the profile picture of the `Bot`
    - `callback_url (str)` *optional*: URL that messages received by the 
    `Bot` will be sent to via an HTTP POST request
    """
    body = {
      'bot': {
        'name': name,
        'group_id': group_id
      }
    }
    if avatar_url: body['bot']['avatar_url'] = avatar_url
    if callback_url: body['bot']['callback_url'] = callback_url
    
    result = requests.post(
      url=f'{config.API_URL}/bots',
      headers={ 'X-Access-Token': config.API_TOKEN },
      json=body
    )
    if result.status_code != 201:
      raise UnexpectedStatusCodeError(result.status_code, 201)
    
    return Bot.from_dict(result.json()['response'])
  
  
  @staticmethod
  def _send_message(bot_id:str, text:str=None, attachments:list[Attachment]=None):
    """
    Sends a `Message` in the `Group` that the `Bot` is in. Returns the status 
    code of the `Message` creation request.
    
    params:
    - `bot_id (str)`: ID of the `Bot` you wish to send the `Message` as
    - `text (str)`: Text of the `Message` (max length is 1000 characters)
    - `attachments (list[Attachment])`: List of `Attachment`s for the `Message`
    
    raises:
    - `APIParameterError` 
    """
    body = { 'bot_id': bot_id }
    if text:
      if len(text) > 1000:
        raise APIParameterError(f'API parameter `text` exceeded max length of 1000 characters ({len(text)} characters)') 
      body['text'] = text
    if attachments: 
      body['attachments'] = [
        attachment.to_dict() for attachment in attachments
      ]
    
    print(body)
    result = requests.post(
      url=f'{config.API_URL}/bots/post',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    return result.status_code
  
  
  @staticmethod
  def _get_bots():
    """
    Returns a list of all the `Bot`s you have created but not deleted.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    result = requests.get(f'{config.API_URL}/bots', headers={ 'X-Access-Token': config.API_TOKEN })
    if result.status_code != 200:
      raise UnexpectedStatusCodeError(result.status_code, 200)
    
    bots_data = result.json()
    bots = []
    for bot_dict in bots_data['response']:
      bots.append(Bot.from_dict(bot_dict))
      
    return bots
  
  
  @staticmethod
  def _destroy(bot_id:str):
    """
    Destroys the `Bot` with ID `bot_id`. Returns the status code of the request to destroy the `Bot`.
    
    params:
    - `bot_id (str)`: ID of the `Bot` you intend to destroy
    """
    result = requests.post(f'{config.API_URL}/bots/destroy', headers={ 'X-Access-Token': config.API_TOKEN }, json={ 'bot_id': bot_id })
    
    return result.status_code


  def send_message(self, text:str=None, attachments:list[Attachment]=None):
    """
    Sends a `Message` in the `Group` that the `Bot` is in. Returns a `Message` object on success.
    
    params:
    - `text (str)`: Text of the `Message` (max length is 1000 character
    - `attachments (list[Attachment])`: List of `Attachment`s for the `Message`
    
    raises:
    - `APIParameterError` 
    """
    return Bot._send_message(self.bot_id, text, attachments)
  
  
  def destroy(self):
    """
    Destroys the `Bot`. Returns the status code of the request to destroy the `Bot`.
    
    raises:
    - `UnexpectedStatusCodeError` 
    """ 
    return Bot._destroy(self.id)
