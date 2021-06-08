import base64
from cryptography.fernet import Fernet

file= open('key.key','rb')
key= file.read()
file.close()

with open('test.txt.encrypted','rb') as f:
	data=f.read()

fernet=Fernet(key)
encrypted = fernet.decrypt(data)

with open('test.txt.decrypt','wb') as f:
	f.write(encrypted)


file=open('test.txt.decrypt','rb')
test_string=file.read()
file.close()

#res = ''.join(format(ord(i), 'b') for i in test_string) 

imgdata = base64.b64decode(test_string)
filename = 'some_image.png'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
	f.write(imgdata)
#fh=open('veification.png','wb')
#fh.write(base64.b64decode((res)))
#fh.close()  
# printing result  
#print("The string after binary conversion : " + str(res)) 
#print(test_string)
#print(type(test_string))
#sample=test_string.encode('UTF-8')
#sample=b(test_string)
#print(sample)
#print(type(sample))
