__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class Image:

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return self.instance['name']

  @property
  def uuid(self):
     return self.instance['uuid']

  @property
  def vmdisk_uuid(self):
      return self.instance['vm_disk_uuid']

  @property
  def storagecontainer_uuid(self):
      return self.instance['storage_container_uuid']

  @property
  def type(self):
      return self.instance['image_type']

  @property
  def state(self):
      return self.instance['image_state']
