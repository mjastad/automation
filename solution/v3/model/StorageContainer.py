
__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Chris Brown", "M.Lavi"]
__license__ = "N/A"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

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
