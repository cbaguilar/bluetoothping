import csv
import subprocess
import re
import time

FILENAME = raw_input("What antenna are you testing? ")
#DEGREES = raw_input("How many degrees will you test?")
#ADDRESS = raw_input("fc:58:fa:13:2f:b8")

INTERVAL = 15


file = []
for x in range(0,360/INTERVAL):
	raw_input("please turn " +str(x*INTERVAL)+"degrees")
	row = []
	row.append(x*INTERVAL)
	try:
	 for y in range (0,3):
		ping = subprocess.check_output(['hcitool','rssi', 'fc:58:fa:13:2f:b8'])
		print("Pinging...")
		values = ping.split(': ')[1].rstrip()
		row.append(values)
		time.sleep(0.1)
	 file.append(row)
	except Exception:
		print("failed")
print(file)


with open(FILENAME, 'wb') as outcsv:
	writer = csv.writer(outcsv)
	writer.writerows(file)
#subprocess.call(['chown','christian',FILENAME])
