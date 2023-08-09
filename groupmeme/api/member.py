from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme import config

import requests


class Member:
  __attrs__ = [
    'user_id',
    'member_id',
    'nickname',
    'muted',
    'image_url',
    'autokicked',
    'member_id'
  ]
  
  data = dict()
  
  
  def __init__(
    self,
    user_id:str,
    nickname:str,
    muted:bool,
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


  def from_dict(member_dict) -> 'Member':
    return Member(
      member_id=member_dict['id'] if 'id' in member_dict else None,
      user_id=member_dict['user_id'],
      nickname=member_dict['nickname'],
      muted=member_dict['muted'],
      image_url=member_dict['image_url'],
      autokicked=member_dict['autokicked'] if 'autokicked' in member_dict else None,
    )

  
  def _add(
    group_id:str,
    members:list[dict]
  ) -> str:
    headers = { 'X-Access-Token': config.API_TOKEN }
    body = { 'members': [member for member in members] }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/members/add', headers=headers, json=body)
    if res.status_code != 202:
      raise UnexpectedStatusCodeError(res.status_code, 202)
    add_members_result_id = res.json()['response']['results_id']
    return add_members_result_id


  def _add_result(
    group_id:str,
    result_id:str
  ):
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/members/results/{result_id}', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    add_members_results = res.json()['response']['members']
    members = [Member.from_dict(member) for member in add_members_results]
    return members


  def _remove(
    group_id:str,
    member_id:str
  ):
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/members/{member_id}/remove', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    return res.status_code


  def _update(
    group_id:str,
    nickname:str
  ):
    headers = { 'X-Access-Token': config.API_TOKEN }
    body = {
      "membership": {
        "nickname": nickname
      }
    }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/memberships/update', headers=headers, json=body)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    member_data = res.json()['response']
    print(res.status_code)
    return Member.from_dict(member_data)