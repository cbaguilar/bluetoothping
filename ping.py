import csv
import subprocess
import re

FILENAME = raw_input("What antenna are you testing? ")
#DEGREES = raw_input("How many degrees will you test?")
#ADDRESS = raw_input("fc:58:fa:13:2f:b8")

file = []
for x in range(0,5):
	raw_input("please turn " +str(x*60)+"degrees")
	row = []
	row.append(x*60)
	for y in range (0,3):
		ping = subprocess.check_output(['hcitool','rssi', 'fc:58:fa:13:2f:b8'])
		print("Pinging...")
		values = ping.split(': ')[1].rstrip()
		row.append(values)
	file.append(row)
print(file)


with open(FILENAME, 'wb') as outcsv:
	writer = csv.writer(outcsv)
	writer.writerows(file)
#subprocess.call(['chown','christian',FILENAME])
