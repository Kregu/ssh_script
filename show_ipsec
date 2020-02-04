import paramiko
from datetime import datetime
import time
host = '192.168.5.1'
user = 'admin'
secret = 'password'
port = 22
command = 'show ipsec'
while True:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command(command)
    data = stdout.read() + stderr.read()
    client.close()
    with open('data.txt', 'ab') as file_data:
        file_data.write(data)
    with open('data.txt', 'a') as file_data:
        print('Файл Обновлён '+str(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        file_data.write(str(datetime.today().strftime("%Y-%m-%d %H:%M:%S")+str(' Обновлён')))
    time.sleep(10)
