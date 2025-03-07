import platform
import socket
print("Machine Type")
print(platform.machine())

print("Processor Type:")
print(platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout:")
print(socket.getdefaulttimeout())