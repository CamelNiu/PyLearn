import requests

class Request(object):
  """docstring for Request"""
  paramMap = {}
  paramKeysSet = (['params','header','cookie'])

  def get(self,url):
    self.res = requests.get(url)
    return self

  def text(self):
    return self.res.text
  def encoding(self):
    return self.res.encoding
  def content(self):
    return self.res.content
  def headers(self):
    return self.res.headers
  def code(self):
    return self.res.status_code
  def raw(self):
    return self.res.raw
  def ok(self):
    return self.res.ok
  def json(self):
    return self.res.json()
  def error(self):
    return self.raise_for_status()













r = Request()

r.get('http://api.digifinex.com/invite/flash')

print(r.content())