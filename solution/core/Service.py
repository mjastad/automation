!/usr/bin/env python

''' 
Class Service: A non-mutable object designed to represent a RESTful service endpoint.
'''

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class Service:

   def __init__(self):
      self.ver = '/PrismGateway/services/rest/v2.0'

   @property
   def name(self):
      return self.ver
