#!/usr/bin/env Python
"""
- Obtener información del equipo: ]3/\|)´|+|><. 
"""
import socket
import uuid
import msvcrt
from netifaces import interfaces, ifaddresses, AF_INET

def obtener_info_equipo():
	nombre_equipo = socket.gethostname()
	direccion_equipo = socket.gethostbyname(nombre_equipo)
	print("\nHOST: \t%s\n" % nombre_equipo)
	#print("IP: %s" % direccion_equipo)
	print("MAC: \t", end="") 
	print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
	for ele in range(0,8*6,8)][::-1]))
	print("\nIP's: ")
	""" Get all IPv4 addresses for all interfaces. """
	try:
		# to not take into account loopback addresses (no interest here)
		for interface in interfaces():
			config = ifaddresses(interface)
			# AF_INET is not always present
			if AF_INET in config.keys():
				for link in config[AF_INET]:
					# loopback holds a 'peer' instead of a 'broadcast' address
					if 'addr' in link.keys() and 'peer' not in link.keys():
						#addresses.append(link['addr']) 
						print('\t'+link['addr'])
		#return addresses
	except ImportError:
		print("Error ---") 

if __name__ == '__main__':
	print("INFORMACION DE HOST | v0.0.0.1")
	obtener_info_equipo()
	msvcrt.getch()
