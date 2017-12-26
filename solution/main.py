#!/usr/bin/env python

"""
File: main.py: NTNX REST API Driver.
"""
'''
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
        
def showList(itemList):
    for item in itemList : item.show()

def main():

    data = {'filter': '', 'offset': 0, 'length': 20}

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    #v2 API
    #showList(VirtualMachineService().getVMS(connection, data)) 

    #v3 API
    #showList(VirtualMachineService().getVMS(connection, data)) 

    showList(ApplicationService().getApplications(connection, data)) 
    application = ApplicationService().findApplication(connection, APPLICATION)
    application = ApplicationService().getApplication(connection, application.uuid)
    application.show()
    
    showList(BlueprintService().getBlueprints(connection, data)) 
    blueprint = BlueprintService().findBlueprint(connection, BLUEPRINT)
    blueprint = BlueprintService().getBlueprint(connection, blueprint.uuid) 
    blueprint.show()
    
    showList(ProjectService().getProjects(connection, data)) 
    project = ProjectService().findProject(connection, PROJECT) 
    project = ProjectService().getProject(connection, project.uuid)
    project.show()

if __name__ == "__main__":
    main()
