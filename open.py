'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
12/20/17
Mr. Davis
Door Security
'''

import socket                                         
import time
from datetime import datetime

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "127.0.0.1"
host_str = host + "\r\n"

port = 9999                                           
port_str = str(port) + "\r\n"

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Door opened "+str(datetime.now()))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(host_str.encode('ascii')+port_str.encode('ascii')+currentTime.encode('ascii'))
    clientsocket.close()

    file = open("door_opened.txt", "w")
    file.write("Door opened "+str(datetime.now()))
    file.close()
    
