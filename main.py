from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

fo = open("test.txt", "w")
name = "MoriKamiya"
name = str.encode(name)
print(name)
random_generator = Random.new().read
"""rsa = RSA.generate(1024, random_generator)
rsa = RSA.generate(1024, random_generator)
private_pem = rsa.exportKey()
public_pem = rsa.publickey().exportKey()
fo.write(private_pem.decode("utf-8") + "\r\n" + public_pem.decode("utf-8"))
fo.close()
"""
flag = 1
while(flag):
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()
    #print(private_pem[:50])
    if name in private_pem:
        flag = 0 
        public_pem = rsa.publickey().exportKey()
        print(private_pem)
        fo.write(private_pem.decode("utf-8") + "\r\n" + public_pem.decode("utf-8"))
        fo.close()
