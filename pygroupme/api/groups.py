from .functions.groups import *

class GroupsAPI:
  def __init__(
    self, 
    token: str, 
    group_id: str|None = None
  ):
    self.token = token
    if group_id != None:
      self.group_id = group_id
    
  def groups(self):
    pass
  
  def former_groups(self):
    pass
  
  def show(self):
    pass
  
  def update(self):
    pass
  
  def create(self):
    pass
  
  def destroy(self):
    pass
  
  def join(self):
    pass
  
  def rejoin(self):
    pass
  
  def change_ownership(self):
    pass
  
  def add_member(self):
    pass
  
  def add_member_result(self):
    pass
  
  def remove_member(self):
    pass
  
  def nickname(self):
    pass
  
  def messages(self):
    pass
  
  def send_message(self):
    pass
  
  def hits(self):
    pass
  
  def likes(self):
    pass
  