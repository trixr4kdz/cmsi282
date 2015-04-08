def encrypt (key, plaintext):
	return process(key, plaintext, 1)

def decrypt (key, ciphertext):
	return process(key, ciphertext, -1)

def process(key, text, sign):
	if key is "":
		raise ValueError ("Cannot use empty key")
	else:
		uppercase_key = key.replace(' ', '').upper()
		uppercase_text = text.replace(' ', '').upper()
		if sign == 1:
			length = len(uppercase_text)
			actual_key = str(uppercase_key) + str(uppercase_text)
			actual_key = actual_key[0:length]
		else:
			actual_key = uppercase_key

		char_in_text = []
		extend = (ord('Z') + 1)
		j = 0

		for i, char in enumerate(uppercase_text):

			if (sign == -1):
				extend = 0
				if (i >= len(key)):
					actual_key += (char_in_text[j])
					j += 1
					
			position = (ord(char) + extend + (sign * ord(actual_key[i]))) % (ord('Z') + 1)
			if (position < ord('A')):
				position += (extend - (sign * ord('A')))
			char_in_text.append(chr(position))

		result = ''.join(char_in_text)
	return result