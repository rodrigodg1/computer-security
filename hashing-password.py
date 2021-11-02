
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())

#password  = rodrigo
#hashed in data base
my_pass_in_data_base = b'\xc9\xfd\x92\xc75\xc7`\x99i\xa0\xabH\xb6\xdc/\xda\x85\xa0n\x13Q\x96W\x1c\x06p\x82"\xba\xf5\xa2\xe7'


def database(password):
    if (password == my_pass_in_data_base):
        return True
    else:
        return False
    
    


def verify(password):
    digest = hashes.Hash(hashes.SHA256())

    password = digest.update(password.encode())
    password = digest.finalize()
    
    if(database(password)):
        print("Success! Correct password")
        return True
    else:
        print("Error! Wrong password")
        print("try again :(")
        return False
        
    
    
  
passwordNotCorrect = True
    
while(passwordNotCorrect):
   password = input("type password \n> ")
   correct = verify(password)
   if(correct):
       passwordNotCorrect = False
   