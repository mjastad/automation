#!/usr/bin/env python

"""
File: Main.py: NTNX REST API Driver.
"""

from core.Connection import Connection
from core.Host import Host
from core.User import User
from services.VirtualMachineService import VirtualMachineService

__author__ = "M. Jastad"
__copyright__ = "Copyright 2017, CSRA Hackathon"
__credits__ = ["Roger Gibson", "Dan Fallon"]
__license__ = "N/A"
__version__ = "1.0.1"
__maintainer__ = "M. Jastad"
__email__ = "michael.jastad@nutanix.com"
__status__ = "Reference"

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
