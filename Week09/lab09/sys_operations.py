import platform
import socket
import os
print("Machine Type")
print(platform.machine())

print("Processor Type:")
print(platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout:")
print(socket.getdefaulttimeout())

print("OS Type:")
print(os.name)
print("OS Name:")
print(platform.system())

print("Current PID:")
print(os.getpid())

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print("\n[Process {os.getpid()}] Opened file_handle {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

pid = os.fork()

if pid == 0:
    print(f"[Child Process {os.getpid()}], [Parent Process {os.getppid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"[File Content] {os.read(file_handle, 100)}")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent Process {os.getpid()}], [Child Process {pid}]")
    print(f"[Parent Process {os.getpid()}] Waiting for child process to finish")
    os.wait()
    print("The child process has finished")
    file_object_TextIO.close()

    print(f"\n[Parent Process {os.getpid()}], [Child Process {pid}]")
    sys.exit(0)