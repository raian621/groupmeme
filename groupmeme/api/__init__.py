import groupmeme.config as config
from .bot import Bot
from .group import Group
from .member import Member
from .message import Message
from .user import User
from .chat import Chat
from .direct_message import DirectMessage


class GroupMeme:
  def __init__(self, token:str|None=None, api_url:str|None=None):
    init_groupmeme(token, api_url)
    self.group = Group
    self.bot = Bot
    self.message = Message
    self.member = Member
    self.user = User
    self.chat = Chat
    self.dm = DirectMessage
    
    
def init_groupmeme(token:str, api_url:str):
  if token: config.API_TOKEN = token
  if api_url: config.API_URL = api_url