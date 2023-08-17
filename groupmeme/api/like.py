import requests

from groupmeme.api.base import BaseInterface
from groupmeme import config


class Like(BaseInterface):
  @staticmethod
  def _like(conversation_id:str, message_id:str) -> int:
    """
    Like a message. Returns the status code of the response from the GroupMe API
    server.
    
    params:
    - `conversation_id (str)`: The ID of the conversation that the message you want
    like is in.
    - `message_id (str)`: The ID of the message you want to like
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    res = requests.post(
      f'{config.API_URL}/messages/{conversation_id}/{message_id}/like',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    return res.status_code
  
  
  @staticmethod
  def _unlike(conversation_id:str, message_id:str) -> int:
    """
    Unlike a message. Returns the status code of the response from the GroupMe API
    server.
    
    params:
    - `conversation_id (str)`: The ID of the conversation that the message you want
    unlike is in.
    - `message_id (str)`: The ID of the message you want to unlike.
    
    raises:
    - `UnexpectedStatusCodeError`
    """
    res = requests.post(
      f'{config.API_URL}/messages/{conversation_id}/{message_id}/unlike',
      headers={ 'X-Access-Token': config.API_TOKEN },
    )
    
    return res.status_code