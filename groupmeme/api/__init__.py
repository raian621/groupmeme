import groupmeme.config as config
from .bot import Bot
from .group import Group
from .member import Member
from .message import Message


class GroupMeme:
  def __init__(self, token:str|None=None, api_url:str|None=None):
    init_groupmeme(token, api_url)
    self.groups = Group
    self.bots = Bot
    self.messages = None
    self.members = Member
    
    
def init_groupmeme(token:str, api_url:str):
  if token: config.API_TOKEN = token
  if api_url: config.API_URL = api_url