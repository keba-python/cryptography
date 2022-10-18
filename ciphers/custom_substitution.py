import random
import numpy as np

x={chr(i):i-97 for i in range(97,123)}
y={i-97:chr(i) for i in range(97,123)}
n={chr(i):i-33 for i in range(33,127)}
m={i-33:chr(i) for i in range(33,127)}



def encrypt(word):
    txt=word.lower()
    txt=txt.replace(' ','')
    
    text=[x[i] for i in txt]
    
    my = []
    ly=[]
    for i in text:
        r = random.randrange(94)
        if i+r>=94:
            ly.append(r)
            my.append(m[i+r-94])
        else:
            ly.append(r)
            my.append(m[i+r])

    my=''.join(my)
    print('Cipher_text:',my,'\nKey',ly)
    
    
def decrypt(word,key):
    word=word.replace(' ','')
    text=[n[i] for i in word]
    my=[]
    #custom code
    text=np.array(text)
    key=np.array(key)
    data=text-key
    dec = [y[i] if i>0 else y[i+94] for i in data]
    dec=''.join(dec)
    print(dec)
    
    

    
encrypt("hello")
decrypt(")^)aV,4Utx-lVZ",[1, 57, 91, 53, 39, 4, 5, 30, 83, 70, 8, 51, 39, 37])
