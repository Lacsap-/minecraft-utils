#!/usr/bin/python3
from mcrcon import mcrcon
import sys


# Arguments check
args = sys.argv[1:]
if len(args) != 1:
  print("usage: python {0} <login_file>".format(sys.argv[0]))
  print("login file format: <host> <port> <password>")
  sys.exit(1)

with open(args[0], 'r') as login_file:
  login_info = login_file.readline().split('\n')[0].split(' ')
host, port, password = login_info
port = int(port)

rcon = mcrcon.MCRcon()
rcon.connect(host, port)
rcon.login(password)

hour_dic = {0:6, 1:7, 2:8, 3:9, 4:10, 5:11, 6:12, 7:13, 8:14, 9:15, 10:16,
            11:17, 12:18, 13:19, 14:20, 15:21, 16:22, 17:23, 18:0, 19:1, 20:2,
            21:3, 22:4, 23:5}

daytime = rcon.command("time query daytime").split(' ')[-1]
hour = hour_dic[int(int(daytime) / 1000)]
minute = int(int(daytime) % 1000 / 17)

print("{0}:{1}".format(hour, minute))

rcon.disconnect()

