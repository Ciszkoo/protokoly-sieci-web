import paramiko

host = "host"
port = "port"
username = "username"

ssh = paramiko.SSHClient()
key = paramiko.Ed25519Key.from_private_key_file("path/to/key")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, pkey=key)

path = input("Enter path: ")

stdin, stdout, stderr = ssh.exec_command("cat " + path)
lines = stdout.readlines()

if len(lines) == 0:
    print("File not found")
else:
    for line in lines:
        print(line, end="")
