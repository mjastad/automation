class Image:

  type = "image"

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
      return self.instance['vm_disk_id']

  @property
  def storagecontainer_uuid(self):
      return self.instance['storage_container_uuid']

  @property
  def image_type(self):
      return self.instance['image_type']

  @property
  def state(self):
      return self.instance['image_state']

  @property
  def size(self):
      return self.instance['vm_disk_size']

  def show(self):
  	print "type: " + self.type
  	print "name: " + self.name
	print "uuid: " + self.uuid
	print "vmdisk uuid: " + self.vmdisk_uuid
	print "storagecontainer uuid: " + self.storagecontainer_uuid
	print "image type: " + self.image_type
	print "state:" + self.state
	#print "vm disk size:" + self.size
	print ' '
