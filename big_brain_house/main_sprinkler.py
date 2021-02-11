from objects.lamp import Lamp

luzinha = Lamp(False)
addr = luzinha.get_addr_by_mult()
socket = luzinha.connect_tcp(addr)
msg = 'Oi'
luzinha.write(socket, msg)
luzinha.receive(socket)


