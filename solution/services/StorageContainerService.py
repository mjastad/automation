from model.StorageContainer import StorageContainer


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
