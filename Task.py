

class Task:

  def __init__(self, inst):
     self.instance = inst

  def id(self):
     return self.instance['task_uuid']