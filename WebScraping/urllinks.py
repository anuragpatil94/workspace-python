import urllib
from BeautifulSoup import *
url=urllib.urlopen(raw_input('Enter URL:')).read()

count=raw_input('Enter Count:')
position=raw_input('Enter Position:')
count=int(count)
while count!=0:
	soup = BeautifulSoup(url)
	tags=soup('a')
	
	t=0
	for tag in tags:
		t=t+1
		if not t==18:
			continue
		ut=tag.get('href',None)
        print "Retriving:", ut
        url = urllib.urlopen(ut).read()
        count=count-1
        m=tag.contents[0]
        
        continue
   

