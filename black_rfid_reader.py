from keyboard_alike import reader
import sys
import httplib, urllib

# *****Config******
# Ouput of `dmesg | tail` after plugging the device
VENDOR_ID = 0x08ff
PRODUCT_ID = 0x0009
DATA_SIZE = 80
CHUNK_SIZE = 8
DEBUG = False
# *****Config******

# LOG=sys.stderr.write

class RFIDReader(reader.Reader):
    """
    This class supports common black RFID Readers for 125 kHz read only tokens
    http://www.dx.com/p/intelligent-id-card-usb-reader-174455
    """
    def __init__(self):
        super(RFIDReader,self).__init__(VENDOR_ID, PRODUCT_ID, DATA_SIZE, CHUNK_SIZE, should_reset=False, debug=DEBUG)


if __name__ == "__main__":
    reader = RFIDReader()
    reader.initialize()
    while True:
        try:
            print('Waiting...') 
            data = reader.read().strip()
            print('RFID: %s' % data)

            print('HTTP Request...')
            params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0, 'data': data})
            headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("www.mysite.com:80")
            conn.request("POST", "/query", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            dataHTTP = response.read()
            conn.close()
        except KeyboardInterrupt:
            print("\n\nBye Bye")
            #reader.disconnect()
            sys.exit()
