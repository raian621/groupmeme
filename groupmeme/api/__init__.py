import groupmeme.api.groups as groups
import groupmeme.api.messages as messages
import groupmeme.api.members as members
import groupmeme.config as config

class GroupMeme:
  def __init__(self, token:str|None=None, api_url:str|None=None):
    init_groupmeme(token, api_url)
    self.groups = groups.GroupsAPI()
    self.messages = messages.MessagesAPI()
    self.members = members.MembersAPI()
    
    
def init_groupmeme(token:str, api_url:str):
  if token: config.API_TOKEN = token
  if api_url: config.API_URL = api_url