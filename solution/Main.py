'''
@file: Main.py
@author: M.Jastad
'''
from core.Connection import Connection
from core.Host import Host
from core.User import User
from services.VirtualMachineService import VirtualMachineService

USER = "admin"
PASSWD = "passw0rd"
IPADDRESS = "10.68.69.102"
PORT = "9440"


def main():

    user = User(USER, PASSWD)
    host = Host(IPADDRESS, PORT)
    connection = Connection(user, host)

    vmService = VirtualMachineService()
    vmList = vmService.getVMS(connection)

    for vm in vmList : print vm.name


if __name__ == "__main__":
    main()
