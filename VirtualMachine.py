

class VirtualMachine:

  def __init__(self, inst):
     self.instance = inst

  def name(self):
     return self.instance['name']

  def description(self):
     return self.instance['description']

  def uuid(self):
     return self.instance['uuid']

  def powerState(self):
     return self.instance['power_state']

  def memory(self):
     return self.instance['memory_mb']