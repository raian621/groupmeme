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
    name:str,
    created_at:int,
    updated_at:int,
    image_url:str=None,
    zip_code:str=None,
    phone_number:str=None,
    email:str=None,
    sms:bool=False
  ):
    """
    Constructor for `User`.
    
    params:
    - `id (str)`: User ID of the user.
    - `name (str)`: Name of the user.
    - `created_at (int)`: Time (Unix time) that the user was created.
    - `updated_at (int)`: Time (Unix time) that the user was last updated.
    - `image_url (str)` *optional*: URL to the user's profile picture.
    - `zip_code (str)` *optional*: Zip code of the user.
    - `phone_number (str)` *optional*: Phone number of the user.
    - `email (str)` *optional*: Email of the user.
    - `sms (bool) *optional*?`: If the user is using SMS mode for GroupMe
    """
    self.id = id
    self.image_url = image_url
    self.name = name
    self.created_at = created_at
    self.updated_at = updated_at
    self.zip_code = zip_code
    self.phone_number = phone_number
    self.email = email
    self.sms = sms
    
  
  def from_dict(user_dict) -> 'User':
    """
    Returns a `User` object initialized using the `user_dict` parameter.
    
    params:
    - `user_dict (dict)`: Used to initialize the returned 'User` object.
    Must contain keys and values corresponding to the parameters in `User.__init__`
    """
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
    """
    Return a `User` object containing information from your account
    
    raises:
    - UnexpectedStatusCodeError
    """
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
    """
    Update your user information.
    
    params:
    - `avatar_url (str) *optional*`: URL to your new profile picture.
    - `name (str)` *optional*: New name for your profile.
    - `email (str)` *optional*: New email for your profile.
    - `zip_code (str)` *optional*: New zip code for your profile.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
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