import re 
hand=open('/home/anurag/PythonWorkspace/RegularExpression/regex_sum_226418.txt')
x=hand .read()

y=re.findall('[0-9]+',x) 

print len(y)
sum=0
for i in range(len(y)):
    sum=sum+int(y[i])
print sum        
        
