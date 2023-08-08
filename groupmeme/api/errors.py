class UnexpectedStatusCodeError(Exception):
  def __init__(self, code, expected):
    super().__init__(f'Unexpected `{code}` status code, expected `{expected}`')
    
class APIParameterError(Exception):
  def __init__(self, param_name, max_length, length):
    super().__init__(f'API parameter `{param_name}` exceeded max length of {max_length} characters ({length} characters)')