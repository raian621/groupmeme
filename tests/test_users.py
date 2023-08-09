import requests
from requests import Response
from unittest import TestCase
from unittest.mock import MagicMock

from groupmeme.api import User
from groupmeme.api.errors import UnexpectedStatusCodeError


class TestUsers(TestCase):
  def test_get_me(self):
    expected_result = Response()
    expected_result.status_code = 200
    
    with open('tests/mock/users/get_me_res.json', 'rb') as file:
      expected_result._content = file.read()
      
    requests.get = MagicMock(return_value=expected_result)
    
    user = User._me()
    
    assert isinstance(user, User)
  
  
  def test_get_me__fails(self):
    expected_result = Response()
    expected_result.status_code = 400
      
    requests.get = MagicMock(return_value=expected_result)
    
    self.assertRaises(UnexpectedStatusCodeError, User._me)
    
  
  def test_update_me(self):
    expected_result = Response()
    expected_result.status_code = 200
    
    with open('tests/mock/users/update_me_res.json', 'rb') as file:
      expected_result._content = file.read()
      
    requests.post = MagicMock(return_value=expected_result)
    
    user = User._update_me(
      avatar_url="https://4.bp.blogspot.com/-GAeMYT8SZoI/TtBTK209xMI/AAAAAAAAWts/5nmvpmmvoWo/s1600/TopGun_059Pyxurz.jpg",
      name="Tom Skerritt",
      email="viper@topgun.usaf.mil",
      zip_code="92145"
    )
