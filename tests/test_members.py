from unittest import mock
import unittest
import requests
import json
from requests import Response

from api.members import *
from entities import Member
from api import init_groupmeme
from api.errors import UnexpectedStatusCodeError


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestMembersAPI(unittest.TestCase):
  def test_add_members(self):
    expected_response = Response()
    expected_response.status_code = 202
    with open('tests/mock/add_members_res.json') as file:
      expected_response._content = file.read().encode('utf-8')
    
    requests.post = mock.MagicMock(return_value=expected_response)
    add_members_result = add_members(1234, members={
      'members': [
        {
          "nickname": "Mom",
          "user_id": "1234567890",
          "guid": "GUID-1"
        },
        {
          "nickname": "Dad",
          "phone_number": "+1 2123001234",
          "guid": "GUID-2"
        },
        {
          "nickname": "Jane",
          "email": "jane@example.com",
          "guid": "GUID-3"
        }
      ]
    })
    
    assert isinstance(add_members_result, str)
    
  
  def test_add_members_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/add_members_res.json') as file:
      expected_response._content = file.read().encode('utf-8')
    
    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, add_members, 1234, members={
      'members': [
        {
          "nickname": "Mom",
          "user_id": "1234567890",
          "guid": "GUID-1"
        },
        {
          "nickname": "Dad",
          "phone_number": "+1 2123001234",
          "guid": "GUID-2"
        },
        {
          "nickname": "Jane",
          "email": "jane@example.com",
          "guid": "GUID-3"
        }
      ]
    })
  
  
  def test_add_members_result(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/members_res.json') as file:
      expected_response._content = file.read().encode('utf-8')
    
    requests.post = mock.MagicMock(return_value=expected_response)
    result = add_members_result(group_id='123', result_id='GUID')
    
    assert len(result) == 2
    for member in result:
      assert isinstance(member, Member)
  
  
  def test_add_members_result_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/members_res.json') as file:
      expected_response._content = file.read().encode('utf-8')
    
    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, add_members_result, group_id='123', result_id='GUID')
  
  
  def test_remove_member(self):
    expected_response = Response()
    expected_response.status_code = 200

    requests.post = mock.MagicMock(return_value=expected_response)
    result = remove_member(group_id='123', member_id='123')
    
    assert result == 200
  
  def test_remove_member_fails(self):
    expected_response = Response()
    expected_response.status_code = 400

    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, remove_member, group_id='123', member_id='123')
  
  
  def test_set_group_nickname(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/member.json') as file:
      expected_response._content = file.read().encode('utf-8')

    requests.post = mock.MagicMock(return_value=expected_response)
    result = set_group_nickname(group_id='123', nickname='Nick')
    
    assert isinstance(result, Member)
    assert result.nickname == 'Nick'
  
  
  def test_set_group_nickname_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/member.json') as file:
      expected_response._content = file.read().encode('utf-8')

    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, set_group_nickname, group_id='123', nickname='Nick')

  