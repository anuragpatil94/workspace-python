#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
#name = "mbox-short.txt"
handle = open(name)
stuff=dict()
lst=list()
for line in handle:
    if not line.startswith('From'):
        continue
    elif line.startswith("From:"):
        continue
    lst=line.split()
    a=lst[1]
    stuff[a]=stuff.get(a,0) + 1

count=None
maxmail=None
for mail,value in stuff.items():
    if count==None or value>count:
        count=value
        maxmail=mail
print maxmail,count







