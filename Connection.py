import pprint
import json
import os
import random
import requests
import sys
import traceback

#This block initializes the parameters for the request.
class Connection():                

  def __init__(self,user,host):
    self.user = user
    self.host = host
    self.session = self.session()

  def session(self):
    session = requests.session()
    session.auth = (self.user.name(),self.user.password())
    session.verify = False
    session.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    return session

  def get(self,resource):
    serverResponse = self.session.get(self.host.url()+resource) 
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def post(self,resource,data):
    serverResponse = self.session.post(self.host.url()+resource,data)
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def put(self,resource,data):
    serverResponse = self.session.put(self.host.url()+resource,data)
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

  def delete(self,resource,data):
    serverResponse = self.session.delete(self.host.url()+resource,data)
    print "Response code: %s" % serverResponse.status_code
    return json.loads(serverResponse.text)

