import requests

from groupmeme.api.errors import UnexpectedStatusCodeError, APIParameterError
from groupmeme.api.base import BaseInterface
from groupmeme.objects import Attachment
from groupmeme import config


class Message(BaseInterface):
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
    """
    `Message` constructor
    
    params:
    - `id (str)`: The ID of the `Message`.
    - `source_guid (str)`: The guid of the `Message`. Can be used as a client-side
    ID for the message. The server scans the `source_guid` of each `Message` for
    duplication; If two messages are sent with the same `source_guid` within one
    minute, the second message will fail to send and yield a 409 Conflict HTTP 
    response code.
    - `created_at (int)`: The time (UNIX time) that the `Message` was created at.
    - `user_id (str)`: The id of the `User` that sent the `Message`.
    - `group_id (str)`: The `Group` that the message was sent in.
    - `name (str)`: The name of the sender of the message.
    - `avatar_url (str)`: URL to the profile picture of the `User` that sent the 
    message. The URL will always be what the senders profile picture URL was when
    they sent the message.
    - `text (str)`: The text content of the message.
    - `system (bool)`: Whether the message was sent by the system.
    - `favorited_by (list[str])`: A list of the user ids of `User`s that liked the
    message
    - `attachments (list[Attachment])`: A list of attachments on the message.
    """
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

  
  def from_dict(message_dict) -> 'Message':
    """
    Returns a `Message` object initialized using the `message_dict` parameter.
    
    params:
    - `message_dict (dict)`: Used to initialize the returned `Message` object.
    Must contain keys and values corresponding to the parameters in 
    `Message.__init__`.
    
    example:
    
    ```py
    message = Message.from_dict({
      "id": "<id>",
      "source_guid": "<source_guid>",
      "created_at": 123456789,
      "user_id": "<user_id>",
      "group_id": "<group_id>",
      "name": "<name>",
      "avatar_url": "<avatar_url>",
      "text": "<text>",
      "system": False,
      "favorited_by": ["123", "1234"],
      "attachments": [Attachment(type="image", url="<image_url>")],
    })
    ```
    """
    attachments = []
    for attachment in attachments:
      attachments.append(Attachment.from_dict(attachment))
    
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
      attachments=attachments
    )
  
  
  def _messages(
    group_id:str,
    before_id:int|None = None,
    since_id:int|None = None,
    after_id:int|None = None,
    limit:int|None = None
  ) -> list['Message']:
    """
    Returns a list of messages for a given time period in a `Group`.
    
    params:
    - `group_id (str)`: The ID of the group you want to retrieve messages from.
    - `before_id (str)`: Get messages created before the message with ID 
    `before_id`
    - `after_id (str)`: Get messages created immediately after the message with
    ID `after_id`.
    - `since_id (str)`: Get the most recent messages created since the message
    with ID `since_id`.
    - `limit (int)`: Limit the number of messages returned (default=20, max=100).
    
    raises:
    - `UnexpectedStatusCodeError`
    - `APIParameterError`
    """
    body = {}
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    if before_id: body['before_id'] = before_id
    if since_id: body['since_id'] = since_id
    if after_id: body['after_id'] = after_id
    if limit:
      if limit > 100:
        raise APIParameterError(f'API parameter `limit` must be less than or equal to 100.') 
      body['limit'] = limit
    
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
    source_guid:str,
    attachments:list['Attachment']=None,
  ) -> 'Message':
    """
    Posts a message to the group given by `group_id`.
    
    params:
    - `group_id (str)`: ID of the group to post the message to
    - `text (str)`: Text content of the message
    - `source_guid (str)`: The guid of the `Message`. Can be used as client-side
    IDs for messages. The server scans the `source_guid` of each `Message` for
    duplication; If two messages are sent with the same `source_guid` within one
    minute the second message will fail to send, yielding a 409 Conflict HTTP 
    response code.
    - `attachments (list[Attachment])`: Attachments on the message to be posted
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    body = { 'message': { 'text': text }}
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    if attachments: body['message']['attachments'] = [ 
      attachment.to_dict() for attachment in attachments
    ]
    body['source_guid'] = source_guid
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/messages', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    message_data = res.json()['response']
    return Message.from_dict(message_data)
      
    