from groupmeme.api.base import BaseInterface

class ChatMessage(BaseInterface):
  __attrs__ = [
    'id',
    'name',
    'conversation_id',
    'created_at',
    'recipient_id',
    'sender_id',
    'sender_type',
    'source_guid',
    'text',
    'attachments',
    'favorited_by',
    'user_id',
    'avatar_url'
  ]
  
  
  def __init__(
    self,
    id:str,
    conversation_id:str,
    created_at:int,
    name:str,
    recipient_id:str,
    sender_id:str,
    sender_type:str,
    source_guid:str,
    text:str,
    attachments:list['Attachment'],
    favorited_by:list['str'],
    user_id:str,
    avatar_url:str|None=None
  ):
    """
    `ChatMessage` constructor.
    
    params:
    - `id (str)`: The ID of the chat.
    - `name (str)`: The name of the user that sent the message.
    - `conversation_id (str)`: The ID of the conversation / chat.
    - `created_at (int)`: The time (Unix time) that the message was created.
    - `recipient_id (str)`: The ID of the user that received the message.
    - `sender_id (str)`: The ID of the user that sent the message.
    - `sender_type (str)`: The type of sender that sent the message (ex. "user", "system).
    - `source_guid (str)`: The `source_guid` of the message.
    - `attachments (list[Attachment])`: Attachments on the message.
    - `favorited_by (list[str])`: List of user IDs of users that liked the message.
    - `user_id (str)`: The ID of the user requesting ChatMessage info(?).
    - `avatar_url (str|None)`: The URL to the profile picture of the user that
    sent the message.
    """
    self.id = id
    self.name = name
    self.conversation_id = conversation_id
    self.created_at = created_at
    self.recipient_id = recipient_id
    self.sender_id = sender_id
    self.sender_type = sender_type
    self.source_guid = source_guid
    self.text = text
    self.attachments = attachments
    self.favorited_by = favorited_by
    self.user_id = user_id
    self.avatar_url = avatar_url
    
    
  def from_dict(chat_message_dict):
    """
    Returns a `ChatMessage` object initialized using `chat_message_dict`.
    
    params:
    - `chat_message_dict (dict)`: Dictionary used to initialize the returned
    `ChatMessage`, must have keys and values corresponding to the params in
    `ChatMessage.__init__`
    """
    return ChatMessage(**chat_message_dict)