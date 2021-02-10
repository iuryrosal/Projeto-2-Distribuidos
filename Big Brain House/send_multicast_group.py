import socket
import struct
import sys

def send_multicast(message):
    multicast_group = ('224.3.29.71', 10000)

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(0.2)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        # Send data to the multicast group
        print('sending "%s"' %message)
        message = message.encode('UTF-8')
        sock.sendto(message, multicast_group)

    finally:
        print('closing socket')
        sock.close()

message = 'Oiiiiiiiiiiiiiiiiiiiiiiiiiii'
send_multicast(message)