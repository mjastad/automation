#!/usr/bin/env python

"""
File: main.py: NTNX REST API Driver.
"""

from v2.core.Connection import Connection
from v2.core.Host import Host
from v2.core.User import User
from v2.services.VirtualMachineService import VirtualMachineService
from v2.services.ImageService import ImageService
from v2.services.StorageContainerService import StorageContainerService

'''
from v3.core.Connection import Connection
from v3.core.Host import Host
from v3.core.User import User
from v3.services.VirtualMachineService import VirtualMachineService
from v3.services.ImageService import ImageService
from v3.services.StorageContainerService import StorageContainerService
from v3.services.ApplicationService import ApplicationService
from v3.services.BlueprintService import BlueprintService
'''

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Joseph Angeletti", "Mark Lavi"]
__license__ = "N/A"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

USER = "REST Target User"
PASSWD = "REST Target User Password"
IPADDRESS = "REST Target IP"
PORT = "9440"

def _virtualMachines(connection):
    vmList = VirtualMachineService().getVMS(connection)
    for vm in vmList : vm.show() 

def getVirtualMachines(connection, data):
    vmList = VirtualMachineService().getVMS(connection, data)
    for vm in vmList : vm.show() 

def getApplications(connection, data):
    appList = ApplicationService().getApplications(connection, data)
    for app in appList : app.show() 

def getBlueprintss(connection, data):
    bpList = BlueprintService().getBlueprints(connection, data)
    for bp in bpList : bp.show()
     

def main():

    data = {'filter': '', 'offset': 0, 'length': 20}

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    #v2 API
    _virtualMachines(connection) 

    #v3 API
    #getVirtualMachines(connection, data) 
    #getApplications(connection, data) 
    #getBlueprints(connection, data) 

if __name__ == "__main__":
    main()
