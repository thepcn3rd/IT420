#!/usr/bin/python3

# Built to encrypt the communication between the download cradle and where these files are hosted

# Create a pem file
# openssl req -new -x509 -keyout my.pem -out my.pem -days 365 -nodes

import http.server
import ssl
import os

server_address = ('172.31.1.10', 8090)
server_directory = "/work/pwsh/outputEncrypted"

# Change Directory to what needs to be served
os.chdir(server_directory)

# Check if the index.html file exists if not create
if not os.path.exists('index.html'):
    fileLocation = server_directory + "/index.html"
    f = open(fileLocation, 'w')
    f.write(" ")
    f.close()

h = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
h.socket = ssl.wrap_socket(h.socket, server_side=True, certfile='/work/pwsh/my.pem', ssl_version=ssl.PROTOCOL_TLSv1_2)
h.serve_forever()
