import requests
from groupmeme.entities.member import member_from_dict
import groupmeme.config as config
from groupmeme.api.errors import UnexpectedStatusCodeError


def add_members(
  group_id:str,
  members:[dict]
) -> str:
  headers = { 'X-Access-Token': config.API_TOKEN }
  body = { 'members': [member for member in members] }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/add', headers=headers, json=body)
  if res.status_code != 202:
    raise UnexpectedStatusCodeError(res.status_code, 202)
  add_members_result_id = res.json()['response']['results_id']
  return add_members_result_id


def add_members_result(
  group_id:str,
  result_id:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/results/{result_id}', headers=headers)
  if res.status_code != 200:
    raise UnexpectedStatusCodeError(res.status_code, 200)
  add_members_results = res.json()['response']['members']
  members = [member_from_dict(member) for member in add_members_results]
  return members


def remove_member(
  group_id:str,
  member_id:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/{member_id}/remove', headers=headers)
  if res.status_code != 200:
    raise UnexpectedStatusCodeError(res.status_code, 200)
  return res.status_code


def set_group_nickname(
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
  return member_from_dict(member_data)