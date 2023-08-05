from groupmeme.entities.member import Member, member_from_dict

class Group:
  def __init__(
    self, 
    id:str,
    name:str,
    type:str,
    description:str,
    image_url:str,
    creator_user_id:str,
    created_at:int,
    updated_at:int,
    members:list[Member],
    share_url: str,
    messages: any=None
  ):
    self.id = id
    self.name = name
    self.type = type
    self.description = description
    self.image_url = image_url
    self.creator_user_id = creator_user_id
    self.created_at = created_at
    self.updated_at = updated_at
    self.members = members
    self.share_url = share_url
    self.messages = messages
    
def group_from_dict(data):
  members = [member_from_dict(member) for member in data['members']]

  return Group(
    id=data['id'],
    name=data['name'],
    type=data['type'],
    description=data['description'],
    image_url=data['image_url'],
    creator_user_id=data['creator_user_id'],
    created_at=data['created_at'],
    updated_at=data['updated_at'],
    members=members,
    share_url=data['share_url'],
  )