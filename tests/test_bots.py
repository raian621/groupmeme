import unittest
from unittest import mock
import requests
from requests import Response

from groupmeme.api import Bot
from groupmeme.objects import Attachment
from groupmeme.api import init_groupmeme
from groupmeme.api.errors import UnexpectedStatusCodeError, APIParameterError


init_groupmeme(token='asdfasdf', api_url='https://api.groupme.com/v3')

class TestBotsAPI(unittest.TestCase):
  def test_create_bot(self):
    expected_response = Response()
    expected_response.status_code = 201
    
    with open('tests/mock/bots/create_bot_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    result = Bot._create(
      name='Dasani Bot',
      group_id='1234567890',
      avatar_url='https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ipvgzU.b0q4M/v0/1000x-1.jpg',
      callback_url='https://example.herokuapp.com/'
    )
        
    assert isinstance(result, Bot)
    assert result.name == 'Dasani Bot'
    assert result.group_id == '1234567890'
    assert result.avatar_url == 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ipvgzU.b0q4M/v0/1000x-1.jpg'
    assert result.callback_url == 'https://example.herokuapp.com/'
    
  
  def test_create_bot__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    with open('tests/mock/bots/create_bot_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, Bot._create,
      name='Dasani Bot',
      group_id='1234567890',
      avatar_url='https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ipvgzU.b0q4M/v0/1000x-1.jpg',
      callback_url='https://example.herokuapp.com/'
    )


  def test_bot_send_message(self):
    expected_response = Response()
    expected_response.status_code = 201
    
    with open('tests/mock/bots/send_message_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    attachments = [
      Attachment(
        _type='image',
        url='https://i.groupme.com/123456789'  
      )
    ]
    result = Bot._send_message(
      bot_id="1234567890",
      text="Hello World",
      attachments=attachments
    )
    
    assert isinstance(result, int)
    assert result == 201
    
    
  def test_bot_send_message__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    attachments = [
      Attachment(
        _type='image',
        url='https://i.groupme.com/123456789'  
      )
    ]
    result = Bot._send_message(
      bot_id="1234567890",
      text="Hello World",
      attachments=attachments
    )
    
    assert isinstance(result, int)
    assert result == 400
    
    
  def test_bot_send_message__too_long(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    attachments = [
      Attachment(
        _type='image',
        url='https://i.groupme.com/123456789'  
      )
    ]
    self.assertRaises(
      APIParameterError,
      Bot._send_message,
      bot_id='1234567890',
      text='a' * 1001, # API documentation states that the text must be <= 1000 characters
      attachments=attachments
    )
    
    
  def test_get_bots(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/bots/get_bots_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.get = mock.MagicMock(return_value=expected_response)
    
    result = Bot._get_bots()
    
    assert len(result) == 1
    for bot in result:
      assert isinstance(bot, Bot)
    
    
  def test_get_bots__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.get = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, Bot._get_bots)
    
    
  def test_destroy_bot(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    result = Bot._destroy_bot(bot_id='1234')
    assert result == 200
    
    
  def test_destroy_bot__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.post = mock.MagicMock(return_value=expected_response)
    
    result = Bot._destroy_bot(bot_id='1234')
    assert result == 400
    