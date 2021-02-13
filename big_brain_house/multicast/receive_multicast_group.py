import socket
import struct
import sys

def receive_multicast():
    multicast_group = '224.3.29.71'
    server_address = ('', 10000)

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Bind to the server address
    sock.bind(server_address)

    # Receive/respond loop
    while True:
        print('\nwaiting to receive message by multicast\n')
        data, address = sock.recvfrom(1024)
        
        print('received %s bytes from %s\n' % (len(data), address))

        if data != None:
            return data