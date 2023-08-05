from unittest import mock
import unittest
import requests
from requests import Response

from groupmeme.api.groups import *
from groupmeme.entities import Group
from groupmeme.api import init_groupmeme
from groupmeme.api.errors import UnexpectedStatusCodeError


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestGroupAPI(unittest.TestCase):
  def test_get_groups(self):
    expected_response = Response()
    expected_response.status_code = 200

    text = ''
    with open('tests/mock/groups.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    groups = get_groups()
    
    assert len(groups) == 1
    assert isinstance(groups[0], Group)
    
    
  def test_get_groups_fails(self):
    expected_response = Response()
    expected_response.status_code = 400

    text = ''
    with open('tests/mock/groups.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, get_groups)
    
    
  def test_get_former_groups(self):
    expected_response = Response()
    expected_response.status_code = 200

    text = ''
    with open('tests/mock/groups.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    groups = get_former_groups()
    
    assert len(groups) == 1
    assert isinstance(groups[0], Group)
    
    
  def test_get_former_groups_fails(self):
    expected_response = Response()
    expected_response.status_code = 400

    text = ''
    with open('tests/mock/groups.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, get_former_groups)
    
    
  def test_get_group(self):
    expected_response = Response()
    expected_response.status_code = 200

    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    group = get_group(group_id=123)
    
    assert isinstance(group, Group)
    
    
  def test_get_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400

    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, get_group, group_id=123)
    
    
  def test_create_group(self):
    expected_response = Response()
    expected_response.status_code = 201
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    group = create_group(
      name='Family',
      description='Coolest Family Ever',
      image_url='https://i.groupme.com/123456789',
      share=True
    )
    
    assert group.name == 'Family'
    assert group.description == 'Coolest Family Ever'
    assert group.image_url == 'https://i.groupme.com/123456789'
    
    assert isinstance(group, Group)
    
  
  def test_create_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, create_group,
      name='Family',
      description='Coolest Family Ever',
      image_url='https://i.groupme.com/123456789',
      share=True
    )
  
    
  def test_update_group(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    group = update_group(
      group_id='1234567890',
      name='Family',
      description='Coolest Family Ever',
      image_url='https://i.groupme.com/123456789',
      share=True
    )
    
    assert group.name == 'Family'
    assert group.description == 'Coolest Family Ever'
    assert group.image_url == 'https://i.groupme.com/123456789'
    
    assert isinstance(group, Group)


  def test_update_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, update_group,
      group_id='1234567890',
      name='Family',
      description='Coolest Family Ever',
      image_url='https://i.groupme.com/123456789',
      share=True
    )

    
  def test_destroy_group(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    result = destroy_group(group_id='1234567890')
    
    assert result == 200
    
    
  def test_destroy_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, destroy_group, group_id='1234567890')
  

  def test_join_group(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    group = join_group(group_id='1234567890', share_token='SHARE_TOKEN')
    
    assert group.name == 'Family'
    assert group.description == 'Coolest Family Ever'
    assert group.image_url == 'https://i.groupme.com/123456789'
    
    assert isinstance(group, Group)


  def test_join_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, join_group, group_id='1234567890', share_token='SHARE_TOKEN')


  def test_rejoin_group(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    group = rejoin_group(group_id='1234567890', share_token='SHARE_TOKEN')
    
    assert group.name == 'Family'
    assert group.description == 'Coolest Family Ever'
    assert group.image_url == 'https://i.groupme.com/123456789'
    
    assert isinstance(group, Group)
    
    
  def test_rejoin_group_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    text = ''
    with open('tests/mock/group.json', 'r') as file:
      text = file.read()
    expected_response._content = text.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, rejoin_group, group_id='1234567890', share_token='SHARE_TOKEN')
    
    
  def test_change_group_ownership(self):
    expected_response = Response()
    expected_response.status_code = 200
    expected_response._content = '{ "response": "mock rock" }'.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    change_group_ownership(group_id=1234, owner_id=4321)
    
    
  def test_change_group_ownership_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    expected_response._content = '{ "response": "mock rock" }'.encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, change_group_ownership, group_id=1234, owner_id=4321)