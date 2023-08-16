import requests
import groupmeme.config as config
from groupmeme.api.errors import UnexpectedStatusCodeError

def upload_picture(filepath:str):
  """
  Upload a picture to GroupMe's image CDN
  
  params:
  - `filepath (str)`: Path to the image file you wish to upload
  
  raises:
  - `UnexpectedStatusCodeError`
  - `FileNotFoundError`
  """
  res = None
  headers = { 'X-Access-Token': config.API_TOKEN }
  with open(filepath, 'rb') as image_file:
    body = image_file.read()
    res = requests.post(f'https://image.groupme.com/pictures', headers=headers, data=body)
  if res.status_code != 200:
    raise UnexpectedStatusCodeError(res.status_code, 200)
  res_data = res.json()['response']['payload']
  return res_data['url'], res_data['picture_url']
    