import os
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad
import hashlib

def get_master_key(master_password: str, device_salt: str):
    salt = device_salt.encode()
    return hashlib.pbkdf2_hmac('sha256', master_password.encode(), salt, 1000000)

def encrypt(plaintext: str, master_key: str) -> bytes:
    iv = os.urandom(16)
    cipher = AES.new(master_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext)

def decrypt(ciphertext: bytes, master_key: str) -> str:
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    cipher = AES.new(master_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[16:]), AES.block_size).decode()
