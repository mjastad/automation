
class User:

  def __init__(self, uname, pwd):
     self.uname = uname
     self.passwd = pwd

  @property
  def name(self):
     return self.uname

  @property
  def password(self):
     return self.passwd


