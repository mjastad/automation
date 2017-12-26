
class Project:

  type = "Project"

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
  def state(self):
     return self.instance['status']['state']

  @property
  def status(self):
     return self.instance['status']

  @property
  def spec(self):
     return self.instance['spec']

  @property
  def metadata(self):
     return self.instance['metadata']

  @property
  def apiVersion(self):
     return self.instance['api_version']


  def show(self):
     print 'type: ' + self.type 
     print 'name: ' + self.name
     print 'description: ' + self.description
     print 'uuid: ' + self.uuid
     print 'state: ' + self.state
     print ' '
