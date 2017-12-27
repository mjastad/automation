class Task:

  type = "task"

  def __init__(self, inst):
     self.instance = inst

  @property
  def id(self):
     return self.instance['task_uuid']

  @property
  def status(self):
      return self.instance['progress_status']

  def show(self):
      print 'type: ' + self.type
      print 'id: ' + self.id
      print 'status: ' + self.status
      print ' '
