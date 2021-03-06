#!/usr/bin/env python
import socket

if __name__ == '__main__':
	try:
		target = raw_input('Enter host to scan: ')
		targetIP = socket.gethostbyname(target)
	except socket.gaierror, err:
		print "cannot resolve hostname: ", target, err
		exit()
	
	print 'Starting scan on host ', targetIP
	array = ['21','22','25','80','443','139','3389','1723','1521','23','110', '996', '445','8080','5900','1433','3306','143','993']
	arrayname = ['FTP','SSH','SMTP','HTTP','HTTPS','NETBIOS','RDP','VPN','Oracle DB','TELNET','POP3','POP3SSL','Windows file Sharing','firewall','VNC','MSQL','Mysql','IMAP','IMAPSSL']
	#scan reserved ports
	for i in range(0,len(array)):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		result = s.connect_ex((targetIP, int(array[i])))
		if(result == 0) :
			print "Port", array[i], arrayname[i], "OPEN"
		else:
			print "Port", array[i], arrayname[i], "CLOSE"
        	s.close()

