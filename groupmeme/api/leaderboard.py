import requests

from groupmeme.api.base import BaseInterface
from groupmeme.api.errors import UnexpectedStatusCodeError
from groupmeme.api import Message
from groupmeme.objects import Attachment
from groupmeme import config


class Leaderboard(BaseInterface):
  @staticmethod
  def _likes(group_id:str, period:str):
    """
    Returns a list of the liked messages in the group for a given time period.
    
    params:
    - `group_id (str)`: The ID of the group you wish to query liked messages from.
    - `period (str)`: The time period for which you want to query liked messages
    from. Possible values are 'day', 'week', or 'month', corresponding to liked
    liked messaged from the last day, last week, and last month respectively.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    res = requests.get(
      f'{config.API_URL}/{group_id}/likes',
      headers={ 'X-Access-Token': config.API_TOKEN },
      params={ 'period': period }
    )
    
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    messages_data = res.json()['response']['messages']
    messages = []
    for message_data in messages_data:
      message_data['attachments'] = [Attachment.from_dict(a) for a in message_data['attachments']]
      messages.append(Message.from_dict(message_data))
      
    return messages
  
  
  @staticmethod
  def _my_likes(group_id:str):
    """
    Returns a list of the messages you've liked in the group with ID `group_id`.
    
    params:
    - `group_id (str)`: The ID of the group you'd like to query your the messages
    you've liked from.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    res = requests.get(
      f'{config.API_URL}/{group_id}/likes/mine',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    messages_data = res.json()['response']['messages']
    messages = []
    for message_data in messages_data:
      message_data['attachments'] = [Attachment.from_dict(a) for a in message_data['attachments']]
      messages.append(Message.from_dict(message_data))
      
    return messages
  
  
  @staticmethod
  def _my_hits(group_id:str):
    """
    Returns a list of your messages that have been liked in the group with ID
    `group_id`.
    
    params:
    - `group_id (str)`: The ID of the group you'd like to query your liked
    messages from.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    res = requests.get(
      f'{config.API_URL}/{group_id}/likes/for_me',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    if res.status_code != 200:
      raise UnexpectedStatusCodeError(res.status_code, 200)
    
    messages_data = res.json()['response']['messages']
    messages = []
    for message_data in messages_data:
      message_data['attachments'] = [Attachment.from_dict(a) for a in message_data['attachments']]
      messages.append(Message.from_dict(message_data))
      
    return messages