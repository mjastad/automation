class VirtualMachine:

  type = "virtual machine"

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return self.instance['status']['name']

  @property
  def description(self):
     return self.instance['status']['description']

  @property
  def uuid(self):
     return self.instance['metadata']['uuid']

  @property
  def ipaddress(self):
     return self.instance['status']['resources']['nic_list'][0]['ip_endpoint_list'][0]['ip']

  @property
  def powerState(self):
     return self.instance['status']['resources']['power_state']

  @property
  def memory(self):
     return self.instance['status']['resources']['memory_size_mib']

  def show(self):
     print 'type: ' + str(self.type)
     print 'name: ' + str(self.name)
     print 'description: ' + str(self.description)
     print 'ipaddress: ' + str(self.ipaddress)
     print 'uuid: ' + str(self.uuid)
     print 'power state: ' + str(self.powerState)
     print 'memory: ' + str(self.memory)
     print ' '
 
