from unittest import TestCase
from unittest.mock import MagicMock
import requests
from requests import Response

from groupmeme.api import init_groupmeme, DirectMessage
from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.objects import Attachment


init_groupmeme(token='asdfasdf', api_url='https://api.groupme.com/v3')

class TestDirectMessages(TestCase):
  def test_get_dms(self):
    expected_response = Response()
    expected_response.status_code = 200
    
    with open('tests/mock/dms/get_dms_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.get = MagicMock(return_value=expected_response)
    
    dms = DirectMessage._list(
      other_user_id="123456", before_id="1234", after_id="0123"
    )
    
    assert len(dms) == 1
    assert isinstance(dms[0], DirectMessage)
    dm = dms[0]
    assert isinstance(dm.attachments[0], Attachment)


  def test_get_dms__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    requests.get = MagicMock(return_value=expected_response)
    
    self.assertRaises(
      UnexpectedStatusCodeError,
      DirectMessage._list,
      other_user_id="123456",
      before_id="1234", after_id="0123"
    )


  def test_create_dm(self):
    expected_response = Response()
    expected_response.status_code = 201
    
    with open('tests/mock/dms/create_dm_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.post = MagicMock(return_value=expected_response)
    
    dm = DirectMessage._create(
      source_guid='GUID',
      recipient_id='123456',
      text='Hello',
      attachments=[Attachment('image', url='https://google.com')]
    )
    
    assert isinstance(dm, DirectMessage)
    assert isinstance(dm.attachments[0], Attachment)


  def test_create_dm__fails(self):
    expected_response = Response()
    expected_response.status_code = 400
    
    with open('tests/mock/dms/create_dm_res.json', 'rb') as file:
      expected_response._content = file.read()
    
    requests.post = MagicMock(return_value=expected_response)
    self.assertRaises(
      UnexpectedStatusCodeError,
      DirectMessage._create,
      source_guid='GUID',
      recipient_id='123456',
      text='Hello',
      attachments=[Attachment('image', url='https://google.com')]
    )