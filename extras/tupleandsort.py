#10.2 Write a program to read through the mbox-short.txt and 
#figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below.


name = raw_input("Enter file:")
handle = open(name)
fhand=dict()
lst=list()
for line in handle:
    
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    lst=line.split()
    t=lst[5]
    t=t[:2]
    fhand[t]=fhand.get(t,0)+1
    

temp=list()
temp=sorted(fhand.items())
for k,v in temp:
    print k,v
