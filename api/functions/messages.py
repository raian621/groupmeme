import requests
from random import randint
from entities import Message, Attachment, message_from_dict
import config as config
from api.errors import UnexpectedStatusCodeError

def get_messages(
  group_id:str,
  before_id:int|None = None,
  since_id:int|None = None,
  after_id:int|None = None,
  limit:int|None = None
) -> [Message]:
  body = {}
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  if before_id: body['before_id'] = before_id
  if since_id: body['since_id'] = since_id
  if after_id: body['after_id'] = after_id
  if limit: body['limit'] = limit
  
  res = requests.get(f'{config.API_URL}/groups/{group_id}/messages', headers=headers, json=body)
  if res.status_code != 200:
    raise UnexpectedStatusCodeError(res.status_code, 200)
  messages_data = res.json()['response']
  count = messages_data['count']
  messages = [message_from_dict(message) for message in messages_data['messages']]
  return messages, count


def create_message(
  group_id:str,
  text:str,
  attachments:[Attachment]=None
):
  body = { 'message': { 'text': text }}
  headers = { 'X-Access-Token': config.API_TOKEN }
  
  if attachments: body['message']['attachments'] = [ dict(attachment) for attachment in attachments]
  body['source_guid'] = str(randint(0, 1000))
  
  res = requests.post(f'{config.API_URL}/groups/{group_id}/messages', headers=headers, json=body)
  if res.status_code != 200:
    raise UnexpectedStatusCodeError(res.status_code, 200)
  message_data = res.json()['response']
  return message_from_dict(message_data)