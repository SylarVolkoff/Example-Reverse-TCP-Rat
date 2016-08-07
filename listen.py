#/usr/bin/python env
# Built for python 2 and 3
import socket
from sys import version

# Python version compatiablity issues - fucking backwards compatiablity
# So to solve this, we monkey patch it.
# Since function names are variables, resign the function name to input if python 2
if version[0] == 2:
    input = raw_input
else: input = input

PORT = 4444

# Incase there's nothing to be sent back
noShow = '__NO_INFO__'

# Start TCP Port, with Keep-Alive-Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Port to our machine
# argv[1] = our port number
try:
    s.bind(('', int(argv[1])))
    # Listen for x amount of clients - in this case 1 since we're not doing a multi-server
    s.listen(1)
except socket.error as msg:
    # Incase of failure
    print('Bind failed. Error Code: ' + str(msg))
    # Exit program
    exit()

# Server is running now
print('Socket now listening')

# Forever wait  until you recieve a connection
while 1:
    # wait to accept a connection - blocking the rest of our code
    conn, addr = s.accept() # This is padded already, - so we leave it alone

    # We got a connection! addr[0] = IP, addr[1] = Relocated port
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    # While we're connected connected
    while conn:
        # Time to send input
        conn.sendall(input(addr[0]+'$> ').encode())

        # We're always expecting a response, this will hang up our code if we don't get one
        data = conn.recv(2048).decode()
        # So we decide if the response should be shown
        if not data == noShow:
            # If it's not our "noShow" data, then we print it so the user can see it
            print(data)

s.close()