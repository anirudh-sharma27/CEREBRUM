from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

fernet = Fernet(key)

msg = b"yayy crypto"

enc_msg = fernet.encrypt(msg)

print(msg,enc_msg)