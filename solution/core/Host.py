#!/usr/bin/env python

''' 
Class Host: A non-mutable object designed to represent a RESTful host endpoint.
'''

from Service import Service

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class Host:

   def __init__(self, ip, port):

       self.ip_address = ip
       self.port_address = port
       self.service = Service()

   @property
   def port(self):
       return self.port_address

   @property
   def ip(self):
       return self.ip_address


   def service(self):
       return self.service

   @property
   def url(self):
       return "https://%s:%s%s" % (self.ip, self.port, self.service.name)
