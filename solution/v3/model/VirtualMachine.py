

class VirtualMachine:

  type = "Virtual Machine"

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
     print 'type: ' + self.type
     print 'name: ' +  self.name
     print 'description: ' + self.description
     print 'uuid: ' +  self.uuid
     print 'power state: ' + self.powerState
     print 'memory: ' +  self.memory
     print ' '

