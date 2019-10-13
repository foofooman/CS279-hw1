import socket
import time
import base64
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ts = int(time.time())
s.connect(("192.35.222.199",1340))
a = s.recv(1024)
encoded = str(a[405:])[2:-39]
print(encoded)
decoded = base64.b64decode(encoded)
print(len(decoded))
random.seed(ts)
decrypted = ""
for c in decoded:
	r = random.randint(0,255) ^ c
	decrypted = decrypted + chr(r)

decrypted = decrypted + '\n\n'
s.send(bytes(decrypted, 'utf-8'))
print(decrypted)
print(s.recv(1024))