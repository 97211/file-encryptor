from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated: secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    print(f"{filename} encrypted → {filename}.encrypted")

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    original_name = filename.replace(".encrypted", "")
    with open("decrypted_" + original_name, "wb") as file:
        file.write(decrypted_data)
    print(f"{filename} decrypted → decrypted_{original_name}")

if __name__ == "__main__":
    print("=== File Encryptor ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter choice: ")
    
    if choice == "1":
        generate_key()
    elif choice == "2":
        filename = input("Enter filename to encrypt: ")
        key = load_key()
        encrypt_file(filename, key)
    elif choice == "3":
        filename = input("Enter filename to decrypt: ")
        key = load_key()
        decrypt_file(filename, key)
    else:
        print("Invalid choice")
