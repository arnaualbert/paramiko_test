import paramiko
host = input("Enter the host ip: ")
username = input("Username: ")
password = input("Password: ")
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
command = "pwd"
while command != "exit":
    command = input("Enter the command: ")
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
