
import string
import random

def radonstring_generator(size=6, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for Y in range(size))

def randomemail_generator(size=8, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

text=radonstring_generator()
email=randomemail_generator() + "@gmail.com"
print(email,'and text is', text)

