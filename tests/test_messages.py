from unittest import mock
import unittest
import requests
import json
from requests import Response

from groupmeme.api import Message
from groupmeme.api import init_groupmeme
from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.objects import Attachment


init_groupmeme(token='sdklfja', api_url='https://api.groupme.com/v3')

class TestMessagesAPI(unittest.TestCase):
  def test_get_messages(self):
    expected_response = Response()
    expected_response.status_code = 200
    with open('tests/mock/messages.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    messages, count = Message._messages(group_id='123', before_id=1234)
    assert count == 123
    assert len(messages) == 1
  
  def test_get_messages_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    with open('tests/mock/messages.json') as file:
      expected_response._content = file.read().encode('utf-8')
    requests.get = mock.MagicMock(return_value=expected_response)
    self.assertRaises(UnexpectedStatusCodeError, Message._messages, group_id='123', before_id=1234)
  
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
    attachments = [Attachment.from_dict(attachment_dict) for attachment_dict in message_input['attachments']]
    
    result = Message._create(
      attachments=attachments,
      text=message_input['text'],
      source_guid='GUID01',
      group_id='123'
    )
    assert isinstance(result, Message)
  
  def test_create_messages_fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    message_input = dict()
    with open('tests/mock/message.json', 'rb') as file:
      expected_response._content = file.read()
      message_input = json.loads(expected_response._content.decode('utf-8'))['response']
    requests.post = mock.MagicMock(return_value=expected_response)
    attachments = [Attachment.from_dict(attachment_dict) for attachment_dict in message_input['attachments']]
    
    self.assertRaises(
      UnexpectedStatusCodeError,
      Message._create,
      attachments=attachments,
      source_guid='GUID01',
      text=message_input['text'],
      group_id='123'
    )

  