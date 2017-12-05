
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Chris Brown", "M.Lavi"]
__license__ = "N/A"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

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


