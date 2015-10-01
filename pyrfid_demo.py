#!/usr/bin/python3

from keyboard_alike import reader
import sys
import RPi.GPIO as GPIO
import time
import http.client, urllib

# *****Config******
# Ouput of `dmesg | tail` after plugging the device
VENDOR_ID = 0x08ff
PRODUCT_ID = 0x0009
DATA_SIZE = 80
CHUNK_SIZE = 8
DEBUG = False

RELAY_PIN_LIST = [24]
RELAY_SLEEP_TIME = 0.5
# *****Config******

# LOG=sys.stderr.write

class RFIDReader(reader.Reader):
	"""
		This class supports common black RFID Readers for 125 kHz read only tokens
		http://www.dx.com/p/intelligent-id-card-usb-reader-174455
		"""
	def __init__(self):
		super(RFIDReader,self).__init__(VENDOR_ID, PRODUCT_ID, DATA_SIZE, CHUNK_SIZE, should_reset=False, debug=DEBUG)


class Relay():
	# time to sleep between operations in the main loop
	sleepTimeS = 0.5
		
	# init list with pin numbers
	pinList = [24]
	
	def __init__(self, pinList = [24], sleepTimeS = 0.5):
		self.sleepTimeS = sleepTimeS
		self.pinList = pinList
		GPIO.setmode(GPIO.BCM)


	def __del__(self):
		GPIO.cleanup()
	
	
	def openRelay(self):
		# loop through pins and set mode and state to 'high'
		for i in self.pinList:
			GPIO.setup(i, GPIO.OUT)
			GPIO.output(i, GPIO.HIGH)

		for i in self.pinList:
			GPIO.output(i, GPIO.LOW)
			time.sleep(self.sleepTimeS)
		
		for i in self.pinList:
			GPIO.output(i, GPIO.HIGH)
			time.sleep(self.sleepTimeS)
		
		self.pinList.reverse()
#GPIO.cleanup()
		# find more information on this script at
		# http://youtu.be/WpM1aq4B8-A


if __name__ == "__main__":
	reader = RFIDReader()
	reader.initialize()
	relay = Relay([24], 0.5)
	while True:
		try:
			print('Waiting rfid...')
			data = reader.read().strip()
			print('RFID: %s' % data)
				
			#            print('HTTP Request...')
			#            params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0, 'data': data})
			#            headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
			#            conn = http.client.HTTPConnection("www.mysite.com:80")
			#            conn.request("POST", "/query", params, headers)
			#            response = conn.getresponse()
			#            print(response.status, response.reason)
			#            dataHTTP = response.read()
			#            conn.close()
			relay.openRelay()
		except KeyboardInterrupt:
			
				print("\n\nBye Bye")
				#reader.disconnect()
				sys.exit()
