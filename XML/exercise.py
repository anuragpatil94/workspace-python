import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')

uh = urllib.urlopen(url)
data = uh.read()


tree= ET.fromstring(data)
lst=tree.findall('comments/comment')
print len(lst)
sum=0
for stuff in lst:
    val=int(stuff.find('count').text)
    sum=sum+val
print sum
    
