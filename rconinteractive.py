#!/usr/bin/python3

from mcrcon import mcrcon
import os
import sys


with open(os.path.expanduser('~/.mcscript/rcon'), 'r') as login_file:
  login_info = login_file.readline().split('\n')[0].split(' ')
host, port, password = login_info
port = int(port)


rcon = mcrcon.MCRcon()

print("# connecting to %s:%i..." % (host, port))
rcon.connect(host, port)

print("# logging in...")
rcon.login(password)

print("# ready")

try:
  while True:
    response = rcon.command(input('> '))
    if response:
      print("  %s" % response)

except KeyboardInterrupt:
  print("\n# disconnecting...")
  rcon.disconnect()
