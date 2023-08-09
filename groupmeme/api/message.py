import requests
from random import randint

from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme import config


class Message:
  __attrs__ = [
    'id',
    'source_guid',
    'created_at',
    'user_id',
    'group_id',
    'name',
    'avatar_url',
    'text',
    'system',
    'favorited_by',
    'attachments'
  ]
  
  data = dict()
  
  
  def __init__(
    self,
    id:str,
    source_guid:str,
    created_at:int,
    user_id:str,
    group_id:str,
    name:str,
    avatar_url:str,
    text:str,
    system:bool,
    favorited_by:list[str],
    attachments:list['Attachment']=None
  ):
    self.id = id
    self.source_guid = source_guid
    self.created_at = created_at
    self.user_id = user_id
    self.group_id = group_id
    self.name = name
    self.avatar_url = avatar_url
    self.text = text
    self.system = system
    self.favorited_by = favorited_by
    self.attachments = attachments
    
    
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
  
  
  def from_dict(message_dict) -> 'Message':
    return Message(
      id=message_dict['id'],
      source_guid=message_dict['source_guid'] if 'source_guid' in message_dict else '',
      created_at=message_dict['created_at'],
      user_id=message_dict['user_id'],
      group_id=message_dict['group_id'],
      name=message_dict['name'],
      avatar_url=message_dict['avatar_url'],
      text=message_dict['text'],
      system=message_dict['system'],
      favorited_by=message_dict['favorited_by'],
      attachments=message_dict['attachments'] if 'attachments' in message_dict else None
    )
  
  
  def _messages(
    group_id:str,
    before_id:int|None = None,
    since_id:int|None = None,
    after_id:int|None = None,
    limit:int|None = None
  ) -> list['Message']:
    body = {}
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    if before_id: body['before_id'] = before_id
    if since_id: body['since_id'] = since_id
    if after_id: body['after_id'] = after_id
    if limit: body['limit'] = limit
    
    res = requests.get(f'{config.API_URL}/groups/{group_id}/messages', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    messages_data = res.json()['response']
    count = messages_data['count']
    messages = [Message.from_dict(message) for message in messages_data['messages']]
    return messages, count


  def _create(
    group_id:str,
    text:str,
    attachments:list['Attachment']=None
  ):
    body = { 'message': { 'text': text }}
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    if attachments: body['message']['attachments'] = [ dict(attachment) for attachment in attachments]
    body['source_guid'] = str(randint(0, 1000))
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/messages', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    message_data = res.json()['response']
    return Message.from_dict(message_data)
      
    