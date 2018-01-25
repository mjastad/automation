class Service:

   def __init__(self):
      self.ver = '/api/nutanix/v3/'

   @property
   def name(self):
      return self.ver
