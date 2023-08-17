from unittest import TestCase
from unittest.mock import MagicMock
import requests
from requests import Response

from groupmeme.api import init_groupmeme, Leaderboard, Message
from groupmeme.api.errors import UnexpectedStatusCodeError


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestLeaderboard(TestCase):
  def test_get_likes(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/leaderboard/get_likes_res.json', 'rb') as file:
      expected_response._content = file.read()
      
    requests.get = MagicMock(return_value=expected_response)
    
    liked_messages = Leaderboard._likes(group_id='1234', period='week')
    
    assert len(liked_messages) == 2
    for message in liked_messages:
      assert isinstance(message, Message)
      
      
  def test_get_likes__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
      
    requests.get = MagicMock(return_value=expected_response)
    
    self.assertRaises(
      UnexpectedStatusCodeError,
      Leaderboard._likes, 
      group_id='1234', period='week'
    )
    
    
  def test_get_my_likes(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/leaderboard/get_likes_res.json', 'rb') as file:
      expected_response._content = file.read()
      
    requests.get = MagicMock(return_value=expected_response)
    
    liked_messages = Leaderboard._my_likes(group_id='1234')
    
    assert len(liked_messages) == 2
    for message in liked_messages:
      assert isinstance(message, Message)
      
      
  def test_get_my_likes__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
      
    requests.get = MagicMock(return_value=expected_response)
    
    self.assertRaises(
      UnexpectedStatusCodeError,
      Leaderboard._my_likes, 
      group_id='1234'
    )
    
    
  def test_get_my_hits(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/leaderboard/get_likes_res.json', 'rb') as file:
      expected_response._content = file.read()
      
    requests.get = MagicMock(return_value=expected_response)
    
    liked_messages = Leaderboard._my_hits(group_id='1234')
    
    assert len(liked_messages) == 2
    for message in liked_messages:
      assert isinstance(message, Message)


  def test_get_my_hits__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
      
    requests.get = MagicMock(return_value=expected_response)
    
    self.assertRaises(
      UnexpectedStatusCodeError,
      Leaderboard._my_hits, 
      group_id='1234'
    )