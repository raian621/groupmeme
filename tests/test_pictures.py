from groupmeme.api.pictures import *
from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.api import init_groupmeme

from unittest import mock
import unittest
import requests
import json
from requests import Response

init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestPicturesAPI(unittest.TestCase):
  def test_upload_picture(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/picture_upload_response.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    url, picture_url = upload_picture(filepath='tests/static/image.jpg')
    assert isinstance(url, str)
    assert isinstance(picture_url, str)


  def test_upload_picture__no_file(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/picture_upload_response.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(FileNotFoundError, upload_picture, filepath='tests/static/imag.jpg')
  
  
  def test_upload_picture__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/picture_upload_response.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.post = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, upload_picture, filepath='tests/static/image.jpg')