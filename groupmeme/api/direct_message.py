import requests

from groupmeme.api.base import BaseInterface
from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.objects import Attachment
from groupmeme import config


class DirectMessage(BaseInterface):
  __attrs__ = [
    'id',
    'source_guid',
    'recipient_id',
    'user_id',
    'created_at',
    'name',
    'text',
    'favorited_by',
    'attachments',
    'avatar_url'
  ]
  
  
  def __init__(
    self,
    id:str,
    source_guid:str,
    recipient_id:str,
    user_id:str,
    created_at:int,
    name:str,
    text:str,
    favorited_by:list[str],
    attachments:list[Attachment],
    avatar_url:str|None=None
  ):
    """
    `DirectMessage` constructor.
    
    params:
    - `id (str)`: The ID of the direct message.
    - `source_guid (str)`: The guid of the direct message.
    - `recipient_id (str)`: The ID of the user who recieved the DM.
    - `user_id (str)`: The ID of the user that sent the message.
    - `created_at (int)`: The time (Unix time) that the DM was created.
    - `name (str)`: The name of the user that sent the DM.
    - `text (str)`: The text content of the message.
    - `favorited_by (str)`: A list of user IDs of users that liked the DM.
    - `attachments (list[Attachment])`: A list of attachments on the DM.
    - `avatar_url (str)` *optional*: URL to the profile picture of the user
    that sent the DM.
    """
    self.source_guid = source_guid
    self.recipient_id = recipient_id
    self.user_id = user_id
    self.created_at = created_at
    self.name = name
    self.text = text
    self.favorited_by = favorited_by
    self.attachments = attachments
    self.avatar_url = avatar_url
    
  
  @staticmethod  
  def from_dict(dm_dict):
    """
    Returns a `DirectMessage` object initialized using `dm_dict`.
    
    params:
    - `dm_dict(dict)`: Used to initialize the returned `DirectMessage` object.
    Must contain keys and values corresponding to the params in
    `DirectMessage.__init__`
    """
    return DirectMessage(**dm_dict)
  
  
  @staticmethod
  def _list(
    other_user_id:str,
    before_id:str=None,
    after_id:str=None
  ):
    """
    Returns a list (max length of 20) of direct messages between you and another
    user.
    
    params:
    - `other_user_id (str)`: The other user that has DMed you.
    - `before_id (str)` *optional*: Return DMs created before the DM with this ID.
    - `after_id (str)` *optional*: Return DMs created after the DM with this ID.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    body = { 'other_user_id': other_user_id }
    if before_id: body['before_id'] = before_id
    if after_id: body['after_id'] = after_id
    res = requests.get(
      f'{config.API_URL}',
      headers={ 'X-Access-Token': config.API_TOKEN },
      json=body
    )
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    dms_data = res.json()['response']['direct_messages']
    dms = []
    
    for dm_data in dms_data:
      attachments = []
      for attachment in dm_data['attachments']:
        attachments.append(Attachment.from_dict(attachment))
      dm_data['attachments'] = attachments
      dms.append(DirectMessage.from_dict(dm_data))
      
    return dms
      
  
  @staticmethod
  def _create(
    source_guid:str,
    recipient_id:str,
    text:str,
    attachments:list[Attachment]=None
  ):
    """
    Create a direct message and return the direct message as a `DirectMessage`
    object.
    
    params:
    - `source_guid (str)`: GUID of the direct message.
    - `recipient_id (str)`: ID of the recipient of the direct message.
    - `text (str)`: Text content of the direct message.
    - `attachments (list[Attachment])`: Attachments on the direct message.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    body = {
      'source_guid': source_guid,
      'recipient_id': recipient_id,
      'text': text
    }
    if attachments: body['attachments'] = [a.data for a in attachments]

    res = requests.post(
      f'{config.API_URL}',
      headers={ 'X-Access-Token': config.API_TOKEN },
      json=body
    )
    
    if res.status_code != 201:
      raise UnexpectedStatusCodeError(res.status_code, 201)
    
    dm_dict = res.json()['response']['message']
    dm_dict['attachments'] = [Attachment.from_dict(a) for a in dm_dict['attachments']]
    return DirectMessage.from_dict(dm_dict)
