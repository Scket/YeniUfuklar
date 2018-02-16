import serial.tools.list_ports
connected_list = []
empty_list = []
try:
	print("[INFO] Waiting for ports")
	for port in list(serial.tools.list_ports.comports()):
		if not port[2] == 'n/a' : empty_list.append(port)
	_ = raw_input("[Plug into your device and press Enter")
	for port in list(serial.tools.list_ports.comports()):
		if not port[2] == 'n/a' : connected_list.append(port)
	for port in range(len(empty_list)):
		connected_list.remove(empty_list[port])
	device = connected_list[0]
	print "[INFO] Your Device Port : " + device[0]
	print "[INFO] Port Name : " + device[1]
	print "[INFO] Device PID and SNR : " +device[2]
except:
	print "[ERROR] Please be sure unplugged your device and try again"	
