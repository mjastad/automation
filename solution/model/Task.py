'''
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"
'''

class Task:

  def __init__(self, inst):
     self.instance = inst

  @property
  def id(self):
     return self.instance['task_uuid']

  @property
  def status(self):
      return self.instance['progress_status']
