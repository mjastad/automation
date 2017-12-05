from v2.model.StorageContainer import StorageContainer

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

class StorageContainerService:

    def __init__(self):
        self.RESOURCE_SC = '/storage_containers/'

    def getStorageContainer(self, conn, uuid):
        storageContainerDictionary = conn.get(self.RESOURCE_SC + uuid)
        return StorageContainer(storageContainerDictionary)

    def getStorageContainers(self, conn):
        storageContainerList = []
        storageContainerDictionary = conn.get(self.RESOURCE_SC)

        for storageContainer in storageContainerDictionary['entities']:
             storageContainerList.append(StorageContainer(storageContainer))

        return storageContainerList

    def find(self, conn, id):
        storageContainerList = self.getStorageContainers(conn)
        for storageContainer in storageContainerList :
            if storageContainer.name.find(id) >= 0 : return storageContainer

        return None
