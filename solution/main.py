#!/usr/bin/env python

"""
File: main.py: NTNX REST API Driver.
"""

#from V2 import *
from V3 import * 
from config import * 
from manageBlueprint import * 

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, Calm Workshop"
__credits__ = ["JAA", "ML"]
__license__ = "Use-As-Is"
__version__ = "2.0.1"
__maintainer__ = "M. Jastad"
__email__ = "mjastad@gmail.com"
__status__ = "Reference"

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
    #showList(VirtualMachineService().getVMS(connection, data)) 
    #showList(ApplicationService().getApplications(connection, data)) 
    #showList(BlueprintService().getBlueprints(connection, data)) 
    #showList(ProjectService().getProjects(connection, data)) 

    #importBlueprint(connection, PROJECT, BLUEPRINT_FILE, BLUEPRINT, DRAFT)
    #modifyCredential(connection, BLUEPRINT, DRAFT, CREDENTIAL, PASSWORD)
    #launchBlueprint(connection, BLUEPRINT, ACTIVE, APPLICATION)

    #deleteBlueprint(connection, BLUEPRINT, ACTIVE)
    #deleteApplication(connection, APPLICATION)

if __name__ == "__main__":
    main()

