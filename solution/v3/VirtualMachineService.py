from v3.model.Task import Task
from v3.model.VirtualMachine import VirtualMachine


class VirtualMachineService:

    def __init__(self):
        self.RESOURCE_VM = '/vms/'
        self.RESOURCE_VM_PWR_STATE = '/set_power_state/'

    def createVM(self, conn, data):
        pass

    def getVM(self, conn, uuid):
        vmDictionary = conn.get(self.RESOURCE_VM + uuid)
        return VirtualMachine(vmDictionary)

    def getVMS(self, conn, data):
        vmList = []
        vmDictionary = conn.post(self.RESOURCE_VM+'list', data)
        for vm in vmDictionary['entities']:
             vmList.append(VirtualMachine(vm))

        return vmList

    def deleteVM(self, conn, vm):
        task_dictionary = conn.delete(self.RESOURCE_VM + vm.uuid)
        return Task(task_dictionary)

    def updateVM(self, conn, vm, data):
        task_dictionary = conn.put(self.RESOURCE_VM + vm.uuid, data)
        return Task(task_dictionary)

    def powerOn(self, conn, vm):
        data = {'transition': 'ON', 'uuid': vm.uuid}
        task_dictionary = conn.post(self.RESOURCE_VM + vm.uuid + self.RESOURCE_VM_PWR_STATE, data)
        return Task(task_dictionary)

    def powerOff(self, conn, vm):
        data = {'transition': 'OFF', 'uuid': vm.uuid }
        task_dictionary = conn.post(self.RESOURCE_VM + vm.uuid + self.RESOURCE_VM_PWR_STATE, data)
        return Task(task_dictionary)

    def find(self, conn, id):
        vmList = self.getVMS(conn)
        for vm in vmList :
            if id == vm.name : return vm

        return None
