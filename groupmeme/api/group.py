from groupmeme.api.member import Member
import groupmeme.config as config
from groupmeme.api.errors import UnexpectedStatusCodeError

import requests


class Group:
  __attrs__ = [
    'id',
    'name',
    'type',
    'description',
    'image_url',
    'creator_user_id',
    'created_at',
    'updated_at',
    'members',
    'share_url',
    'messages'
  ]
  
  data = dict()
  
  
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
    messages: list['Message']=None
  ):
    """
    `Group` constructor

    params:
    - `id (str)`: ID of the Group.
    - `name (str)`: The name of the Group
    - `type (str)`: The type of Group (`'public'` or `'private'`)
    - `description (str)`: The description of the Group
    - `image_url (str)`: URL for the Group's profile image
    - `members (list[Member])`: Members of the Group
    - `created_at (str)`: The time (Unix time) that the Group was created
    - `updated_at (str)`: The time (Unix time) that the Group was last updated
    - `creator_user_id (str)`: ID of the creator of the Group
    - `share_url (str)`: URL that can be used to join the Group
    - `messages (list[Message])`: Messages in the Group
    """
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
    
  
  def __setattr__(self, name, value):
    if name in self.__attrs__ and name != 'data':
      self.data[name] = value
    else:
      raise AttributeError(name=name)
    
  
  def __getattr__(self, name):
    if name in self.__attrs__ and name != 'data':
      return self.data[name]
    else:
      raise AttributeError(name=name)
  
  
  @staticmethod
  def from_dict(group_dict:dict):
    """
    Returns a `Group` object initialized using a `dict`.

    The dict must contain keys corresponding to the parameters in the `Group` 
    constructor (`id`, `name`, `type`, `description`, `image_url`, `members`, 
    `created_at`, `updated_at`, `creator_user_id`, `share_url`, `messages`)

    params:
    - `group_dict (dict)`: `dict` used to initialize the Group
    """
    members = [Member.from_dict(member) for member in group_dict['members']]

    return Group(
      id=group_dict['id'],
      name=group_dict['name'],
      type=group_dict['type'],
      description=group_dict['description'],
      image_url=group_dict['image_url'],
      creator_user_id=group_dict['creator_user_id'],
      created_at=group_dict['created_at'],
      updated_at=group_dict['updated_at'],
      members=members,
      share_url=group_dict['share_url'],
    )
    
  
  @staticmethod
  def _groups(
    page: int|None = None,
    per_page: int|None = None,
    omit: str|None = None
  ) -> list['Group']:
    """
    Returns a paginated list of `Group` objects that the user is a part of

    params:
    - `page (int)`: Page of results, defaults to `1`
    - `per_page (int)`: `Group` results per page, defaults to `10`
    - `omit (str)`: Comma seperated list of fields to omit from each 
    `Group` result. The only currently supported value is just 
    `"memberships"` which results in the `members` field being empty

    raises:
    - `UnexpectedStatusCodeError`
    """
    req_params = {}
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    if page: req_params['page'] = page
    if per_page: req_params['per_page'] = per_page
    if omit: req_params['omit'] = omit
    
    res = requests.get(f'{config.API_URL}/groups', params=req_params, headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    groups_data = res.json()
    groups = []

    for data in groups_data['response']:    
      groups.append(Group.from_dict(data))
    
    return groups
  
  
  @staticmethod
  def _former_groups() -> list['Group']:
    """
    Returns a list of all the `Group`s that the user has previously left

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
  
    res = requests.get(f'{config.API_URL}/groups/former', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    groups_data = res.json()
    groups = []

    for data in groups_data['response']:    
      groups.append(Group.from_dict(data))
    
    return groups
  
  
  @staticmethod
  def _get(
    group_id: str
  ) -> 'Group':
    """
    Returns a `Group` matching the supplied `group_id`

    params:
    - `group_id (str)`: ID of a group

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
  
    res = requests.get(f'{config.API_URL}/group/{group_id}', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    if res.status_code == 404:
      raise ValueError
    group_data = res.json()
    group = Group.from_dict(group_data['response'])
    
    return group
  
  
  @staticmethod
  def _create(
    name:str,
    description:str|None = None,
    image_url:str|None = None,
    share:bool|None = None
  ) -> 'Group':
    """
    Creates a GroupMe `Group`

    params:
    - `name (str)`: The name of the `Group`
    - `description (str)` *optional*:  Description of the `Group`
    - `image_url (str)` *optional*: URL of the `Group`'s profile image
    - `share (bool)`: *optional*: If `True` a share URL will be generated for the `Group`, if `False` a share URL will not be generated for the `Group`. Defaults to `False`
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    body = { 'name': name }

    if description: body['description'] = description
    if image_url: body['image_url'] = image_url
    if share: body['share'] = share

    res = requests.post(f'{config.API_URL}/groups', headers=headers, json=body)
    if res.status_code != 201:
      raise UnexpectedStatusCodeError(res.status_code, 201)

    group_data = res.json()
    group = Group.from_dict(group_data['response'])

    return group
  
  
  @staticmethod
  def _update(
    group_id:str,
    name:str|None = None,
    description:str|None = None,
    image_url:str|None = None,
    office_mode:bool|None = None,
    share:bool|None = None
  ) -> 'Group':
    """
    Updates the information for a `Group`

    Only the group's creator has authority to update the group.

    params:
    - `group_id (str)`: ID of the `Group` you wish to update the 
    information of
    - `name (str)` *optional*: The new name of the `Group`
    - `description (str)` *optional*: The new description of the `Group`
    - `image_url (str)` *optional*: The new URL of the profile picture of
    the `Group`
    - `office_mode (bool)` *optional*: The new value of `office_mode` for
    the `Group`, if `office_mode` is `False` notifications from this group won't buzz your phone
    - `share (bool)` *optional*: The new value of `share` for the `Group`,
    if `True` then a share URL will be generated that can be used to join the `Group`

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    body = {}
    
    if name: body['name'] = name
    if description: body['description'] = description
    if image_url: body['image_url'] = image_url
    if office_mode: body['office_mode'] = office_mode
    if share: body['share'] = name
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/update', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    group_data = res.json()
    group = Group.from_dict(group_data['response'])
    
    return group
  
  
  @staticmethod
  def _destroy(group_id:str) -> int:
    """
    Destroy a `Group`

    Only the group's creator has authority to destroy the group

    params:
    - `group_id (str)`: The ID of the `Group` to delete

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    res = requests.post(f'{config.API_URL}/groups/{group_id}/destroy', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    return res.status_code
  
  
  @staticmethod
  def _join(
    group_id:str,
    share_token:str
  ):
    """
    Join a `Group`.

    params:
    - `group_id (str)`: ID of the `Group` you wish to join
    - `share_token (str)`: Share token of the `Group` you wish to join

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/join/{share_token}', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    group_data = res.json()
    group = Group.from_dict(group_data['response'])
    
    return group


  @staticmethod
  def _rejoin(
    group_id:str,
    share_token:str
  ):
    """
    Rejoin a `Group`.

    You have to have previously left (not banned or kicked) in order to rejoin a group.

    params:
    - `group_id (str)`: ID of the `Group` you wish to join
    - `share_token (str)`: Share token of the `Group` you wish to join

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/join/{share_token}', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    group_data = res.json()
    group = Group.from_dict(group_data['response'])
    
    return group

  @staticmethod
  def _change_ownership(
    group_id:str,
    owner_id:str
  ):
    """
    Change ownership of the `Group` to another user.

    Only the owner of the group has the authorization to change the 
    ownership of the group.

    params:
    - `group_id (str)`: ID of the `Group` you wish to change the owner of
    - `owner_id (str)`: ID of the user you wish to transfer ownership to

    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    body = {
      'requests': [{
        'group_id': group_id,
        'owner_id': owner_id
      }]
    }
    
    res = requests.post(f'{config.API_URL}/groups/change_owners', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    change_result = res.json()
    return change_result['response']
  
  
  def update(
    self,
    name:str|None = None,
    description:str|None = None,
    image_url:str|None = None,
    office_mode:bool|None = None,
    share:bool|None = None
  ) -> 'Group':
    """
    Updates the information for a `Group`

    Only the group's creator has authority to update the group.

    params:
    - `name (str)` *optional*: The new name of the `Group`
    - `description (str)` *optional*: The new description of the `Group`
    - `image_url (str)` *optional*: The new URL of the profile picture of
    the `Group`
    - `office_mode (bool)` *optional*: The new value of `office_mode` for
    the `Group`, if `office_mode` is `False` notifications from this group won't buzz your phone
    - `share (bool)` *optional*: The new value of `share` for the `Group`,
    if `True` then a share URL will be generated that can be used to join the `Group`

    raises:
    - `UnexpectedStatusCodeError`
    """
    return Group._update(self, name, description, image_url, office_mode, share)
  
  
  def destroy(self) -> int:
    """
    Destroy a `Group`

    Only the group's creator has authority to destroy the group

    raises:
    - `UnexpectedStatusCodeError`
    """
    return Group._destroy(self.id)


  def rejoin(self, share_token:str):
    """
    Rejoin a `Group`.

    You have to have previously left (not banned or kicked) in order to
    rejoin a group.

    params:
    - `share_token (str)`: Share token of the `Group` you wish to join

    raises:
    - `UnexpectedStatusCodeError`
    """
    return Group._rejoin(self.id, share_token)


  def change_ownership(self, owner_id:str):
    """
    Change ownership of the `Group` to another user.

    Only the owner of the group has the authorization to change the 
    ownership of the group.

    params:
    - `owner_id (str)`: ID of the user you wish to transfer ownership to

    raises:
    - `UnexpectedStatusCodeError`
    """
    return Group._change_ownership(self.id, owner_id)