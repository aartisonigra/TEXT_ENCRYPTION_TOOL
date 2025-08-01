from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(text):
    return text + b" " * (16 - len(text) % 16)

def encrypt_text_to_file(plain_text, output_file):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plain_text.encode()))

    with open(output_file, "wb") as f:
        f.write(encrypted)

    return key

def decrypt_file_to_text(file_path, key):
    with open(file_path, "rb") as f:
        encrypted = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.rstrip(b" ").decode("utf-8")
