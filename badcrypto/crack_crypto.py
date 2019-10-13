# from pwn import *
import base64

def rotate_right(n, times):
	return ((n >> times) | (n << (8 - times))) & 0xff

# conn = remote("192.35.222.199",1338)
# conn.recvuntil(", named \'")
# file_name = conn.recvuntil(".txt", drop=True)
# conn.recvuntil("----- Begin of File ------\n")
# base64encoded = conn.recvuntil("\n----- End of File ------",drop=True)
file_name = raw_input()
base64encoded = raw_input()
decoded = base64.b64decode(base64encoded)

#magic_num_first_byte = 0x1f
rotation = -1
for i in range(0,8):
	# print(i)
	# print(hex(ord(decoded[0])))
	# print(hex(ord(decoded[15])))
	# print(hex(rotate_right(0x1f, i)))
	# print(hex(ord(decoded[15]) ^ (ord(decoded[0]) ^ rotate_right(0x1f, i))))
	# print(hex(ord(file_name[5])))
	# print(hex(rotate_right(ord(file_name[5]), i)))
	if ((ord(decoded[15]) ^ (ord(decoded[0]) ^ rotate_right(0x1f, i)))
		== rotate_right(ord(file_name[5]), i)):
		rotation = i
		break

# print(rotation)

encr_file_name = decoded[10:25]
key = [None] * 15
for i in range(0,15):
	# print(i)
	key[(i + 10)%15] = rotate_right(ord(file_name[i]), rotation)^ord(encr_file_name[i])

# for a in key:
# 	print(chr(a))

decr = []
file = open(file_name+'.txt.gz', 'w+')
for i in range(0,len(decoded)):
	decr.append(rotate_right(ord(decoded[i]) ^ key[i % 15],8 - rotation))
	file.write(chr(decr[i]))
file.close()
