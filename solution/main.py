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
from v3.services.ProjectService import ProjectService
'''

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Joseph Angeletti", "Mark Lavi"]
__license__ = "Use-As-Is"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

USER = "REST Target User"
PASSWD = "REST Target User Password"
IPADDRESS = "REST Target IP"
PORT = "9440"

APPLICATION = "NAME OF APPLICATION"
BLUEPRINT = "NAME OF BLUEPRINT"
PROJECT = "NAME OF PROJECT"

def _virtualMachines(connection):
    vmList = VirtualMachineService().getVMS(connection)
    for vm in vmList : vm.show() 

def getVirtualMachines(connection, data):
    vmList = VirtualMachineService().getVMS(connection, data)
    for vm in vmList : vm.show() 

def getApplications(connection, data):
    appList = ApplicationService().getApplications(connection, data)
    for app in appList : app.show() 

def getApplication(connection, data):
    application = ApplicationService().getApplication(connection, data)
    application.show() 

def getBlueprints(connection, data):
    bpList = BlueprintService().getBlueprints(connection, data)
    for bp in bpList : bp.show()

def getBlueprint(connection, data):
    blueprint = BlueprintService().getBlueprint(connection, data)
    blueprint.show()

def getProjects(connection, data):
    projectList = ProjectService().getProjects(connection, data)
    for project in projectList : project.show()

def getProject(connection, data):
    project = ProjectService().getProject(connection, data)
    project.show()

def main():

    data = {'filter': '', 'offset': 0, 'length': 20}

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    #v2 API
    #_virtualMachines(connection) 

    #v3 API
    #getVirtualMachines(connection, data) 

    getApplications(connection, data) 
    application = ApplicationService().findApplication(connection, APPLICATION)
    getApplication(connection,application.uuid)

    getBlueprints(connection, data) 
    blueprint = BlueprintService().findBlueprint(connection, BLUEPRINT)
    getBlueprint(connection, blueprint.uuid) 

    getProjects(connection, data) 
    project = ProjectService().findProject(connection, PROJECT) 
    getProject(connection, project.uuid) 

if __name__ == "__main__":
    main()
