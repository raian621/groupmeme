import requests
from groupmeme.config import API_URL, API_TOKEN
from groupmeme.api.errors import UnexpectedStatusCodeError, APIParameterError
from groupmeme.entities import Attachment

class Bot:
  def __init__(self, name:str, group_id:str, bot_id:str, avatar_url:str=None, callback_url:str=None):
    self.name = name
    self.group_id = group_id
    self.bot_id = bot_id
    self.avatar_url = avatar_url
    self.callback_url = callback_url


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
      'name': name,
      'group_id': group_id
    }
    if avatar_url: body['avatar_url'] = avatar_url
    if callback_url: body['callback_url'] = callback_url
    
    result = requests.post(
      url=f'{API_URL}/bots',
      headers={ 'X-Access-Token': API_TOKEN },
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
        raise APIParameterError('text', 1000, len(text)) 
      body['text'] = text
    if attachments: 
      body['attachments'] = [
        attachment.__dict__() for attachment in attachments
      ]
    
    result = requests.post(
      url=f'{API_URL}/bots/post',
      headers={ 'X-Access-Token': API_TOKEN },
    )
    
    return result.status_code
  
  
  def send_message(self, text:str=None, attachments:list[Attachment]=None):
    return Bot._send_message(self.bot_id, text, attachments)
  
  
  @staticmethod
  def _get_bots():
    result = requests.get(f'{API_URL}/bots', headers={ 'X-Access-Token': API_TOKEN })
    if result.status_code != 200:
      raise UnexpectedStatusCodeError(result.status_code, 200)
    
    bots_data = result.json()
    bots = []
    for bot_dict in bots_data['response']:
      bots.append(Bot.from_dict(bot_dict))
      
    return bots
  
  
  @staticmethod
  def _destroy_bot():
    result = requests.post(f'{API_URL}/bots/destroy', headers={ 'X-Access-Token': API_TOKEN })
    
    return result.status_code