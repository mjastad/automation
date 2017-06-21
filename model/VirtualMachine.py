

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
