import requests
from pygroupme.__constants__ import BASE_URL
from pygroupme.entities.group import Group, group_from_dict
from pygroupme.entities.member import member_from_dict

def get_groups(
  token: str,
  page: int|None = None,
  per_page: int|None = None,
  omit: str|None = None
) -> [Group]:
  req_params = { 'token': token }
  
  if page: req_params['page'] = page
  if per_page: req_params['per_page'] = per_page
  if omit: req_params['omit'] = omit
  
  res = requests.get(f'{BASE_URL}/groups', params=req_params)
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_former_groups(
  token: str,
) -> [Group]:
  req_params = { 'token': token }
  
  res = requests.get(f'{BASE_URL}/groups/former', params=req_params)
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_group(
  token: str,
  id: str
) -> Group:
  req_params = { 'token': token, 'id': id }
 
  res = requests.get(f'{BASE_URL}/group', params=req_params)
  
  if res.status_code == 404:
    raise ValueError
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def create_group(
  token:str,
  name:str,
  description:str|None = None,
  image_url:str|None = None,
  share:bool|None = None
) -> Group:
  req_params = { 
    'token': token,
  }
  
  body = {
    'name': name
  }
  
  if description: req_params['description'] = description
  if image_url: req_params['image_url'] = image_url
  if share: req_params['share'] = share
  
  res = requests.post(f'{BASE_URL}/groups', params = req_params, json=body)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def update_group(
  token: str,
) -> Group:
  req_params = { 'token': token }


def destroy_group(
  token: str,
):
  req_params = { 'token': token }

def join_group(
  token: str,
):
  req_params = { 'token': token }

def rejoin_group(
  token: str,
):
  req_params = { 'token': token }

def change_group_ownership(
  token: str,
):
  req_params = { 'token': token }

def add_member(
  token: str,
):
  req_params = { 'token': token }

def add_member_result(
  token: str,
):
  req_params = { 'token': token }

def group_nickname(
  token: str,
):
  req_params = { 'token': token }

def get_messages(
  token: str,
):
  req_params = { 'token': token }

def get_hits(
  token: str,
):
  req_params = { 'token': token }

def get_likes(
  token: str,
):
  req_params = { 'token': token }