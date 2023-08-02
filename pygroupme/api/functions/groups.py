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
  req_params = {}
  headers = { 'X-Access-Token': token }
  
  if page: req_params['page'] = page
  if per_page: req_params['per_page'] = per_page
  if omit: req_params['omit'] = omit
  
  res = requests.get(f'{BASE_URL}/groups', params=req_params, headers={'X-Access-Token': token})
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_former_groups(
  token: str,
) -> [Group]:
  req_params = { 'token': token }
  headers = { 'X-Access-Token': token }
  
  res = requests.get(f'{BASE_URL}/groups/former', params=req_params, headers=headers)
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_group(
  token: str,
  group_id: str
) -> Group:
  req_params = { 'token': token }
  headers = { 'X-Access-Token': token }
 
  res = requests.get(f'{BASE_URL}/group/{group_id}', params=req_params, headers=headers)
  
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
  headers = { 'X-Access-Token': token }
  body = { 'name': name }
  
  if description: body['description'] = description
  if image_url: body['image_url'] = image_url
  if share: body['share'] = share
  
  res = requests.post(f'{BASE_URL}/groups', headers=headers, json=body)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def update_group(
  token:str,
  group_id:str,
  name:str|None = None,
  description:str|None = None,
  image_url:str|None = None,
  office_mode:bool|None = None,
  share:bool|None = None
) -> Group:
  headers = { 'X-Access-Token': token }
  body = {}
  
  if name: body['name'] = name
  if description: body['description'] = description
  if image_url: body['image_url'] = image_url
  if office_mode: body['office_mode'] = office_mode
  if share: body['share'] = name
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/update', headers=headers, body=body)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group
  
  
def destroy_group(
  token:str,
  group_id:str,
):
  headers = { 'X-Access-Token': token }
  res = requests.post(f'{BASE_URL}/groups/{group_id}/destroy', headers=headers)


def join_group(
  token:str,
  group_id:str,
  share_token:str
):
  headers = { 'X-Access-Token': token }
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/join/{share_token}', headers=headers)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def rejoin_group(
  token:str,
  group_id:str,
  share_token:str
):
  headers = { 'X-Access-Token': token }
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/join/{share_token}', headers=headers)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def change_group_ownership(
  token:str,
  group_id:str,
  owner_id:str
):
  headers = { 'X-Access-Token': token }
  body = {
    'requests': [{
      'group_id': group_id,
      'owner_id': owner_id
    }]
  }
  
  res = requests.post(f'{BASE_URL}/groups/change_owners', headers=headers, json=body)
  change_result = res.json()
  return change_result['response']


def add_member(
  token:str,
  group_id:str,
  members:[dict]
):
  headers = { 'X-Access-Token': token }
  body = { 'members': [member for member in members] }
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/members/add', headers=headers, json=body)
  add_member_result_id = res.json()['response']['results_id']
  return add_member_result_id


def add_member_result(
  token:str,
  group_id:str,
  result_id:str
):
  headers = { 'X-Access-Token': token }
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/members/results/{result_id}', headers=headers)
  add_member_results = res.json()['response']
  members = [member_from_dict(member) for member in add_member_results]
  return members


def remove_member(
  token:str,
  group_id:str,
  member_id:str
):
  headers = { 'X-Access-Token': token }
  
  res = requests.post(f'{BASE_URL}/groups/{group_id}/members/{member_id}', headers=headers)
  return res.status_code


def group_nickname(
  token: str,
):
  req_params = {}
  headers = { 'X-Access-Token': token }

def get_messages(
  token: str,
):
  req_params = {}
  headers = { 'X-Access-Token': token }

def get_hits(
  token: str,
):
  req_params = {}
  headers = { 'X-Access-Token': token }

def get_likes(
  token: str,
):
  req_params = {}
  headers = { 'X-Access-Token': token }