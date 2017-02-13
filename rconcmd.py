#!/usr/bin/python3
from mcrcon import mcrcon
import sys


# Arguments check
args = sys.argv[1:]
if len(args) != 2:
  print("usage: python rconcmd.py <login_file> <command>")
  print("login file format: <host> <port> <password>")
  sys.exit(1)

with open(args[0], 'r') as login_file:
  login_info = login_file.readline().split('\n')[0].split(' ')
host, port, password = login_info
port = int(port)

rcon = mcrcon.MCRcon()

rcon.connect(host, port)
rcon.login(password)

response = rcon.command(args[1])
print(response)

rcon.disconnect()
