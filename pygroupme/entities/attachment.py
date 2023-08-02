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
    if url: self.url = url
    if _type: self._type = _type
    if lat: self.lat = lat
    if lng: self.lng = lng
    if name: self.name = name
    if token: self.token = token
    if placeholder: self.placeholder = placeholder
    if charmap: self.charmap = charmap