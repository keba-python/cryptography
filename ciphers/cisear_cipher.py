x={chr(i):i-97 for i in range(97,123)}
y={i-97:chr(i) for i in range(97,123)}

# we can easly encrypt a data using simple cisear cipher with a given data and a given specific plain text.
def encrypt(plain,key):        
    text=[x[i]+key  if x[i]+key<26
          else x[i]+key-26 for i in plain]
    encrypt=[y[i] for i in text]
    encrypt=''.join(encrypt)
    print(encrypt)
    
#to decrypt a data using a given cipher and key
def decrypt(cipher,key):
    word=[x[i]-key+26  if x[i]-key<=0 else x[i]-key for i in cipher]
    decrypt=[y[i] for i in word]
    decrypt=''.join(decrypt)
    print(decrypt)    

#to decrypt a data using brute force without any key
def decrypt_brute_force(cipher):
    word=[[y[x[i]-j+25]  if x[i]-j<=0 else y[x[i]-j] for i in cipher] for j in range(26)]
    word =[''.join(k) for k in word]
    for i in word:
        print(i)

#encrypt("hello",4)
#decrypt("khoor",3)
decrypt_brute_force("pzqaetqr")

        
        
