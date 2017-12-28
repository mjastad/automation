#!/usr/bin/env python

"""
File: main.py: NTNX REST API Driver.
"""

from V3 import * 
#from V2 import *

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["Joseph Angeletti", "Mark Lavi"]
__license__ = "Use-As-Is"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

USER = "admin"
PASSWD = "nx2Tech476!"
IPADDRESS = "10.21.81.39"
PORT = "9440"

VM = "PC"
APPLICATION = "NAME OF APPLICATION"
BLUEPRINT = "NAME OF BLUEPRINT"
PROJECT = "Calm"

def showList(itemList):
    for item in itemList : item.show()

def main():

    data = {'filter': '', 'offset': 0, 'length': 20}

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    #v2 API
    #showList(VirtualMachineService().getVMS(connection)) 
    #showList(ImageService().getImages(connection)) 
    #showList(StorageContainerService().getStorageContainers(connection)) 

    #v3 API
    showList(VirtualMachineService().getVMS(connection, data)) 
    vm = VirtualMachineService().findVM(connection, VM)
    if vm != None :
        vm = VirtualMachineService().getVM(connection, vm.uuid)
        vm.show()

    showList(ApplicationService().getApplications(connection, data)) 
    application = ApplicationService().findApplication(connection, APPLICATION)
    if application != None : 
	application = ApplicationService().getApplication(connection, application.uuid)
    	application.show()
    
    showList(BlueprintService().getBlueprints(connection, data)) 
    blueprint = BlueprintService().findBlueprint(connection, BLUEPRINT)
    if blueprint != None : 
	blueprint = BlueprintService().getBlueprint(connection, blueprint.uuid) 
    	blueprint.show()
    
    showList(ProjectService().getProjects(connection, data)) 
    project = ProjectService().findProject(connection, PROJECT) 
    if project != None : 
	project = ProjectService().getProject(connection, project.uuid)
    	project.show()

if __name__ == "__main__":
    main()

