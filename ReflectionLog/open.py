import json
from lockcommand import unlock_journal
import json
from sentence_transformers import SentenceTransformer,util


with open("tags.json","r") as f:
    data = json.load(f)

tags  = data[0]["tags"]
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(tags)
strr = model.encode("thermod")
        
cos_sim = util.cos_sim(embeddings, model.encode("poe"))
print(cos_sim)
while True:
    
    try:
        passphrase = input("What did you talk about in your last entry?? -")
        cos_sim = util.cos_sim(embeddings, model.encode(passphrase))
        if max(cos_sim) >0.5:
            print("congratulations")
            
            data = unlock_journal("3937", infile="memory.enc", saltfile="salt.bin")
            with open("memory.json", "w") as f:
                json.dump(data, f, indent=4)

            print("Restored memory.json from memory.enc")
            break
        else:
            print("Password incorrect.")

# Write it back as plaintext JSON
        
    except:
        print("Please enter the right passcode")


# Decrypt to Python object

