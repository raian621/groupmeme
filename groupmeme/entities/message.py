from .attachment import Attachment

class Message:
  def __init__(
    self,
    _id:str,
    source_guid:str,
    created_at:int,
    user_id:str,
    group_id:str,
    name:str,
    avatar_url:str,
    text:str,
    system:bool,
    favorited_by:[str],
    attachments:[Attachment]=None
  ):
    self.id = _id
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
    
def message_from_dict(message_dict):
  return Message(
    _id=message_dict['id'],
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