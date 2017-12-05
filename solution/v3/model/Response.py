
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Chris Brown", "M.Lavi"]
__license__ = "N/A"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class Response:

  def __init__(self, inst):
     self.instance = inst

  @property
  def id(self):
     return self.instance['status']

  @property
  def status(self):
      return self.instance['status']
