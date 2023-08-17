from unittest import TestCase
from unittest.mock import MagicMock
import requests
from requests import Response

from groupmeme.api import init_groupmeme, Like


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestLikes(TestCase):
  def test_create_like(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    requests.post = MagicMock(return_value=expected_response)
    
    status_code = Like._like('123456', '54321')
    assert status_code == 200
    
    
  def test_create_like__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = MagicMock(return_value=expected_response)
    
    status_code = Like._like('123456', '54321')
    assert status_code == 400
    
    
  def test_destroy_like(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    requests.post = MagicMock(return_value=expected_response)
    
    status_code = Like._unlike('123456', '54321')
    assert status_code == 200
    
    
  def test_destroy_like__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = MagicMock(return_value=expected_response)
    
    status_code = Like._unlike('123456', '54321')
    assert status_code == 400