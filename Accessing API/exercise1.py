

# In this code the real problem was thati didnt take str(data) and the iterate in for loop for range.

import urllib
import json
input=raw_input('Enter the URL:')
html=urllib.urlopen(input)
data=html.read()

print len(data)
try:
    info=json.loads(str(data))
except:
    info=None
sum=0
print "Count:",len(info["comments"])
d=json.dumps(info, indent=4)
#print d
#print range(len(info))

for line in range(len(info["comments"])):
    
    #print info["comments"][line]["count"]
    
    sum=sum+(info["comments"][line]["count"])
print "Sum: ",  sum

