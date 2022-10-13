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
exitCode = stdout.channel.recv_exit_status()

if exitCode == 0:
    lines = stdout.readlines()
    for line in lines:
        print(line, end="")
else:
    print("Error: " + str(exitCode))
