from unittest import TestCase
from unittest.mock import MagicMock
import requests
from requests import Response

from groupmeme.api import init_groupmeme, Chat
from groupmeme.api.errors import UnexpectedStatusCodeError


init_groupmeme(token='asdfasdf', api_url='https://api.groupme.com/v3')

class TestChats(TestCase):
  def test_get_chats(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/chats/get_chats_res.json', 'rb') as file:
      expected_response._content = file.read()
      
    requests.get = MagicMock(return_value=expected_response)
    
    result = Chat._chats(page=1, per_page=20)
    
    assert len(result) == 1
    assert isinstance(result[0], Chat)
  
  
  def test_get_chats__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
      
    requests.get = MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, Chat._chats, page=1, per_page=20)