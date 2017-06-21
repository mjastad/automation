from Service import Service


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
