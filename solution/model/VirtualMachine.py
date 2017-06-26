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

class VirtualMachine:

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return self.instance['name']

  @property
  def description(self):
     return self.instance['description']

  @property
  def uuid(self):
     return self.instance['uuid']

  @property
  def powerState(self):
     return self.instance['power_state']

  @property
  def memory(self):
     return self.instance['memory_mb']
