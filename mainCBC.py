import pyaes
import os
import logging
import csv

logging.basicConfig(filename='example.log',level=logging.DEBUG)


with open('key.csv', newline='') as csvfile:
	logging.info("Opening KEY CSV File")
	keys = csv.DictReader(csvfile)
	for row in keys:
		print(row['id'], row['key'], row['iv'])

		
def get_key(id):
	global keys
	logging.info("Get KEY from CSV File")
	
	#print(keys.get('id'))

# A 256 bit (32 byte) key
key = "This_key_for_demo_purposes_only!"
# Convert str to byte object
key = key.encode('utf-8')


get_key(2)

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = "InitializationVe"
iv = iv.encode('utf-8')


aes = pyaes.AESModeOfOperationOFB(key, iv = iv)
plaintext = "Text may be any length you wish, no padding is required"
ciphertext = aes.encrypt(plaintext)

#repr(ciphertext)
logging.info(ciphertext)
print(ciphertext)

# The counter mode of operation maintains state, so decryption requires
# a new instance be created
#aes = pyaes.AESModeOfOperationCTR(key)
#aes = pyaes.AESModeOfOperationCFB(key, iv = iv, segment_size = 8)
aes = pyaes.AESModeOfOperationOFB(key, iv = iv)
decrypted = aes.decrypt(ciphertext)
logging.info("Dedecrypted Message: %s",decrypted)
# True
if decrypted == plaintext:
	
	print(decrypted == plaintext)

# To use a custom initial value
counter = pyaes.Counter(initial_value = 100)
aes = pyaes.AESModeOfOperationCTR(key, counter = counter)
ciphertext = aes.encrypt(plaintext)

# '''WZ\x844\x02\xbfoY\x1f\x12\xa6\xce\x03\x82Ei)\xf6\x97mX\x86\xe3\x9d
#    _1\xdd\xbd\x87\xb5\xccEM_4\x01$\xa6\x81\x0b\xd5\x04\xd7Al\x07\xe5
#    \xb2\x0e\\\x0f\x00\x13,\x07'''
#print repr(ciphertext)