
class Host():

   def __init__(self,ip,port):
       self.ipaddr = ip
       self.port = port
       self.service = Service()

   def port(self):
       return self.port

   def ip(self):
       return self.ipaddr	

   def service(self):
       return self.service

   def url(self):
       return "https://%s:%s%s" % self.ip() % self.port() % self.service().name()
