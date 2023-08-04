from unittest import mock
import unittest
import requests
import json
from requests import Response

from api.messages import *
from entities import Member
from api import init_groupmeme
from api.errors import UnexpectedStatusCodeError


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestMessagesAPI(unittest.TestCase):
  def test_get_messages(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/messages.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    messages, count = get_messages(group_id='123', before_id=1234)
    assert count == 123
    assert len(messages) == 1
  
  def test_get_messages_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/messages.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, get_messages, group_id='123', before_id=1234)
  
  def test_create_messages(self):
    expected_response = Response()
    expected_response.status_code = 200
    message_input = dict()
    with open('tests/mock/message.json', 'r') as file:
      text = file.read()
      print(text)
      expected_response._content = text.encode('utf-8')
      message_input = json.loads(text)['response']
    requests.post = mock.MagicMock(return_value=expected_response)
    
    result = create_message(attachments=message_input['attachments'], text=message_input['text'], group_id='123')
    assert isinstance(result, Message)
  
  def test_create_messages_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    message_input = dict()
    with open('tests/mock/message.json', 'r') as file:
      text = file.read()
      print(text)
      expected_response._content = text.encode('utf-8')
      message_input = json.loads(text)['response']
    requests.post = mock.MagicMock(return_value=expected_response)
    
    self.assertRaises(UnexpectedStatusCodeError, create_message, attachments=message_input['attachments'], text=message_input['text'], group_id='123')

  