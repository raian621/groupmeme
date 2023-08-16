from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.api.base import BaseInterface
from groupmeme import config

import requests


class Member(BaseInterface):
  __attrs__ = [
    'user_id',
    'member_id',
    'nickname',
    'muted',
    'image_url',
    'autokicked',
    'member_id'
  ]
  
  
  def __init__(
    self,
    user_id:str,
    nickname:str,
    muted:bool,
    image_url:str,
    autokicked:bool,
    member_id:str,
  ):
    """
    `Member` constructor
    
    params:
    - `user_id (str)`: User id of the member.
    - `nickname (str)`: Nickname of the member.
    - `muted (bool)`: `True` if the member is muted, else `False`.
    - `image_url (str)`: URL to the profile picture of the member.
    - `autokicked (bool)`: `True` if the member was autokicked, else `False`.
    - `member_id (str)`: The group member id of the member.
    """
    self.member_id = member_id
    self.user_id = user_id
    self.nickname = nickname
    self.muted = muted
    self.image_url = image_url
    self.autokicked = autokicked


  def from_dict(member_dict) -> 'Member':
    """
    Returns a `Member` object initialized using the `member_dict` parameter.
    
    params:
    - `message_dict (dict)`: Used to initialize the returned `Member` object.
    Must contain keys and values corresponding to the parameters in
    `Member.__init__`
    """
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
    """
    Official documentation: https://dev.groupme.com/docs/v3#members_add
    
    Add one or more members to the group given by `group_id`. Returns a GUID 
    that can be used to query the status of the member's addition to the group
    
    params:
    - `group_id (str)`: ID of the group you wish to add users to.
    - `members (list[dict])`: Members to add to the group; Must have key `nickname`
    and optionally keys `user_id`, `phone_number`, `email`, `guid`
    
    raises:
    - `UnexpectedStatusCodeError`
    """
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
    """
    Get the membership addition results. Successfully created members will be
    returned. Failed memberships and invites are omitted.
    
    params:
    - `group_id (str)`: ID of the group you wish to check the memberships result of
    - `result_id (str)`: GUID returned by a previous call to `Member._add()`.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
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
    """
    Remove a member from the group given by `group_id`
    
    params:
    - `group_id (str)`: ID of the group you wish to remove a member from
    - `member_id (str)`: ID of the member you wish to remove from the group
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    headers = { 'X-Access-Token': config.API_TOKEN }
    
    res = requests.post(f'{config.API_URL}/groups/{group_id}/members/{member_id}/remove', headers=headers)
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    return res.status_code


  def _update(
    group_id:str,
    nickname:str
  ):
    """
    Change your nickname in the group given by `group_id`
    
    NOTE: You can only change your own nickname.
    
    params:
    - `group_id (str)`: ID of the group you wish to update your nickname in.
    - `nickname (str)`: The new nickname for your user.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
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