import paramiko

host = "host"
port = "port"
username = "username"

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(hostname=host, port=port, username=username)

stdin, stdout, stderr = sshClient.exec_command("who | wc -l")
lines = stdout.readlines()

for line in lines:
    print(line, end="")
