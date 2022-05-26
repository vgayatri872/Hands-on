#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("names_file.txt",'r') as names:
    
    with open("content.txt",'r') as mail:     # open the mail content file
        #mail content
        content = mail.read() 
       
        for name in names:                  # loop over the names
            new_mail = "Hi"+name+content

            # this will create a mail file for each individual name
            with open(name.strip()+".txt",'w') as individual_mail:
                individual_mail.write(new_mail)     


# In[2]:


def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   with open(filename,'rb') as img_file:

       img_file.seek(163)

       a = img_file.read(2)

       height = (a[0] << 8) + a[1]

       a = img_file.read(2)

       width = (a[0] << 8) + a[1]

   print("The resolution of the image is",width,"x",height)

jpeg_res("img1.jpg")


# In[3]:


import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   h = hashlib.sha1()

   with open(filename,'rb') as file:

       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()

message = hash_file("track1.mp3")
print(message)


# In[4]:


from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)


# In[5]:


string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)


# In[6]:


from shutil import copyfile
copyfile("/root/a.txt", "/root/b.txt")


# In[7]:


with open("data_file.txt") as f:
    content_list = f.readlines()

print(content_list)

content_list = [x.strip() for x in content_list]
print(content_list)


# In[8]:


with open("my_file.txt", "a") as f:
   f.write("new text")


# In[9]:


import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])


# In[10]:


import os

file_name = os.path.basename('/root/file.ext')

print(os.path.splitext(file_name)[0])


# In[11]:


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("my_file.txt"))


# In[12]:


import glob, os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)


# In[13]:


import os.path, time

file = pathlib.Path('abc.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))


# In[14]:


import pathlib

print(pathlib.Path("my_file.txt").parent.absolute())

print(pathlib.Path().absolute())


# In[15]:


import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)

