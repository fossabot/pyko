## Hackerman
# Author : Mrx04programmer
# Github : https://github.com/mrx04programmer
import os
import socket
from scapy.all import sniff
from scapy.all import *
from dev.colors import *

sh = os.system
s = socket.socket()

class Hackerman:
    
    def __init__(self):
        # Set Local Host
        self.lhost = '127.0.0.1'
        # Set Local Port
        self.lport = '8080'
        # Set Remote Host
        self.rhost = '1.0.0.0'
        # Set Remote Port
        self.rport = 0000
        # Set Data to send in server.
        self.DataSend = '' 
        # Set Password of Metasploit 
        self.password_metasploit = ''
        # Set Gateway IP 
        self.gateway = '192.168.0.1'
        # Set interface Wlan
        self.iface = None
        # Set Filter MITM
        self.filter = ''
        # Set FTP Port
        self.ftp_port = 21 # Default
        # Set port to use
        self.port = None # Default
    def server(self):
        s.bind(('', self.port))
        s.listen(5)
        print(f"{B} [+] {W} Server created in {self.port}")
        while True:
            # Accept all devices
            c, a = s.accept()
            print(f"{G} [+] {W} Device connected from : {a}")
            # Sending data in DataSend
            c.send(self.DataSend.encode())
            # Close connection
            c.close()
    def connect(self):
        rport = int(rport)
        rhost = str(rhost)
        if self.rhost == '1.0.0.0' or self.rport == 0000:
            print(f" {R}[-] {W} RHOST and RPORT not found.")
        else:
            try:
                hostname = socket.gethostbyname(self.rhost)
                print(f"{G}[INFO] {W} Connected with {self.rhost}:{self.rport}")
            except socket.gaierror:
                print(f"{R}[-] {W} Error to resolving the host")
                exit()

            # Connect to server or host.
            s.connect((str(self.rhost), int(self.rport)))
    
    def sniffer(self, method, iface, limit):
        iface = self.iface
        if limit != None:
            limit = int(limit)
        if method == 'general':
            if iface:
                capture = sniff(iface=iface)
                print(f"{O}[SET] {W} Interface -> {iface}")
            elif limit and iface:
                capture = sniff(iface=iface, count=limit)
            elif limit:
                capture = sniff(count=limit)
                print(f"{O}[SET] {W} Limit -> {limit}")
            else:
                capture = sniff()
            print(f"{G}[INFO] {W}Listening traffic...")
            capture.summary()

        if method == 'port':
            capture = sniff(filter='port %s' % (self.port))
            print(f"{G}[INFO] {W} Listening in the port {self.port}...")
            capture.summary()
        if method == 'ftp':
            print(f"{G}[INFO] {W} Listening in the Protocol FTP ...")
            def r(packet):
                if packet[TCP].dport == self.ftp_port:
                    data = packet.sprintf("%Raw.load%") # Access to data of ftp traffic
                    if "USER" in data:
                        print(f"{G} Connection from {packet[IP].src} <--> {packet[IP].dst}")
                        data = data.split(" ") 
                        data = data[1]
                        print(f"{G} Possible User -> {data}")
                    elif "PASS" in data:
                        data = data.split(" ") 
                        data = data[1]
                        print(f"{G} Possible Password -> {data}")
            if iface:
                capture = sniff(filter="port %s" % (self.ftp_port),iface=iface, prn=r)
                print(f"{O}[SET] {W} Interface -> {iface}")
            else:
                capture = sniff(filter="port %s" % (self.ftp_port), prn=r)
            capture.summary()

        if method == 'tcp':
            if iface:
                capture = sniff(filter='tcp', iface=iface)
                print(f"\n{O}[SET] {W} Interface -> {iface}")
            elif limit and iface:
                capture = sniff(filter='tcp', iface=iface, count=limit)
            elif limit:
                capture = sniff(filter='tcp', count=limit)
                print(f"{O}[SET] {W} Limit -> {limit}")
            else:
                print(f"{G}[INFO] {W}Listening Protocol TCP...Ctrl+C for Finish")
                capture = sniff(filter='tcp')
            capture.summary()
    def read_cap(self, file):
        file = str(file) # Example of file: captures.pcap
        print(f"{O}[READ] {W} FilePath -> {file}")
        print(f"{G}[INFO] {W} Showing content... \n{O}")
        read = sniff(offline=file) #prn=lambda x:x.summary()
        read.summary()