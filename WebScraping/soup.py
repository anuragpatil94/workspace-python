import urllib
from BeautifulSoup import *
url=raw_input('Enter URL:')
html=urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
a=0
for tag in tags:
   # Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   
   a=a+int(tag.contents[0])
print 'A:',a
