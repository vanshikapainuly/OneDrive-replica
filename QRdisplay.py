import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import os

PORT = 8010
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                        'OneDrive')
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #trick
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)


url = pyqrcode.create(IP)
url.svg("myqr.svg", scale=8)
webbrowser.open('myqr.svg')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
