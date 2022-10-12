import paramiko

host = "host"
port = "port"
username = "username"

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(hostname=host, port=port, username=username)

path = input("Enter path: ")

stdin, stdout, stderr = sshClient.exec_command("cat " + path)
lines = stdout.readlines()
err = stderr.readlines()

if len(err) != 0:
    print("File not found")
else:
    for line in lines:
        print(line, end="")
