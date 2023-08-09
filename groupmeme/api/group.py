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
  def _create(name:str,
    description:str|None = None,
    image_url:str|None = None,
    share:bool|None = None
  ) -> 'Group':
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
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/join/{share_token}', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    group_data = res.json()
    group = Group.from_dict(group_data['response'])
    
    return group


  def _change_ownership(
    group_id:str,
    owner_id:str
  ):
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