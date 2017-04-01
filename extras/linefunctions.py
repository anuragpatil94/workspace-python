# Use the file name mbox-short.txt as the file name
fname = raw_input('Enter file name: ')
fh = open(fname)
c=0
count=0
for line in fh:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
   
    line=line[20:]
    c=c+float(line)
    count=count+1
d=c/count
print "Average spam confidence: ", d
