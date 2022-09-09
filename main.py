import sys
import socket
from termcolor import cprint

target = ''
if len(sys.argv) > 1:
    target = socket.gethostbyname(sys.argv[2])
else:
    print("Usage : python3 main.py <url> <first-port> <second-port> <timeout>")


print("-" * 50)
print("Website scanned: " + target)
print("IP address of the website: " + sys.argv[2])
print("-" * 50)

list = []

try:
    for port in range(sys.argv[3], sys.argv[4]):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(sys.argv[5])
        result = s.connect_ex((target, port))
        if result == 0:
            cprint("Port {} is open".format(port), "green")
            list.append(port)
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
except socket.error:
    print("\ Server not responding !!!!")
finally:
    def print_list():
        print("Open ports: " + str(list))
    print_list()
    sys.exit()
