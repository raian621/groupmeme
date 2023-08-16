import requests

from groupmeme.api import User
from groupmeme.api.base import BaseInterface
from groupmeme.objects import ChatMessage
from groupmeme import config
from groupmeme.api.errors import UnexpectedStatusCodeError
  

class Chat(BaseInterface):
  __attrs__ = [
    'created_at',
    'updated_at',
    'last_message',
    'messages_count',
    'other_user'
  ]

  
  def __init__(
    self,
    created_at:int,
    updated_at:int,
    last_message:ChatMessage,
    messages_count:int,
    other_user:User
  ):
    """
    `Chat` constructor
    
    params:
    - `created_at (int)`: Time (Unix time) the chat was created.
    - `updated_at (int)`: Time (Unix time) the chat was last updated.
    - `last_message (ChatMessage)`: The last message in the chat.
    - `messages_count (int)`: The number of messages in the chat.
    - `other_user (user)`: The other user in the chat.
    """
    self.created_at = created_at
    self.updated_at = updated_at
    self.last_message = last_message
    self.messages_count = messages_count
    self.other_user = other_user
    
  
  def from_dict(chat_dict) -> 'Chat':
    """
    Returns a `Chat` object initialized using `chat_dict`
    
    params:
    - `chat_dict (dict)`: Used to initialize returned `Chat` object. Must have
    keys and values corresponding to the params in `Chat.__init__`.
    
    example:
    ```py
    chat = Chat.from_dict({
      "created_at": 1352299338,
      "updated_at": 1352299338,
      "last_message": {
        "attachments": [
  
        ],
        "avatar_url": "https://i.groupme.com/200x200.jpeg.abcdef",
        "conversation_id": "12345+67890",
        "created_at": 1352299338,
        "favorited_by": [
  
        ],
        "id": "1234567890",
        "name": "John Doe",
        "recipient_id": "67890",
        "sender_id": "12345",
        "sender_type": "user",
        "source_guid": "GUID",
        "text": "Hello world",
        "user_id": "12345"
      },
      "messages_count": 10,
      "other_user": {
        "avatar_url": "https://i.groupme.com/200x200.jpeg.abcdef",
        "id": 12345,
        "name": "John Doe"
      }
    })
    ```
    """
    chat_dict['last_message'] = ChatMessage.from_dict(chat_dict['last_message'])
    other_user = chat_dict['other_user']
    other_user['image_url'] = other_user['avatar_url']
    del other_user['avatar_url']
    chat_dict['other_user'] = User.from_dict(other_user)
    return Chat(**chat_dict)
  
  
  def _chats(page:int=None, per_page:int=None) -> list['Chat']:
    """
    Returns a paginated list of `Chat` objects.
    
    params:
    - `page (int)`: Page of chat results.
    - `per_page (int)`: `Chat` objects per page.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    body = {}
    if page: body['page'] = page
    if per_page: body['per_page'] = per_page
    
    res = requests.get(
      f'{config.API_URL}/chats',
      headers={ 'X-Access-Token': config.API_TOKEN },
      json=body
    )
    
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    res_data = res.json()
    chats = [Chat.from_dict(result) for result in res_data['response']]
    
    return chats
