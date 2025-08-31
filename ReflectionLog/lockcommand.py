import os, json, base64
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# -------------------------------
# 1. Derive Key from Passphrase
# -------------------------------
def derive_key(passphrase: str, salt: bytes) -> bytes:
    """Turn a passphrase + salt into a Fernet key"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))

def lock_journal(passphrase: str, infile="memory.json", outfile="memory.enc", saltfile="salt.bin"):
    # Generate or load salt
    if not os.path.exists(saltfile):
        salt = os.urandom(16)
        with open(saltfile, "wb") as f:
            f.write(salt)
    else:
        with open(saltfile, "rb") as f:
            salt = f.read()

    key = derive_key(passphrase, salt)
    fernet = Fernet(key)

    # Read plaintext journal
    with open(infile, "rb") as f:
        data = f.read()

    # Encrypt
    encrypted = fernet.encrypt(data)

    # Save encrypted journal
    with open(outfile, "wb") as f:
        f.write(encrypted)

    print(f"🔒 Locked {infile} → {outfile}")

    # Optionally delete the original plaintext for safety
    os.remove(infile)
    print(f"❌ Deleted {infile} (only {outfile} remains locked).")


def unlock_journal(passphrase: str, infile="memory.enc", saltfile="salt.bin"):
    # Load salt
    with open(saltfile, "rb") as f:
        salt = f.read()

    key = derive_key(passphrase, salt)
    fernet = Fernet(key)

    # Read encrypted file
    with open(infile, "rb") as f:
        encrypted = f.read()

    # Decrypt → Python object
    decrypted = fernet.decrypt(encrypted)
    return json.loads(decrypted)

