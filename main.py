from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import random
#以上 RSA所需模組
import threading #多執行緒模組

def mainProcess(): #產生RSA密鑰，並檢查密鑰內是否具備某字串
    times = 0
    flag = 1 
    while(flag):
        rsa = RSA.generate(1024) #產生RSA1024
        #print(rsa.exportKey()[0:100])
        if name in rsa.exportKey(): #如果產生之RSA PivateKey不符合要求則重新產生RSA
            flag = 0 #條件符合，稍後退出迴圈
            private_pem = rsa.exportKey() 
            public_pem = rsa.publickey().exportKey() #如果條件符合，則獲取該次RSA密鑰
            print(private_pem + "\r\n" + public_pem)
            fo.write(private_pem.decode("utf-8") + "\r\n" + public_pem.decode("utf-8"))
            #匯出符合條件之密鑰至純文字檔案
            fo.close()
            os._exit()
            
fo = open("test.txt", "w")
name = "MoriKamiya"
name = str.encode(name)
print(name)

#Intel Core i7 6700K have 8 Thread with Hyper-Threadding
t1 = threading.Thread(target = mainProcess) 
t2 = threading.Thread(target = mainProcess)
t3 = threading.Thread(target = mainProcess)
t4 = threading.Thread(target = mainProcess)
t5 = threading.Thread(target = mainProcess)
t6 = threading.Thread(target = mainProcess)
t7 = threading.Thread(target = mainProcess)
t8 = threading.Thread(target = mainProcess)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

