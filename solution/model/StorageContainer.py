

class StorageContainer:

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return self.instance['name']

  @property
  def uuid(self):
     return self.instance['storage_container_uuid']

  @property
  def id(self):
      return self.instance['id']

  @property
  def cluster_uuid(self):
      return self.instance['cluster_uuid']

  @property
  def rf(self):
      return self.instance['replication_factor']
