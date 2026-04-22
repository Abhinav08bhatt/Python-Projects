from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    print(f"Key : {key.decode()}")
    with open("e-password-manager/learn/file-key.key","wb") as fk:
        fk.write(key)

write_key()

with open('e-password-manager/learn/file-key.key', 'rb') as fk:
 key = fk.read()

fernet = Fernet(key)

# opening the original file to encrypt
with open('e-password-manager/learn/text.txt', 'rb') as file:
 original = file.read()
 
 # encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and 
# writing the encrypted data
with open('e-password-manager/learn/text.txt', 'wb') as encrypted_file:
 encrypted_file.write(encrypted)

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('e-password-manager/learn/text.txt', 'rb') as enc_file:
 encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# # writing the decrypted data
# with open('e-password-manager/learn/text.txt', 'wb') as dec_file:
#  dec_file.write(decrypted)

print(original.decode())
print("\n")
print(encrypted.decode())
print("\n")
print(decrypted.decode())
print("\n")