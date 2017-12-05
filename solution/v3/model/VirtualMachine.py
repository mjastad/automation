
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Chris Brown", "M.Lavi"]
__license__ = "N/A"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class VirtualMachine:

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return str(self.instance['status']['name'])

  @property
  def description(self):
     return str(self.instance['status']['description'])

  @property
  def uuid(self):
     return str(self.instance['metadata']['uuid'])

  @property
  def powerState(self):
     return str(self.instance['status']['resources']['power_state'])

  @property
  def memory(self):
     return str(self.instance['status']['resources']['memory_size_mib'])

  def show(self):
     print 'name: ' +  self.name
     print 'description: ' + self.description
     print 'uuid: ' +  self.uuid
     print 'power state: ' + self.powerState
     print 'memory: ' +  self.memory
     print ' '

