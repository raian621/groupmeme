import requests
from random import randint
from groupmeme.entities.group import Group, group_from_dict
import groupmeme.config as config


def get_groups(
  page: int|None = None,
  per_page: int|None = None,
  omit: str|None = None
) -> [Group]:  
  req_params = {}
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  if page: req_params['page'] = page
  if per_page: req_params['per_page'] = per_page
  if omit: req_params['omit'] = omit
  
  res = requests.get(f'{config.API_URL}/groups', params=req_params, headers=headers)
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_former_groups() -> [Group]:
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.get(f'{config.API_URL}/groups/former', headers=headers)
  groups_data = res.json()
  groups = []

  for data in groups_data['response']:    
    groups.append(group_from_dict(data))
  
  return groups


def get_group(
  group_id: str
) -> Group:
  headers = { 'X-Access-Token': config.API_TOKEN }
 
  res = requests.get(f'{config.API_URL}/group/{group_id}', headers=headers)
  
  if res.status_code == 404:
    raise ValueError
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def create_group(
  name:str,
  description:str|None = None,
  image_url:str|None = None,
  share:bool|None = None
) -> Group:
  headers = { 'X-Access-Token': config.API_TOKEN }
  body = { 'name': name }
  
  if description: body['description'] = description
  if image_url: body['image_url'] = image_url
  if share: body['share'] = share
  
  res = requests.post(f'{config.API_URL}/groups', headers=headers, json=body)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def update_group(
  group_id:str,
  name:str|None = None,
  description:str|None = None,
  image_url:str|None = None,
  office_mode:bool|None = None,
  share:bool|None = None
) -> Group:
  headers = { 'X-Access-Token': config.API_TOKEN }
  body = {}
  
  if name: body['name'] = name
  if description: body['description'] = description
  if image_url: body['image_url'] = image_url
  if office_mode: body['office_mode'] = office_mode
  if share: body['share'] = name
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/update', headers=headers, json=body)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group
  
  
def destroy_group(group_id:str):
  headers = { 'X-Access-Token': config.API_TOKEN }
  res = requests.post(f'{config.API_URL}/groups/{group_id}/destroy', headers=headers)
  return res.status_code

def join_group(
  group_id:str,
  share_token:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/join/{share_token}', headers=headers)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def rejoin_group(
  group_id:str,
  share_token:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/join/{share_token}', headers=headers)
  group_data = res.json()
  group = group_from_dict(group_data['response'])
  
  return group


def change_group_ownership(
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
  change_result = res.json()
  return change_result['response']



