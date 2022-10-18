import numpy as np




def encrypt(text,key):
    
    #lets create english alphabet mapping and the reverse of it
    EAM={chr(i):i-97 for i in range(97,123)}
    REAM = {i-97:chr(i) for i in range(97,123)}
    
    key=key.lower()
    key=key.replace(" ","")
    key_index = [EAM[i] for i in key]
    block = len(key)//2
    key_array=np.array(key_index).reshape(block,block)
    
    text=text.lower()
    text=text.replace(" ","")
    plain_index = [EAM[i] for i in text]
    plain_array = np.array(plain_index)
    plain_split=np.split(plain_array,len(plain_array)/block)
       
    cipher_block=[np.matmul(plain_split[i],key_array)%26 for i in range(len(plain_split))]
    cipher_array=np.concatenate(cipher_block)
    cipher_decrypt=[REAM[i] for i in cipher_array]
    cipher_decrypt=''.join(cipher_decrypt)
    
    print("cipher Text:-",cipher_decrypt)
    print("key array:\n",key_array)
    


def decrypt(text,key):
    EAM = {chr(i):i-97 for i in range(97,123)}
    REAM = { i-97 : chr(i) for i in range(97,123)}
    
    key=key.lower()
    key_index = [EAM[i] for i in key]
    block = len(key)//2
    key_array=np.array(key_index).reshape(block,block)
    
    rounded_det = round(np.linalg.det(key_array))
    inverse = np.linalg.inv(key_array)
    adj=inverse*rounded_det
    matrix = pow(rounded_det,-1,26)
    key_inverse = (matrix * adj)%26
    key_inverse = np.concatenate(key_inverse)
    key_inverse =[ round(key_inverse[i]) for i in range(len(key_inverse))]
    key_inverse = np.array(key_inverse).reshape(block,block)
    
    cipher_array=[EAM[i] for i in text]
    cipher_array=np.array(cipher_array)
    text_split=np.split(cipher_array,len(cipher_array)/block)
    text_block = [(np.matmul(text_split[i],key_inverse))%26 for i in range(len(text_split))]
    text_array=np.concatenate(text_block)
    text_decrypt=[REAM[i] for i in text_array]
    text_decrypt=''.join(text_decrypt)    
        
    print("matrix of key inverse:\n",key_inverse)
    print("decrypted text:-",text_decrypt)    
    
    
    
    


decrypt("fyutoeelzb","text")
    
    
    