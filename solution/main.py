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

USER = "admin"
#PASSWD = "passw0rd"
#IPADDRESS = "10.68.69.102"
PASSWD = "nx2Tech254!"
IPADDRESS = "10.21.71.39"
PORT = "9440"

def getVirtualMachines(connection, data):
    vmService = VirtualMachineService()
    vmList = vmService.getVMS(connection, data)

    for vm in vmList : vm.show() 

def getApplications(connection, data):
    appService = ApplicationService()
    appList = appService.getApplications(connection, data)

    for app in appList : app.show() 

def getBlueprintss(connection, data):
    bpService = BlueprintService()
    bpList = bpService.getBlueprints(connection, data)

    for bp in bpList : bp.show()
     

def main():

    data = {'filter': '', 'offset': 0, 'length': 20}

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    getVirtualMachines(connection, data) 
    getApplications(connection, data) 
    getBlueprints(connection, data) 

if __name__ == "__main__":
    main()
