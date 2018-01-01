from V3 import *
  
def getProject(connection, projname):
    project = None
    project = ProjectService().findProject(connection, projname)

    if project :
        project = ProjectService().getProject(connection, project.uuid)

    return project

def getBlueprint(connection, bpname, bpstate):
    blueprint = None
    blueprint = BlueprintService().findBlueprint(connection, name=bpname, state=bpstate)

    if blueprint :
        blueprint = BlueprintService().getBlueprint(connection, blueprint.uuid)

    return blueprint

def importBlueprint(connection, projname, bpfile, bpname, bpstate):

    project = getProject(connection,projname)
    if project :
        response = BlueprintService().importBlueprint(connection,bpfile, bpname, project)

    return getBlueprint(connection, bpname, bpstate)

def modifyCredential(connection, bpname, bpstate, credential, password):
    response = None
    blueprint = getBlueprint(connection, bpname, bpstate)

    if blueprint :
        del(blueprint.entity["status"])

        length = len(blueprint.entity["spec"]["resources"]["credential_definition_list"])
        for x in range(0, length):
           if blueprint.entity["spec"]["resources"]["credential_definition_list"][x]["name"] == credential :
              blueprint.entity["spec"]["resources"]["credential_definition_list"][x]["secret"]["value"] = password
              blueprint.entity["spec"]["resources"]["credential_definition_list"][x]["secret"]["attrs"]["is_secret_modified"] = True
              break

        response = BlueprintService().updateBlueprint(connection,blueprint)

    return response

def getApplication(connection, appname):
    application = None
    application = ApplicationService().findApplication(connection, appname)

    if application :
        application = ApplicationService().getApplication(connection, application.uuid)

    return application


def launchBlueprint(connection, bpname, bpstate, appname):

    blueprint = getBlueprint(connection, bpname, bpstate)
    if blueprint :
        response = BlueprintService().launchBlueprint(connection, blueprint, appname)

    return getApplication(connection, appname)
