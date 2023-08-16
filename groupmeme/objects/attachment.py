from typing import Any


class Attachment:
  __attrs__ = [
    '_type',
    'url',
    'lat',
    'lng',
    'name',
    'token',
    'placeholder',
    'charmap'
  ]
  
  data = dict()
  
  def __init__(
    self,
    _type:str,
    url:str|None = None,
    lat:str|None = None,
    lng:str|None = None,
    name:str|None = None,
    token:str|None = None,
    placeholder:str|None = None,
    charmap:any = None
  ):
    if _type: self._type = _type
    if url:
      self.url = url
    if lat:
      if _type != 'location': raise ValueError('Parameter `lat` can only be used with location attachments')
    if lng:
      if _type != 'location': raise ValueError('Parameter `lng` can only be used with location attachments')
    if name:
      if _type != 'location': raise ValueError('Parameter `name` can only be used with location attachments')
    if token:
      if _type != 'split': raise ValueError('Parameter `token` can only be used with split attachments')
    if placeholder: 
      if _type != 'emoji': raise ValueError('Parameter `placeholder` can only be used with emoji attachments')
    if charmap: 
      if _type != 'emoji': raise ValueError('Parameter `charmap` can only be used with emoji attachments')
    
    self.lat = lat
    self.lng = lng
    self.name = name
    self.token = token
    self.placeholder = placeholder
    self.charmap = charmap
  

  def __setattr__(self, name:str, value:Any):
    if name in self.__attrs__ and name != 'data':
      self.data[name] = value
    else:
      raise AttributeError(name=name)
    
  
  def __getattr__(self, name:str):
    if name in self.__attrs__ and name != 'data':
      return self.data[name]
    else:
      raise AttributeError(name=name)
  
  
  def from_dict(attachment_dict: dict) -> 'Attachment':
    attachment_dict['_type'] = attachment_dict['type']
    del attachment_dict['type']
    return Attachment(**attachment_dict)
  
  
  def to_dict(self):
    return self.data
     