class Attachment:
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
  
  def __dict__(self):
    attachment_dict = {
      'type': self._type
    }
    
    if self.url: attachment_dict['url'] = self.url
    if self.lat: attachment_dict['lat'] = self.lat
    if self.lng: attachment_dict['lng'] = self.lng
    if self.name: attachment_dict['name'] = self.name
    if self.token: attachment_dict['token'] = self.token
    if self.placeholder: attachment_dict['placeholder'] = self.placeholder
    
    return attachment_dict
    