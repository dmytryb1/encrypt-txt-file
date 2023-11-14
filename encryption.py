from cryptography.fernet import Fernet

def write_key():
    
    #Generate a key and save it to a file.

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    
    #Loads the key from the current directory

    return open("key.key", "rb").read()


def encrypt(filename, key):
    
    #Given a filename and key (bytes) this encrypts the file
    f = Fernet(key)
    with open(filename, "rb") as file:
        #Read all file data
        file_data = file.read()
        #encrypt data
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)




write_key()
file = "readme.txt"
key = load_key()
encrypt(file, key)
