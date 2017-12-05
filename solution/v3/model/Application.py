
class Application:

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
     return self.instance['status']['uuid']

  @property
  def state(self):
     return self.instance['status']['state']

  @property
  def blueprint(self):
     return self.instance['status']['resources']['app_blueprint_reference']['name']

  @property
  def blueprint_uuid(self):
     return self.instance['status']['resources']['app_blueprint_reference']['uuid']

  @property
  def project(self):
     return self.instance['metadata']['project_reference']['name']

  @property
  def project_uuid(self):
     return self.instance['metadata']['project_reference']['uuid']

  @property
  def owner(self):
     return self.instance['metadata']['owner_reference']['name']


  def show(self):
     print 'name: ' +  self.name
     #print 'description: ' + self.description
     print 'uuid: ' +  self.uuid
     print 'state: ' + self.state
     print 'blueprint: ' +  self.blueprint
     print 'blueprint_uuid: ' + self.blueprint_uuid
     print 'project: ' +  self.project
     print 'project_uuid: ' + self.project_uuid
     print 'owner: ' + self.owner
     print ' '
