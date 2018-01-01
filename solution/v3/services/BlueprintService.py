from v3.model.Task import Task
from v3.model.Blueprint import Blueprint 
from v3.model.Response import Response 

import json

class BlueprintService:

    def __init__(self):
        self.RESOURCE_BP = '/blueprints/'

    def importBlueprint(self, conn, fname, bpname, proj):

        try:
           blueprint = json.load(open(fname))
        except:
           print "error:  can't open file %s" % fname

        project = {'kind':'project','uuid':proj.uuid}
        blueprint["metadata"]["project_reference"] = project 
        blueprint["metadata"]["name"] = bpname 
        blueprint["spec"]["name"] = bpname 
        del(blueprint["status"])

        status_dictionary = conn.post(self.RESOURCE_BP + 'import_json', blueprint)
        return Response(status_dictionary)

    def createBlueprint(self, conn, data):
        status_dictionary = conn.post(self.RESOURCE_BP, data)
        return Response(status_dictionary) 

    def getBlueprint(self, conn, uuid):
        bpDictionary = conn.get(self.RESOURCE_BP + uuid)
        return Blueprint(bpDictionary)

    def getBlueprints(self, conn, data):
        bpList = []
        bpDictionary = conn.post(self.RESOURCE_BP + 'list', data)
        for bp in bpDictionary['entities'] : bpList.append(Blueprint(bp))

        return bpList

    def getPendingBlueprints(self, conn, data):
        bpList = []
        bpDictionary = conn.post(self.RESOURCE_BP + 'pending_launch/list', data)
        for bp in bpDictionary['entities'] : bpList.append(Blueprint(bp))

        return bpList

    def launchBlueprint(self, conn, blueprint, appname):
        del(blueprint.entity["status"])
        del(blueprint.entity["spec"]["name"])

        profile = next(item for item in blueprint.entity["spec"]["resources"]["app_profile_list"] if item["name"] == "Nutanix")
        blueprint.entity["spec"]["app_profile_reference"] = {'kind':'app_profile','uuid':profile["uuid"]}
	blueprint.entity["spec"]["application_name"] = appname

        status_dictionary = conn.post(self.RESOURCE_BP + blueprint.uuid + '/launch', blueprint.entity)
        return Response(status_dictionary)

    def launchMarketplaceBlueprint(self, conn, id, data):
        status_dictionary = conn.post(self.RESOURCE_BP + id + '/marketplace_launch', data)
        return Response(status_dictionary)

    def deleteBlueprint(self, conn, bp):
        status_dictionary = conn.delete(self.RESOURCE_BP + bp.uuid)
        return Response(status_dictionary)

    def updateBlueprint(self, conn, bp):
        status_dictionary = conn.put(self.RESOURCE_BP + bp.uuid, bp.entity)
        return Response(status_dictionary)

    def findBlueprint(self, conn, name, state):
        data = {'filter': 'name==' + name + ';state==' + state, 'offset': 0, 'length': 20}
        blueprintList = self.getBlueprints(conn, data)
        for blueprint in blueprintList : return blueprint 

        return None
