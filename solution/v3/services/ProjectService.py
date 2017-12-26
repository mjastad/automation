from v3.model.Task import Task
from v3.model.Project import Project 
from v3.model.Response import Response 


class ProjectService:

    def __init__(self):
        self.RESOURCE_PROJECT = '/projects/'


    def getProject(self, conn, uuid):
        projectDictionary = conn.get(self.RESOURCE_PROJECT + uuid)
        return Project(projectDictionary)

    def getProjects(self, conn, data):
        projectList = []
        projectDictionary = conn.post(self.RESOURCE_PROJECT + 'list', data)
        for project in projectDictionary['entities']:
             projectList.append(Project(project))

        return projectList

    def deleteProject(self, conn, proj):
        status_dictionary = conn.delete(self.RESOURCE_PROJECT + proj.uuid)
        return Response(status_dictionary)


    def findProject(self, conn, id):
        data = {'filter':'name=='+id, 'offset': 0, 'length': 100}
        projectList = self.getProjects(conn, data)
        for project in projectList : return project 

        return None
