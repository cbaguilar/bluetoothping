import csv
import subprocess
import re

FILENAME = raw_input("What antenna are you testing? ")
DEGREES = raw_input("How many degrees will you test?")
ADDRESS = raw_input("fc:58:fa:13:2f:b8")

file = []
for x in range(0,5):
	try:
		ping = subprocess.check_output(['hcitool','rssi', 'fc:58:fa:13:2f:b8'])
		print("Pinging...")
	except Exception:
		ping = "time err"
		print("could not connect")
	values = re.findall(r'value: (\d+\.\d+)', ping)
	file.append(x*30)
	file.append(values)
	raw_input("please turn "+ str(30*x)+ " and press enter")
print(file)


with open(FILENAME, 'wb') as outcsv:
	writer = csv.writer(outcsv)
	writer.writerows(file)
subprocess.call(['chown','christian',FILENAME])
