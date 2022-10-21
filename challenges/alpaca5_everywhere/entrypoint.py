import sys
import nclib
sys.path.append('/home/pi/Desktop/csaw_esc_2022/communication_framework')
from main import get_server_access_key

def gen_input():
  file_name = input('Enter the filename of the JPG image: ')
  img_bytes_f = open(file_name, "rb")
  img_bytes = img_bytes_f.read()
  img_bytes_f.close()
  return img_bytes.hex()

# Get token required to talk to server (must run on provided RPi VM)
get_server_access_key()
server_access_key = input('Enter server access key:')

# Connect to server over netcat
nc = nclib.Netcat(connect=('18.224.4.51', 3005))

# Send token to server 
server_access_key += '\n'
nc.send(server_access_key.encode())

print("Sent Access Key")
nc.recv().decode()
access = nc.recv().decode()
print(access)
if not 'granted' in access:
	print('Verification failed')
	sys.exit(-1)

# Convert JPG image to bytes to send to server
input_image = gen_input()

# Send JPG 
nc.send(input_image + "\n")
print("Sent JPG")

c = nc.recv().decode()
while 'Finished!' not in c:
	print(c)
	c = nc.recv().decode()
print(c)
