alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_alpha_letters = 26

def encrypt (orig_key, plaintext):
	uppercase_key = orig_key.upper()
	uppercase_plaintext = plaintext.replace(' ', '').upper()
	length = len(uppercase_plaintext)
	actual_key = str(uppercase_key) + str(uppercase_plaintext)
	actual_key = actual_key[0:length]

	encrypted_char = []
	for i, char in enumerate(uppercase_plaintext):
		encrypted_char.append (alpha_list[( alpha_list.index(char) + alpha_list.index(actual_key[i]) ) % num_alpha_letters])
	result = ''.join(encrypted_char)

	print result

encrypt('quark', 'TAKE A COPY OFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR'.lower())