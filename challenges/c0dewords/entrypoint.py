from main import get_server_access_key
import nclib

def gen_input():
  file_name = input('Enter the filename of the CSV: ')
  try:
    csv_file = open(file_name, 'rb')
    return csv_file.read().hex()
    csv_file.close()
  except:
    print('Invalid CSV file!')

# Get token required to talk to server (must run on provided RPi VM)
get_server_access_key()
server_access_key = input('Enter server access key:')

# Convert CSV file to hex string to send to server
weight_indices = gen_input()

# Connect to server over netcat
nc = nclib.Netcat(connect=('18.224.4.51', 3007))

print("Msg:", nc.recv().decode())

# Send token to server 
server_access_key += '\n'
nc.send(server_access_key.encode())

print("Sent Access Key")
print(nc.recv().decode())

# Send CSV input
weight_indices += '\n'
print("Csv Gen", len(weight_indices))
nc.send(str(weight_indices).encode())
print("Sent CSV")

c = nc.recvall().decode()

while 'Decode' not in c:
	if len(c) > 1:
		print(c)
	c = nc.recv().decode()
print(c)
print("Done")
