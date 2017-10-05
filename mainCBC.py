import pyaes
import os
import logging
import csv

keys_list = {}
logging.basicConfig(filename='example.log',level=logging.DEBUG)

'''
with open('key.csv', newline='') as csvfile:
	logging.info("Opening KEY CSV File")
	keys = csv.DictReader(csvfile)
	for row in keys:
		print(row['id'], row['key'], row['iv'])
'''
		
def load_keys():
	logging.info(load_keys)
	with open('key.csv', 'r') as f:
		reader = csv.reader(f)
		#your_list = list(reader)
		keys_list = map(tuple, reader)
		
		data=[tuple(line) for line in csv.reader(f)]
		
		logging.info("key list")
		logging.info(keys_list)

def filter_value( someList, value ):
	result = next((i for i, v in enumerate(someList) if v[0] == 2), None)
	print(result)

	logging.info("filter_value for: %s", value)
			
def get_key(id):
	result= list( filter_value( keys_list, "2" ) )
	logging.info("Get KEY from List: %s", result)
	print(id)
	print(result)


load_keys()
result = next((i for i, v in enumerate(keys_list) if v[0] == "2"), None)
print("result:") 
print(result)
print(keys_list)

#get_key('2')


# A 256 bit (32 byte) key
key = "This_key_for_demo_purposes_only!"
# Convert str to byte object
key = key.encode('utf-8')




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