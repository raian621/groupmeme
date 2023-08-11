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
    body = {
      'bot': {
        'name': name,
        'group_id': group_id
      }
    }
    if avatar_url: body['avatar_url'] = avatar_url
    if callback_url: body['callback_url'] = callback_url
    
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
    body = { 'bot_id': bot_id }
    if text:
      if len(text) > 1000:
        raise APIParameterError(f'API parameter `text` exceeded max length of 1000 characters ({len(text)} characters)') 
      body['text'] = text
    if attachments: 
      body['attachments'] = [
        attachment.__dict__() for attachment in attachments
      ]
    
    print(body)
    result = requests.post(
      url=f'{config.API_URL}/bots/post',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    return result.status_code
  
  
  def send_message(self, text:str=None, attachments:list[Attachment]=None):
    return Bot._send_message(self.bot_id, text, attachments)
  
  
  @staticmethod
  def _get_bots():
    result = requests.get(f'{config.API_URL}/bots', headers={ 'X-Access-Token': config.API_TOKEN })
    if result.status_code != 200:
      raise UnexpectedStatusCodeError(result.status_code, 200)
    
    bots_data = result.json()
    bots = []
    for bot_dict in bots_data['response']:
      bots.append(Bot.from_dict(bot_dict))
      
    return bots
  
  
  @staticmethod
  def _destroy_bot(bot_id:str):
    result = requests.post(f'{config.API_URL}/bots/destroy', headers={ 'X-Access-Token': config.API_TOKEN }, json={ 'bot_id': bot_id })
    
    return result.status_code
  
  
bot = Bot(name='', group_id='', bot_id='')