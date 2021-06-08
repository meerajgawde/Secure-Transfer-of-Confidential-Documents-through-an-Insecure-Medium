import base64
from cryptography.fernet import Fernet


#convert image into binary

with open("image2.png", "rb") as original_file:
    encoded_string = base64.b64encode(original_file.read())
print(encoded_string)
sample= encoded_string.decode("utf-8")
file= open('base.txt',"w")
file.write(sample)
file.close

#Making a key using AES
key = Fernet.generate_key()
file = open('key.key','wb')
file.write(key)
file.close()

#Encrypting base.txt (image_base64) using the AES key
file = open('key.key','rb')
key = file.read()
file.close

with open('base.txt','rb') as f:
    data=f.read()
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('test.txt.encrypted','wb') as f:
    f.write(encrypted)

