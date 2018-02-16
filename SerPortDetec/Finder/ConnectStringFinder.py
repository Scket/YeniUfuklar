import serial.tools.list_ports
connected_list = []
empty_list = []
try:
	print("[INFO] Waiting for ports")
	for p in list(serial.tools.list_ports.comports()):
		if not p[2] == 'n/a' : empty_list.append(p)
	_ = raw_input("[Plug into your device and press Enter")

	for p in list(serial.tools.list_ports.comports()):
		if not p[2] == 'n/a' : connected_list.append(p)
	for p in range(len(empty_list)):
		connected_list.remove(empty_list[p])
	device = connected_list[0]
	print "[INFO] Your Device Port : " + device[0]
	print "[INFO] Port Name : " + device[1]
	print "[INFO] Device_ID (PID and SNR) : " +device[2]
	
except:	

	print "[ERROR] Please be sure unplugged your device and try again"	
