from v3.model.Task import Task
from v3.model.Blueprint import Blueprint 
from v3.model.Response import Response 


class BlueprintService:

    def __init__(self):
        self.RESOURCE_BP = '/blueprints/'

    def createBlueprint(self, conn, data):
        status_dictionary = conn.post(self.RESOURCE_BP, data)
        return Response(status_dictionary) 

    def getBlueprint(self, conn, uuid):
        bpDictionary = conn.get(self.RESOURCE_BP + uuid)
        return Blueprint(bpDictionary)

    def getBlueprints(self, conn, data):
        bpList = []
        bpDictionary = conn.post(self.RESOURCE_BP + 'list', data)
        for bp in bpDictionary['entities']:
             bpList.append(Blueprint(bp))

        return bpList

    def getPendingBlueprints(self, conn, data):
        bpList = []
        bpDictionary = conn.post(self.RESOURCE_BP + 'pending_launch/list', data)
        for bp in bpDictionary['entities']:
             bpList.append(Blueprint(bp))

        return bpList

    def launchBlueprint(self, conn, id, data):
        status_dictionary = conn.post(self.RESOURCE_BP + id + '/launch', data)
        return Response(status_dictionary)

    def launchMarketplaceBlueprint(self, conn, id, data):
        status_dictionary = conn.post(self.RESOURCE_BP + id + '/marketplace_launch', data)
        return Response(status_dictionary)

    def deleteBlueprint(self, conn, bp):
        status_dictionary = conn.delete(self.RESOURCE_BP + bp.uuid)
        return Response(status_dictionary)

    def updateBlueprint(self, conn, bp, data):
        status_dictionary = conn.put(self.RESOURCE_BP + bp.uuid, data)
        return Response(status_dictionary)

    def findBlueprint(self, conn, id):
        data = {'filter': 'name=='+id+';state==ACTIVE', 'offset': 0, 'length': 20}
        blueprintList = self.getBlueprints(conn, data)
        for blueprint in blueprintList : return blueprint 

        return None
