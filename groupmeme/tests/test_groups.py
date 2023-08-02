from unittest import mock
import requests
from requests import Response

from groupmeme.api.groups import *

def test_get_groups():
  expected_response = Response()
  expected_response.status_code = 200

  text = ''
  with open('groupmeme/tests/mock/groups.json', 'r') as file:
    text = file.read()
  expected_response._content = text.encode('utf-8')
  requests.get = mock.MagicMock(return_value=expected_response)
  
  groups = get_groups(token='token')
  
  assert len(groups) == 1
  assert isinstance(groups[0], Group)
  
  
def test_get_former_groups():
  expected_response = Response()
  expected_response.status_code = 200

  text = ''
  with open('groupmeme/tests/mock/groups.json', 'r') as file:
    text = file.read()
  expected_response._content = text.encode('utf-8')
  requests.get = mock.MagicMock(return_value=expected_response)
  
  groups = get_former_groups(token='token')
  
  assert len(groups) == 1
  assert isinstance(groups[0], Group)
  
  
def test_get_group():
  expected_response = Response()
  expected_response.status_code = 200

  text = ''
  with open('groupmeme/tests/mock/group.json', 'r') as file:
    text = file.read()
  expected_response._content = text.encode('utf-8')
  requests.get = mock.MagicMock(return_value=expected_response)
  
  group = get_group(token='token', group_id=123)
  
  assert isinstance(group, Group)