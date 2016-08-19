import uuid

import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


uniqueIDStr = "#" + uuid.uuid4().hex
print(uniqueIDStr)
addToClipBoard(uniqueIDStr)

