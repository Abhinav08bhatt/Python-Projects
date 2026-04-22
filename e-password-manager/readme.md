> Make sure to install the python library :
```
pip install cryptography
```
or maybe :
```
sudo pacman -S python-cryptography
```

# Password Manager

 > A secure script that allows a user to view, add, and retrieve encrypted passwords from a file.

### Requirements :  
- Users must provide a Master Password to access the system.
- Use the cryptography.fernet library to encrypt and decrypt the saved passwords.
- Passwords must be saved to a persistent file (e.g., passwords.txt) along with the service name (e.g., Netflix | encrypted_value).
- Include functions for add() (to encrypt and save a new password) and view() (to retrieve and decrypt all saved passwords).
- Key Management The Fernet key must be saved to a separate, securely managed file (key.key). If this file is missing, the program should not run.
- Clear Exit: Implement a clean way to exit the program after logging out or completing an action.

> The youtube tutorial was not usable so had to learn to use the lib from documentation

> the key.key file is pre-built and the master.txt and will be made during the code password.txt.
- once u make teh master password, the only way to reset is by deleting the master.txt file