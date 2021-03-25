str1='214u77bsabdafja'

p=str1
print(str1[0:4])

print(str1[4])
import re

a=re.search(':',str1)
print(a)


(a,b)=str1.split('b',1)
print(a,b)