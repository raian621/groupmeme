from .attachment import Attachment

class Message:
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
    favorited_by:[str],
    attachments:[Attachment]
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