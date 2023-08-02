import requests
from groupmeme.entities.member import member_from_dict
import groupmeme.config as config


def add_member(
  group_id:str,
  members:[dict]
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  body = { 'members': [member for member in members] }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/add', headers=headers, json=body)
  add_member_result_id = res.json()['response']['results_id']
  return add_member_result_id


def add_member_result(
  group_id:str,
  result_id:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/results/{result_id}', headers=headers)
  add_member_results = res.json()['response']
  members = [member_from_dict(member) for member in add_member_results]
  return members


def remove_member(
  group_id:str,
  member_id:str
):
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/members/{member_id}/remove', headers=headers)
  return res.status_code


def group_nickname(
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
  member_data = res.json()['response']
  print(res.status_code)
  return member_from_dict(member_data)