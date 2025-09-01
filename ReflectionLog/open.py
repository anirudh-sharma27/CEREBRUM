import json
from lockcommand import unlock_journal

from sentence_transformers import SentenceTransformer,util
#from lock import tags

data = unlock_journal("3937", infile="memory.enc", saltfile="salt.bin")
with open("memory.json", "w") as f:
            json.dump(data, f, indent=4)



y = input("please tell the passphrase")
    
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(tags[0])

    
        



while True:
    
    try:
        passphrase = input("What did you talk about in your last entry?? -")
        cos_sim = util.cos_sim(embeddings, passphrase)
        if max(cos_sim) >0.75:
            print("congratulations")
            
            data = unlock_journal("3937", infile="memory.enc", saltfile="salt.bin")
        else:
            print("Password incorrect.Try again")

# Write it back as plaintext JSON
        with open("memory.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Restored memory.json from memory.enc")
        break
    except:
        print("Please enter the right passcode")


# Decrypt to Python object

