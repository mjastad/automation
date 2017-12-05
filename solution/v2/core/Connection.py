import json
import requests

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["M.Jastad", "M.Lavi"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

#disable warnings: caution certificates should be used to prevent mitm attacks
requests.packages.urllib3.disable_warnings()

class Connection:

  def __init__(self, user, host):
    self.user = user
    self.host = host
    self.session = self.session()

  def session(self):
    session = requests.session()
    session.auth = (self.user.name, self.user.password)
    session.verify = False
    session.headers.update({'Content-Type': 'application/json; charset=utf-8',
                            'Accept': 'application/json'})
    return session

  def get(self, resource):
    serverResponse = self.session.get(self.host.url+resource)
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def post(self, resource, data):
    serverResponse = self.session.post(self.host.url+resource, json.dumps(data))
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def put(self, resource, data):
    serverResponse = self.session.put(self.host.url+resource, json.dumps(data))
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def delete(self, resource):
    serverResponse = self.session.delete(self.host.url+resource)
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

