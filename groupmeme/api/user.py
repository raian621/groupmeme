import requests
from groupmeme import config
from groupmeme.api.errors import UnexpectedStatusCodeError

class User:
  __attrs__ = [
    'id',
    'phone_number',
    'image_url',
    'name',
    'created_at',
    'updated_at',
    'email',
    'sms',
    'avatar_url',
    'phone_number',
    'zip_code'
  ]
  
  data = dict()
  
  
  def __init__(
    self,
    id:str,
    image_url:str,
    name:str,
    created_at:int,
    updated_at:int,
    zip_code:str=None,
    avatar_url:str=None,
    phone_number:str=None,
    email:str=None,
    sms:bool=False
  ):
    self.id = id
    self.image_url = image_url
    self.name = name
    self.created_at = created_at
    self.updated_at = updated_at
    self.avatar_url = avatar_url
    self.zip_code = zip_code
    self.phone_number = phone_number
    self.email = email
    self.sms = sms
    
  
  def from_dict(user_dict):
    return User(**user_dict)
  
  
  def __setattr__(self, name, value):
    if name in self.__attrs__ and name != 'data':
      self.data[name] = value
    else:
      raise AttributeError(name=name)
    

  def __getattr__(self, name, value):
    if name in self.__attrs__ and name != 'data':
      return self.data[name]
    else:
      raise AttributeError(name=name)
    
    
  def _me() -> 'User':
    result = requests.get(f'{config.API_URL}/users/me', headers={ 'X-Access-Token': config.API_TOKEN })
    if result.status_code != 200:
      raise UnexpectedStatusCodeError(result.status_code, 200)
    
    user = User.from_dict(result.json()['response'])
    return user
  
  
  def _update_me(
    avatar_url:str=None,
    name:str=None,
    email:str=None,
    zip_code:str=None
  ) -> 'User':
    body = {}
    if avatar_url: body['avatar_url'] = avatar_url
    if name: body['name'] = name
    if email: body['email'] = email
    if zip_code: body['zip_code'] = zip_code
    
    if len(body.keys()) == 0:
      return None

    result = requests.post(
      f'{config.API_URL}/users/update',
      headers={ 'X-Access-Token': config.API_TOKEN },
      json=body
    )
    if result.status_code != 200:
      raise UnexpectedStatusCodeError(result.status_code, 200)

    return User(**(result.json()['response']))