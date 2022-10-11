import time
import ntplib
import os

def synctime():
  try:
    print('The current system time is:')
    print(str(os.popen('TZ=\'UTC\' date').read()))
    client = ntplib.NTPClient()
    response = client.request('time.google.com')
    newtime = time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time))
    os.system('sudo date ' + newtime)
    print('Updating system time... New system time is:')
    print(str(os.popen('date').read()))
  except:
    print('Could not sync with time server.')


def main():
  i = input('Update system time? [y/N]: ')
  if (i=='y' or i=='Y'):
    synctime()

main()
