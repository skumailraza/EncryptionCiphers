from socket import*

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))) 

I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ")) 

def encode(plaintext, key): 
	ciphertext = ""
	for c in plaintext.upper():
		if c.isalpha(): 
			ciphertext += I2L[ (L2I[c] + key)%26]
		else: 
			ciphertext += c
	return ciphertext

def decode(ciphertext, key): 
	plaintext2 = ""
	for c in ciphertext.upper():
		if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
	else: 
		plaintext2 += c 
	return plaintext2

def main():
	message = raw_input('Write your message here: ')
	u_key = raw_input('Input key: ')
	ctext = encode(message, u_key)
	print('Cipher Text: ')
	print(ctext)

	ptext = decode(ctext, u_key)

	print('Decoded Plaintext: ')
	print(ptext)

if __name__ == "__main__": main()

