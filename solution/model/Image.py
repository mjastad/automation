

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
