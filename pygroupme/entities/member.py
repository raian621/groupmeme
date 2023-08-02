class Member:
  def __init__(
    self,
    user_id,
    nickname,
    muted,
    image_url
  ):
    self.user_id = user_id
    self.nickname = nickname
    self.muted = muted
    self.image_url = image_url
    
def member_from_dict(member_dict):
  return Member(
    user_id=member_dict['user_id'],
    nickname=member_dict['nickname'],
    muted=member_dict['muted'],
    image_url=member_dict['image_url'],
  )