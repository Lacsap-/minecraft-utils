#!/usr/bin/python3
from mcrcon import mcrcon
import os
import sys


# Arguments check
args = sys.argv[1:]
if len(args) != 1:
  print("usage: python rconcmd.py <command>")
  sys.exit(1)

with open(os.path.expanduser('~/.mcscript/rcon'), 'r') as login_file:
  login_info = login_file.readline().split('\n')[0].split(' ')
host, port, password = login_info
port = int(port)

rcon = mcrcon.MCRcon()

rcon.connect(host, port)
rcon.login(password)

response = rcon.command(args[0])
print(response)

rcon.disconnect()
