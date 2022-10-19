import sys
import nclib
from PIL import Image
sys.path.append('/home/pi/Desktop/csaw_esc_2022/communication_framework')
from main import get_server_access_key

def gen_input():
  file_name = input('Enter the filename of the JPG image: ')
  try:  
    img = Image.open(file_name)
    new_dim = (300,300) # Server expects a 300x300 image
    img = img.resize(new_dim)
    img_bytes = img.tobytes("raw", "RGB")
    img.close()
    return img_bytes
  except:
    print('Invalid image!')

# Get token required to talk to server (must run on provided RPi VM)
get_server_access_key()
server_access_key = input('Enter server access key:')

# Connect to server over netcat
nc = nclib.Netcat(connect=('18.224.4.51', 3004))

print("Msg:", nc.recv().decode())

# Send token to server 
server_access_key += '\n'
nc.send(server_access_key.encode())

print("Sent Access Key")
access = nc.recv().decode()
print(access)
if not 'granted' in access:
	print('Verification failed')
	sys.exit(-1)

# Convert JPG image to bytes to send to server
input_image = gen_input()
print("Size of bytes:", len(input_image))
# Send JPG 
nc.send(input_image)
print("Sent JPG")

c = nc.recv().decode()
while 'white-glass' not in c:
	print(c)
	c = nc.recv().decode()
print(c)
