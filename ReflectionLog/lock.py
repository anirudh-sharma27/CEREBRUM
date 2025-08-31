from lockcommand import lock_journal, unlock_journal
from datetime import datetime




# First time: lock your existing memory.json
try:
    lock_journal("3937")

# Later: unlock it
    data = unlock_journal("3937")
    print("Journal locked")  # show first entry
except:
    print("It is already locked.")
# Add a new entry

