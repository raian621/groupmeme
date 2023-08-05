class UnexpectedStatusCodeError(Exception):
  def __init__(self, code, expected):
    super().__init__(f'Unexpected `{code}` status code, expected `{expected}`')