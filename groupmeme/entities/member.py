class Member:
  def __init__(
    self,
    user_id:str,
    nickname:str,
    muted:str,
    image_url:str,
    autokicked:bool,
    member_id:str|None = None,
  ):
    self.member_id = member_id
    self.user_id = user_id
    self.nickname = nickname
    self.muted = muted
    self.image_url = image_url
    self.autokicked = autokicked


def member_from_dict(member_dict):
  return Member(
    member_id=member_dict['id'] if 'id' in member_dict else None,
    user_id=member_dict['user_id'],
    nickname=member_dict['nickname'],
    muted=member_dict['muted'],
    image_url=member_dict['image_url'],
    autokicked=member_dict['autokicked'] if 'autokicked' in member_dict else None,
  )