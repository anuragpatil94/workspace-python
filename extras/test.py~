#fname = raw_input("Enter file name: ")
fh = open("romeo.txt")
lst = list()

i=0
for line in fh:
    line.rstrip()
    x=line.split()
    for i in range(len(x)):
        print x[i]
        if x[i] not in lst:
            lst.append(x[i])
    #lst.append(x[0])
lst.sort()
print lst

    



