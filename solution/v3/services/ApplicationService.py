from v3.model.Task import Task
from v3.model.Application import Application 
from v3.model.Response import Response 


class ApplicationService:

    def __init__(self):
        self.RESOURCE_APP = '/apps/'

    def createApplication(self, conn, data):
        status_dictionary = conn.post(self.RESOURCE_APP, data)
        return Response(status_dictionary) 

    def getApplication(self, conn, uuid):
        appDictionary = conn.get(self.RESOURCE_APP + uuid)
        return Appliction(appDictionary)

    def getApplications(self, conn, data):
        appList = []
        appDictionary = conn.post(self.RESOURCE_APP + 'list', data)
        for app in appDictionary['entities']:
             appList.append(Application(app))

        return appList

    def getApplicationRunbook(self, conn, app, ):
        appDictionary = conn.get(self.RESOURCE_APP + app.uuid + '/app_runlogs/list')
        return Appliction(appDictionary)

    def deleteApplication(self, conn, app):
        status_dictionary = conn.delete(self.RESOURCE_APP + app.uuid)
        return Response(status_dictionary)

    def updateAppliction(self, conn, app, data):
        status_dictionary = conn.put(self.RESOURCE_APP + app.uuid, data)
        return Response(status_dictionary)

    def find(self, conn, id):
        data = {'filter':'', 'offset': 0, 'length': 100}
        appList = self.getApplications(conn, data)
        for app in appList :
            if id == app.name : return app 

        return None
