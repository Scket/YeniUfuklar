import serial.tools.list_ports
flag = False
#device_ID = 'USB VID:PID=2341:0042 SNR=81231233631351A002F1' //  MY Arduino
#device_ID = 'USB VID:PID=10c4:ea60 SNR=0121'			// RP Lidar
def Controller(device_ID):
	try:
		for p in list(serial.tools.list_ports.comports()):
		    if not p[2] == 'n/a' and p[2] == device_ID : flag = True
		if flag == True:
			return p[0]
	except:
		print "[ERROR] Devices not found"

if __name__ == '__main__':
	try:
		Controller()
	except:
		print "This code must be start in another code"

