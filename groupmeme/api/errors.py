class UnexpectedStatusCodeError(Exception):
  def __init__(self, code, expected):
    super().__init__(f'Unexpected `{code}` status code, expected `{expected}`')
    
class APIParameterError(Exception):
  def __init__(self, message):
    super().__init__(message)