import paramiko
from datetime import datetime
from time import sleep

host = '192.168.5.1'
user = 'admin'
secret = 'password'
port = 22
command = 'show ipsec'
encoding = 'utf-8'
while True:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command(command)
    data = stdout.read() + stderr.read()
    client.close()
    with open('/home/vladimir/data.txt', 'a') as file_data:
        data_time = str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        print('Файл Обновлён '+ data_time)
        file_data.write(str('Файл Обновлён' )+ data_time + '\n')
        file_data.write(data.decode(encoding) + '\n')
    sleep(5)
