fhand=open('dataset.txt')
lst=list()
dset=dict()
classes=dict()
#text=fhand.read()
#words=text.split()
#classes
for lines in fhand:
	x=lines.split()
	print x[4]
	classes[x[4]]=classes.get(x[4],0)+1
print classes.items()

c1=float((classes.values()[0])/4)
c2=float((classes.values()[1])/4)

print float(c1),c2
	 
print "finish"
