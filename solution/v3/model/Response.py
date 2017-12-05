

class Response:

  def __init__(self, inst):
     self.instance = inst

  @property
  def id(self):
     return self.instance['status']

  @property
  def status(self):
      return self.instance['status']
