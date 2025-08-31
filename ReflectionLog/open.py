import json
from lockcommand import unlock_journal


while True:
    try:
        passphrase = input("Enter the passphrase")
        data = unlock_journal(passphrase, infile="memory.enc", saltfile="salt.bin")

# Write it back as plaintext JSON
        with open("memory.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Restored memory.json from memory.enc")
        break
    except:
        print("Please enter the right passcode")


# Decrypt to Python object

